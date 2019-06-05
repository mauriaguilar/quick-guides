import code

@pytest.mark.parametrize("param_a,param_b,expected",
    [
        (1,2,3),
        (2,3,5),
        (3,5,8)
    ]
)
def test_sum(param_a,param_b,expected):
    assert(code.sum(param_a,param_b), expected)