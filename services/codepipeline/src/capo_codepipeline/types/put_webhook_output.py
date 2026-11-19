"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutWebhookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.list_webhook_item


class PutWebhookOutput(TypedDict, closed=True):
    webhook: NotRequired["capo_codepipeline.types.list_webhook_item.ListWebhookItem"]
    """<p>The detail returned from creating the webhook, such as the webhook name, webhook URL, and webhook ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import capo_codepipeline.types.list_webhook_item

        out["webhook"] = (
            capo_codepipeline.types.list_webhook_item.serialize_aws_json_1_1(
                value["webhook"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutWebhookOutput:
    out: PutWebhookOutput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codepipeline.types.list_webhook_item

        out["webhook"] = (
            capo_codepipeline.types.list_webhook_item.deserialize_aws_json_1_1(
                data["webhook"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import capo_codepipeline.types.list_webhook_item

        out["webhook"] = capo_codepipeline.types.list_webhook_item.serialize_cbor(
            value["webhook"]
        )
    return out


def deserialize_cbor(data: dict) -> PutWebhookOutput:
    out: PutWebhookOutput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codepipeline.types.list_webhook_item

        out["webhook"] = capo_codepipeline.types.list_webhook_item.deserialize_cbor(
            data["webhook"]
        )
    return out
