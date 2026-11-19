"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtSigningAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""<p>A JSON Web Signature (JWS) signing algorithm. Valid values are <code>RS256</code>, <code>RS384</code>, <code>RS512</code>, <code>ES256</code>, <code>ES384</code>, and <code>ES512</code>. HMAC (<code>HS256</code>, <code>HS384</code>, <code>HS512</code>) and <code>none</code> are not valid values.</p>"""
JwtSigningAlgorithm: TypeAlias = Literal[
    "RS256",
    "RS384",
    "RS512",
    "ES256",
    "ES384",
    "ES512",
]


# --- restJson1 ser/de ---
def serialize_json(value: JwtSigningAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> JwtSigningAlgorithm:
    return cast(JwtSigningAlgorithm, data)
