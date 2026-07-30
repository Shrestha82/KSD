def test_smoke():
    """A minimal smoke test so CI has at least one test to run."""
    assert True


def test_smoke_trigger():
    """Trigger CI rerun by adding another trivial test."""
    assert 1 == 1
