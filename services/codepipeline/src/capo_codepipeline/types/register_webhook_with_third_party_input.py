"""Generated from Smithy shape ``com.amazonaws.codepipeline#RegisterWebhookWithThirdPartyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.webhook_name


class RegisterWebhookWithThirdPartyInput(TypedDict, closed=True):
    webhook_name: NotRequired["capo_codepipeline.types.webhook_name.WebhookName"]
    """<p>The name of an existing webhook created with PutWebhook to register with a supported third party. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWebhookWithThirdPartyInput) -> dict:
    out: dict = {}
    if "webhook_name" in value:
        out["webhookName"] = value["webhook_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWebhookWithThirdPartyInput:
    out: RegisterWebhookWithThirdPartyInput = {}  # type: ignore[typeddict-item]
    if data.get("webhookName") is not None:
        out["webhook_name"] = data["webhookName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegisterWebhookWithThirdPartyInput) -> dict:
    out: dict = {}
    if "webhook_name" in value:
        out["webhookName"] = value["webhook_name"]
    return out


def deserialize_cbor(data: dict) -> RegisterWebhookWithThirdPartyInput:
    out: RegisterWebhookWithThirdPartyInput = {}  # type: ignore[typeddict-item]
    if data.get("webhookName") is not None:
        out["webhook_name"] = data["webhookName"]
    return out
