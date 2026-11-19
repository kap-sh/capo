"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

BundleAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BundleAssociatedResourceType:
    return cast(BundleAssociatedResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BundleAssociatedResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> BundleAssociatedResourceType:
    return cast(BundleAssociatedResourceType, data)
