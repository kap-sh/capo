"""Generated from Smithy shape ``com.amazonaws.snowball#S3ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.s3_resource

S3ResourceList: TypeAlias = list["capo_snowball.types.s3_resource.S3Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ResourceList) -> list:
    import capo_snowball.types.s3_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.s3_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> S3ResourceList:
    import capo_snowball.types.s3_resource

    out: S3ResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.s3_resource.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ResourceList) -> list:
    import capo_snowball.types.s3_resource

    out: list = []
    for item in value:
        out.append(capo_snowball.types.s3_resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> S3ResourceList:
    import capo_snowball.types.s3_resource

    out: S3ResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.s3_resource.deserialize_cbor(item))
    return out
