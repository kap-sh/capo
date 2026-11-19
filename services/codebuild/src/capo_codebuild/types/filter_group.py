"""Generated from Smithy shape ``com.amazonaws.codebuild#FilterGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.webhook_filter

FilterGroup: TypeAlias = list["capo_codebuild.types.webhook_filter.WebhookFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterGroup) -> list:
    import capo_codebuild.types.webhook_filter

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.webhook_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterGroup:
    import capo_codebuild.types.webhook_filter

    out: FilterGroup = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.webhook_filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterGroup) -> list:
    import capo_codebuild.types.webhook_filter

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.webhook_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterGroup:
    import capo_codebuild.types.webhook_filter

    out: FilterGroup = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.webhook_filter.deserialize_cbor(item))
    return out
