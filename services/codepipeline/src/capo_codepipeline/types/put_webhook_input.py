"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutWebhookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.tag_list
    import capo_codepipeline.types.webhook_definition


class PutWebhookInput(TypedDict, closed=True):
    webhook: "capo_codepipeline.types.webhook_definition.WebhookDefinition"
    """<p>The detail provided in an input file to create the webhook, such as the webhook name, the pipeline name, and the action name. Give the webhook a unique name that helps you identify it. You might name the webhook after the pipeline and action it targets so that you can easily recognize what it's used for later.</p>"""
    tags: NotRequired["capo_codepipeline.types.tag_list.TagList"]
    """<p>The tags for the webhook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutWebhookInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.webhook_definition

    out["webhook"] = capo_codepipeline.types.webhook_definition.serialize_aws_json_1_1(
        value["webhook"]
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutWebhookInput:
    out: PutWebhookInput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codepipeline.types.webhook_definition

        out["webhook"] = (
            capo_codepipeline.types.webhook_definition.deserialize_aws_json_1_1(
                data["webhook"]
            )
        )
    else:
        raise DeserializationError("PutWebhookInput.webhook required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutWebhookInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.webhook_definition

    out["webhook"] = capo_codepipeline.types.webhook_definition.serialize_cbor(
        value["webhook"]
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> PutWebhookInput:
    out: PutWebhookInput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codepipeline.types.webhook_definition

        out["webhook"] = capo_codepipeline.types.webhook_definition.deserialize_cbor(
            data["webhook"]
        )
    else:
        raise DeserializationError("PutWebhookInput.webhook required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_cbor(data["tags"])
    return out
