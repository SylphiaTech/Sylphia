from backend.cache_service import ResultCache

def test_cache_add_and_get():
    cache = ResultCache(max_size=2)
    cache.add_result("one")
    cache.add_result("two")
    assert cache.get_latest() == ["one", "two"]
    cache.add_result("three")
    assert cache.get_latest() == ["two", "three"]