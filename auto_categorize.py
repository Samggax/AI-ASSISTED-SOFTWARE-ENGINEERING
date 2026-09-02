# auto_categorize.py  (AI-generated, first version)
 
KEYWORDS = {
    "electrical": ["Fan", "Switch", "Wiring", "Spark", "Short circuit"],
    "plumbing":   ["Tap", "Leak", "Pipe", "Drain", "Toilet"],
    "wifi":       ["Wifi", "Router", "Internet", "Network"],
    "furniture":  ["Chair", "Table", "Bed", "Cupboard"],
}
 
def guess_category(description: str) -> str:
    for category, words in KEYWORDS.items():
        for w in words:
            if w in description:      # <-- bug: exact case match only
                return category
    return "other"
