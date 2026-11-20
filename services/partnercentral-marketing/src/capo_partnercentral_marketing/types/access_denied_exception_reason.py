"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

"""Why an `AccessDeniedException` was raised, when it isn't IAM's."""
AccessDeniedExceptionReason: TypeAlias = Literal[
    "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_cbor(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
