"""Generated from Smithy shape ``com.amazonaws.pi#MetricTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.sanitized_string

MetricTypeList: TypeAlias = list["capo_pi.types.sanitized_string.SanitizedString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetricTypeList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricTypeList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MetricTypeList:
    return [item for item in data if item is not None]
