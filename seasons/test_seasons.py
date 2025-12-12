import pytest
from seasons import difference

def main():
    test()

def test():
    assert difference("2024-12-12") == "Five hundred twenty-five thousand, six hundred minutes"
    assert difference("2023-12-12") == "One million, fifty-two thousand, six hundred forty minutes"
    with pytest.raises(SystemExit, match="Invalid"):
        difference("August 13, 2024")



if __name__ == "__main__":
    main()



