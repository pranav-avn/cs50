from numb3rs import validate

def main():
    test_validate1()
    test_validate2()

def test_validate1():

    assert validate(r"127.0.0.1") == True
    assert validate(r"ip") == False
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"192.512.2.1000") == False
    assert validate(r"147.241.225.134") == True
    assert validate(r"2d52:9676:39e8:09f0:7787:aa15:fdd2:574f") == False
    assert validate(r"64.128.256.512") == False

def test_validate2():

    assert validate(r"255.255.255.256") == False
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"275.255.255.255") == False
    assert validate(r"1.275.275.275") == False
    assert validate(r"255.255.255.255") == True

if __name__ == "__main__":
    main()
