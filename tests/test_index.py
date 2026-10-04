from sneppx_hub.index import ModelIndex


def test_add_get():
    idx = ModelIndex()
    idx.add("m1", "s3://m1", tags=["llm"], signed=True)
    assert idx.get("m1")["uri"] == "s3://m1"


def test_search_signed_only():
    idx = ModelIndex()
    idx.add("a", "u1", tags=["x"], signed=True)
    idx.add("b", "u2", tags=["x"], signed=False)
    assert len(idx.search(tag="x", signed_only=True)) == 1
