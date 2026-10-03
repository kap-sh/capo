"""Generated from Smithy shape ``com.amazonaws.signin#TokenType``."""

from typing import TypeAlias

"""Token type parameter indicating credential usage A parameter which indicates to the client how the token must be used. Value is "aws_sigv4" (instead of typical "Bearer" for other OAuth systems) to indicate that the client must de-serialize the token and use it to generate a signature."""
TokenType: TypeAlias = str
