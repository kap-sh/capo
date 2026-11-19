"""Generated from Smithy shape ``com.amazonaws.codebuild#FilterGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.filter_group

FilterGroups: TypeAlias = list["capo_codebuild.types.filter_group.FilterGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterGroups) -> list:
    import capo_codebuild.types.filter_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.filter_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterGroups:
    import capo_codebuild.types.filter_group

    out: FilterGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.filter_group.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterGroups) -> list:
    import capo_codebuild.types.filter_group

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.filter_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterGroups:
    import capo_codebuild.types.filter_group

    out: FilterGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.filter_group.deserialize_cbor(item))
    return out
