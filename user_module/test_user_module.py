import pytest
from user_module_functions import (
    hash_password,
    verify_password,
    register_user,
    login_user
)

@pytest.fixture
def users_db():
    return {}

# -------------------
# Password Tests
# -------------------

def test_hash_password_success():
    hashed = hash_password("12345678")
    assert hashed != "12345678"
    assert isinstance(hashed, str)


def test_hash_password_empty():
    with pytest.raises(ValueError):
        hash_password("")


def test_verify_password_correct():
    hashed = hash_password("password")
    assert verify_password("password", hashed)


@pytest.mark.xfail(reason="Intentional fail: verifying wrong password incorrectly")
def test_verify_password_wrong():
    hashed = hash_password("password")
    # intentional fail: assert True instead of False
    assert verify_password("wrong", hashed)  # هذا سيظهر كـ xfail


# -------------------
# Register Tests
# -------------------

def test_register_user_success(users_db):
    user = register_user("test@test.com", "12345678", users_db)
    assert user["email"] == "test@test.com"
    assert "password" in user


@pytest.mark.xfail(reason="Intentional fail: registering existing user incorrectly")
def test_register_existing_user(users_db):
    register_user("test@test.com", "12345678", users_db)
    # intentional fail: not using raises → سيظهر xfail
    register_user("test@test.com", "12345678", users_db)


@pytest.mark.xfail(reason="Intentional fail: missing data not raising error")
def test_register_missing_data(users_db):
    # intentional fail: ignoring exception
    register_user("", "12345678", users_db)


# -------------------
# Login Tests
# -------------------

def test_login_success(users_db):
    register_user("test@test.com", "12345678", users_db)
    assert login_user("test@test.com", "12345678", users_db)


def test_login_wrong_password(users_db):
    register_user("test@test.com", "12345678", users_db)
    assert not login_user("test@test.com", "wrong", users_db)


@pytest.mark.xfail(reason="Intentional fail: user not found returns True incorrectly")
def test_login_user_not_found(users_db):
    # intentional fail: assert True instead of False
    assert login_user("notfound@test.com", "123", users_db)
