"""Generated from Smithy shape ``com.amazonaws.codepipeline#WebhookList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.list_webhook_item

WebhookList: TypeAlias = list[
    "capo_codepipeline.types.list_webhook_item.ListWebhookItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookList) -> list:
    import capo_codepipeline.types.list_webhook_item

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.list_webhook_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WebhookList:
    import capo_codepipeline.types.list_webhook_item

    out: WebhookList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.list_webhook_item.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookList) -> list:
    import capo_codepipeline.types.list_webhook_item

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.list_webhook_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> WebhookList:
    import capo_codepipeline.types.list_webhook_item

    out: WebhookList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.list_webhook_item.deserialize_cbor(item))
    return out
