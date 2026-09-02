# test_auto_categorize.py
from auto_categorize import guess_category
 
def test_electrical_keyword_lowercase():
    assert guess_category("the fan in room 204 is sparking") == "electrical"
 
def test_plumbing_keyword_lowercase():
    assert guess_category("tap in the bathroom keeps leaking") == "plumbing"
 
def test_no_keyword_returns_other():
    assert guess_category("the room smells a bit odd") == "other"
