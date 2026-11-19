"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.revision_info

RevisionInfoList: TypeAlias = list["capo_codedeploy.types.revision_info.RevisionInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionInfoList) -> list:
    import capo_codedeploy.types.revision_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.revision_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RevisionInfoList:
    import capo_codedeploy.types.revision_info

    out: RevisionInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.revision_info.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevisionInfoList) -> list:
    import capo_codedeploy.types.revision_info

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.revision_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RevisionInfoList:
    import capo_codedeploy.types.revision_info

    out: RevisionInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.revision_info.deserialize_cbor(item))
    return out
