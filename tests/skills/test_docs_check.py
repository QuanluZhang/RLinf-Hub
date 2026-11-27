# Copyright 2026 The RLinf Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Offline unit tests for .agents/skills/docs/check.py and check_writing.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
DOCS_DIR = SKILLS_DIR / "docs"


def _load_docs_check():
    for d in (SKILLS_DIR, DOCS_DIR):
        if str(d) not in sys.path:
            sys.path.insert(0, str(d))
    spec = importlib.util.spec_from_file_location(
        "hub_docs_check", DOCS_DIR / "check.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_parity_check(tmp_path: Path) -> None:
    check = _load_docs_check()
    route = sys.modules["route"]

    proj = tmp_path / "models" / "demo"
    proj.mkdir(parents=True)
    (proj / "README.md").write_text("# Demo\n", encoding="utf-8")

    # Missing README.zh-CN.md -> major
    findings = check.check_parity(
        [route.Change("A", "models/demo/README.md")], root=tmp_path
    )
    assert len(findings) == 1
    assert findings[0].severity == "major"
    assert findings[0].rule == "docs/parity"

    # Both exist, only EN edited -> minor
    (proj / "README.zh-CN.md").write_text("# Demo\n", encoding="utf-8")
    findings = check.check_parity(
        [route.Change("M", "models/demo/README.md")], root=tmp_path
    )
    assert len(findings) == 1
    assert findings[0].severity == "minor"

    # Both updated -> clean
    findings = check.check_parity(
        [
            route.Change("M", "models/demo/README.md"),
            route.Change("M", "models/demo/README.zh-CN.md"),
        ],
        root=tmp_path,
    )
    assert findings == []


def test_markdown_syntax_fences_tables_and_prompts(tmp_path: Path) -> None:
    check = _load_docs_check()
    md = tmp_path / "bad.md"
    md.write_text(
        "# Title\n\n"
        "    | A | B |\n"
        "    |---|---|\n\n"
        "```bash\n"
        "$ pytest -q\n"
        "```\n\n"
        "```python\n"
        "x = 1\n",
        encoding="utf-8",
    )
    findings = check.check_markdown_syntax(md, "bad.md")
    by_sev = {(f.severity, f.rule) for f in findings}
    assert ("critical", "docs/markdown") in by_sev
    assert ("major", "docs/markdown") in by_sev
    assert ("minor", "docs/markdown") in by_sev


def test_links_check_broken_placeholder_and_redirect(tmp_path: Path) -> None:
    check = _load_docs_check()
    (tmp_path / "ok.md").write_text("ok", encoding="utf-8")
    md = tmp_path / "doc.md"
    md.write_text(
        "[good](ok.md)\n"
        "[broken](missing.md)\n"
        "[placeholder](https://example.com/model)\n"
        "![img](https://github.com/RLinf/misc/raw/main/pic/logo.svg)\n",
        encoding="utf-8",
    )
    findings = check.check_links(md, "doc.md", root=tmp_path)
    assert len(findings) == 3
    assert any(
        f.severity == "major" and "broken relative link" in f.message for f in findings
    )
    assert any(
        f.severity == "major" and "placeholder URL" in f.message for f in findings
    )
    assert any(
        f.severity == "minor" and "raw.githubusercontent.com" in f.message
        for f in findings
    )


def test_writing_rules_en_zh_hard_wrap_and_structure(tmp_path: Path) -> None:
    check = _load_docs_check()
    cw = check.check_writing

    en = tmp_path / "models" / "demo" / "README.md"
    en.parent.mkdir(parents=True)
    en.write_text(
        "# Demo\n\n"
        "[English](README.md) | [简体中文](README.zh-CN.md)\n\n"
        "This powerful adapter simply leverages RLinf.\n\n"
        "## Install\n\nRun pip.\n\n"
        "## Usage\n\nRun script.\n\n"
        "## Verification\n\nRun pytest.\n",
        encoding="utf-8",
    )
    en_findings = cw.check_page(en, "models/demo/README.md", new=True)
    assert all(f.rule == "docs/en-style" for f in en_findings)
    assert len(en_findings) >= 3

    zh = tmp_path / "models" / "demo" / "README.zh-CN.md"
    zh.write_text(
        "# Demo\n\n"
        "[English](README.md) | [简体中文](README.zh-CN.md)\n\n"
        "值得注意的是，这段中文在源文件里\n"
        "被强行折成了两行，而且对模型进行评估。\n\n"
        "## 安装\n\n安装依赖。\n",
        encoding="utf-8",
    )
    zh_findings = cw.check_page(zh, "models/demo/README.zh-CN.md", new=True)
    rules = {f.rule for f in zh_findings}
    assert "docs/structure" in rules
    assert "docs/zh-hard-wrap" in rules
    assert "docs/zh-style" in rules
