"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.resource_arn

ResourceList: TypeAlias = list[
    "capo_application_insights.types.resource_arn.ResourceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ResourceList:
    return [item for item in data if item is not None]
