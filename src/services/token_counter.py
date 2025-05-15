def count_tokens(text: str) -> int:
    """Count tokens in a text string.
    
    This is a simplified implementation.
    In production, use a proper tokenizer like tiktoken.
    """
    return len(text.split())
