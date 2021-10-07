import softdes


def test_lambda_handler_should_throw_error_with_invalid_function():
    test_code = """def desafio1(test_input):
        pass"""

    event = {"ndes": "0", "code": test_code, "args": ["0"], "resp": "0", "diag": "0"}

    context = ""
    response = softdes.lambda_handler(event)
    assert response == "Nome da função inválido. Usar 'def desafio0(...)'"


def test_lambda_handler_should_return_right_answer():
    test_code = """def desafio1(test_input):
        return 2 + int(test_input)"""

    event = {"ndes": "1", "code": test_code, "args": ["3"], "resp": [5], "diag": ["3"]}

    context = ""
    errors = softdes.lambda_handler(event)
    assert errors == ""


def test_lambda_handler_should_return_wrong_answer():
    test_code = """def desafio1(test_input):
        return 2 + int(test_input)"""

    event = {
        "ndes": "1",
        "code": test_code,
        "args": ["3"],
        "resp": [3],
        "diag": ["Wrong sum"],
    }

    context = ""
    errors = softdes.lambda_handler(event)
    assert errors == "Wrong sum"
