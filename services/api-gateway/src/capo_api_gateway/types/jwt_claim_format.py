"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtClaimFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The format of an additional claim value. The only valid value is <code>SINGLE_STRING</code>.</p>"""
JwtClaimFormat: TypeAlias = Literal["SINGLE_STRING",]


# --- restJson1 ser/de ---
def serialize_json(value: JwtClaimFormat) -> str:
    return value


def deserialize_json(data: str) -> JwtClaimFormat:
    return cast(JwtClaimFormat, data)
