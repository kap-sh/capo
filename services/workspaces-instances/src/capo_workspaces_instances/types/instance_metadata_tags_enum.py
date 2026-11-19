"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMetadataTagsEnum``."""

from typing import Literal, TypeAlias, cast

InstanceMetadataTagsEnum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceMetadataTagsEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceMetadataTagsEnum:
    return cast(InstanceMetadataTagsEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceMetadataTagsEnum) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceMetadataTagsEnum:
    return cast(InstanceMetadataTagsEnum, data)
