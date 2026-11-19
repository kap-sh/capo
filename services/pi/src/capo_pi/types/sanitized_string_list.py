"""Generated from Smithy shape ``com.amazonaws.pi#SanitizedStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.sanitized_string

SanitizedStringList: TypeAlias = list["capo_pi.types.sanitized_string.SanitizedString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SanitizedStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SanitizedStringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SanitizedStringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SanitizedStringList:
    return [item for item in data if item is not None]
