"""Generated from Smithy shape ``com.amazonaws.appintegrations#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal["API_KEY",]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
