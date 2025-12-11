from twttr import shorten

def main():
    test_twttr()

def test_twttr_shortenable():
    assert shorten("word") == "wrd"
    assert shorten("WORD") == "WRD"
    assert shorten("WorD") == "WrD"

def test_twttr_unalterable():
    assert shorten("rhythm") == "rhythm"
    assert shorten("bcd") == "bcd"

def test_twttr_num():
    assert shorten("1234") == "1234"
    assert shorten(".!?,") == ".!?,"

if __name__ == "__main__":
    main()
