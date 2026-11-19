"""Generated from Smithy shape ``com.amazonaws.kendraranking#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra_ranking.types.tag

TagList: TypeAlias = list["capo_kendra_ranking.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    import capo_kendra_ranking.types.tag

    out: list = []
    for item in value:
        out.append(capo_kendra_ranking.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TagList:
    import capo_kendra_ranking.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kendra_ranking.types.tag.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagList) -> list:
    import capo_kendra_ranking.types.tag

    out: list = []
    for item in value:
        out.append(capo_kendra_ranking.types.tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TagList:
    import capo_kendra_ranking.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kendra_ranking.types.tag.deserialize_cbor(item))
    return out
