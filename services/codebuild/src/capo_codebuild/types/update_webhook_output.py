"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateWebhookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.webhook


class UpdateWebhookOutput(TypedDict, closed=True):
    webhook: NotRequired["capo_codebuild.types.webhook.Webhook"]
    """<p> Information about a repository's webhook that is associated with a project in CodeBuild. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.serialize_aws_json_1_1(
            value["webhook"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebhookOutput:
    out: UpdateWebhookOutput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.deserialize_aws_json_1_1(
            data["webhook"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateWebhookOutput) -> dict:
    out: dict = {}
    if "webhook" in value:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.serialize_cbor(value["webhook"])
    return out


def deserialize_cbor(data: dict) -> UpdateWebhookOutput:
    out: UpdateWebhookOutput = {}  # type: ignore[typeddict-item]
    if data.get("webhook") is not None:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.deserialize_cbor(data["webhook"])
    return out
