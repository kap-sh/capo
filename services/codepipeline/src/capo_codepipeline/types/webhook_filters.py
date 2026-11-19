"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.webhook_filter_rule

WebhookFilters: TypeAlias = list[
    "capo_codepipeline.types.webhook_filter_rule.WebhookFilterRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookFilters) -> list:
    import capo_codepipeline.types.webhook_filter_rule

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.webhook_filter_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WebhookFilters:
    import capo_codepipeline.types.webhook_filter_rule

    out: WebhookFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.webhook_filter_rule.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookFilters) -> list:
    import capo_codepipeline.types.webhook_filter_rule

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.webhook_filter_rule.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WebhookFilters:
    import capo_codepipeline.types.webhook_filter_rule

    out: WebhookFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.webhook_filter_rule.deserialize_cbor(item))
    return out
