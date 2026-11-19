"""Generated from Smithy shape ``com.amazonaws.codedeploy#OnPremisesTagSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.tag_filter_list

OnPremisesTagSetList: TypeAlias = list[
    "capo_codedeploy.types.tag_filter_list.TagFilterList"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPremisesTagSetList) -> list:
    import capo_codedeploy.types.tag_filter_list

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OnPremisesTagSetList:
    import capo_codedeploy.types.tag_filter_list

    out: OnPremisesTagSetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OnPremisesTagSetList) -> list:
    import capo_codedeploy.types.tag_filter_list

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.tag_filter_list.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> OnPremisesTagSetList:
    import capo_codedeploy.types.tag_filter_list

    out: OnPremisesTagSetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.tag_filter_list.deserialize_cbor(item))
    return out
