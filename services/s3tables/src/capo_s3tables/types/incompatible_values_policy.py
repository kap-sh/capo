"""Generated from Smithy shape ``com.amazonaws.s3tables#IncompatibleValuesPolicy``."""

from typing import Literal, TypeAlias, cast

IncompatibleValuesPolicy: TypeAlias = Literal[
    "fail",
    "setNull",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleValuesPolicy) -> str:
    return value


def deserialize_json(data: str) -> IncompatibleValuesPolicy:
    return cast(IncompatibleValuesPolicy, data)
