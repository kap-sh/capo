"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""Why the request failed validation, coarsely. Matches the shape `partnercentralbenefits` ships (`ValidationException$Reason`) so a client that already reads one Partner Central API's validation errors reads this one the same way."""
ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "CANNOT_PARSE",
    "OTHER",
    "CAMPAIGN_INCOMPLETE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
