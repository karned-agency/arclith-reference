from pathlib import Path


PROJECT_ROOT = Path(__file__).parents[2]


def test_public_references_use_karned_agency() -> None:
    previous_owner = "karned" + "-rekipe"
    public_files = [
        PROJECT_ROOT / "README.md",
        PROJECT_ROOT / "QUICKSTART.md",
        PROJECT_ROOT / ".github" / "scripts" / "patch-framework-source.sh",
    ]

    assert all(
        previous_owner not in path.read_text(encoding="utf-8")
        for path in public_files
    )
    assert "https://github.com/karned-agency/arclith" in public_files[0].read_text(
        encoding="utf-8"
    )
