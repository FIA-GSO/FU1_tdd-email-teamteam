import pytest
from password_validation import is_valid_password

@pytest.mark.parametrize("password", [
    ("3wG.-aM8")
,   ("fk]6=0ME")
,    ("CGFuK5[6|")
,    ("L-BW#45UjM")
,    ("|EoP82X)Ac")
,    ("3ID]V=k8Bb")
,    ("gRMsSK96}8;")
,    ("R-QX^x8A@5m3")
,    ("U8Lk21754KAFPZ9w0OYIAEJFV")
,    ("YAL1N03pegzT4GX7c8295CWRw6SUVPVN")
,    ("NJ15tOBR9XDFAQh0SZ2378BsLU6c")
,    ("N67xAf4B13i9PRbI8WgEQ5F2HS0urP")
])

def test_is_valid_password__valid(password):
    #Arrange
    expectedResult = True

    #Act
    result = is_valid_password(password)

    #Assert
    assert result == expectedResult

@pytest.mark.parametrize("password", [
    ("HelloWorld")
,   ("Hallo")
,    ("12")
,    ("hi45")
,    ("Sebastian")
,    ("Fatih")
,    ("12345")
,    ("..-!++++*'''#")
,    ("#")
,    ("+*34,5f")
,    ("0987654321")
])

def test_is_valid_password__failed(password):
    #Arrange
    expectedResult = False

    #Act
    result = is_valid_password(password)

    #Assert
    assert result == expectedResult