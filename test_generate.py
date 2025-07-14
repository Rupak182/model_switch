from generate import count_output_tokens

def test_token_counting():
    result= count_output_tokens("Hello, how are you?", "Qwen/Qwen2.5-Coder-32B-Instruct")
    assert isinstance(result, int), "The result should be an integer."
    assert result > 0, "The token count should be greater than zero."

def test_token_counting_invalid():
    result = count_output_tokens("test", "invalid/model")
    assert isinstance(result, int), "The result should be an integer."
    assert result == -1, "The token count for an invalid model should be -1."

