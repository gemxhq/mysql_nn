
def test(*args, **kwargs):
    if "password" in kwargs:
        kwargs.pop("passwrod")
