"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeleteWebhookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.webhook_name


class DeleteWebhookInput(TypedDict, closed=True):
    name: "capo_codepipeline.types.webhook_name.WebhookName"
    """<p>The name of the webhook you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebhookInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebhookInput:
    out: DeleteWebhookInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
