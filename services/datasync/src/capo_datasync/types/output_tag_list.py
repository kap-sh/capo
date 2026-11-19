"""Generated from Smithy shape ``com.amazonaws.datasync#OutputTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.tag_list_entry

OutputTagList: TypeAlias = list["capo_datasync.types.tag_list_entry.TagListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputTagList) -> list:
    import capo_datasync.types.tag_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.tag_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutputTagList:
    import capo_datasync.types.tag_list_entry

    out: OutputTagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.tag_list_entry.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OutputTagList) -> list:
    import capo_datasync.types.tag_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.tag_list_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OutputTagList:
    import capo_datasync.types.tag_list_entry

    out: OutputTagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.tag_list_entry.deserialize_cbor(item))
    return out
