"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#TokenParts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.auth_token_key
    import capo_lambda_microvms.types.auth_token_value

TokenParts: TypeAlias = dict[
    "capo_lambda_microvms.types.auth_token_key.AuthTokenKey",
    "capo_lambda_microvms.types.auth_token_value.AuthTokenValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TokenParts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TokenParts:
    out: TokenParts = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
