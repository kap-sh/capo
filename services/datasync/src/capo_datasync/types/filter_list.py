"""Generated from Smithy shape ``com.amazonaws.datasync#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.filter_rule

FilterList: TypeAlias = list["capo_datasync.types.filter_rule.FilterRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterList) -> list:
    import capo_datasync.types.filter_rule

    out: list = []
    for item in value:
        out.append(capo_datasync.types.filter_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterList:
    import capo_datasync.types.filter_rule

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.filter_rule.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterList) -> list:
    import capo_datasync.types.filter_rule

    out: list = []
    for item in value:
        out.append(capo_datasync.types.filter_rule.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterList:
    import capo_datasync.types.filter_rule

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.filter_rule.deserialize_cbor(item))
    return out
