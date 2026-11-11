"""Generated from Smithy shape ``com.amazonaws.lakeformation#UserDefinedFunctionWildcard``."""

from typing_extensions import TypedDict


class UserDefinedFunctionWildcard(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: UserDefinedFunctionWildcard) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UserDefinedFunctionWildcard:
    out: UserDefinedFunctionWildcard = {}  # type: ignore[typeddict-item]
    return out
