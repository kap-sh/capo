"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.error_message
    import capo_partnercentral_marketing.types.validation_exception_field_list
    import capo_partnercentral_marketing.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    reason: NotRequired[
        "capo_partnercentral_marketing.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """The single coarse reason the request was rejected, for a caller that does not care which field."""
    field_list: NotRequired[
        "capo_partnercentral_marketing.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """Every field that failed, not just the first. <p>⚠️ **Every field, deliberately.** The convention comment carried by most internal models — *"if more than one field caused the error, pick one and elaborate in the message"* — is the reading this service does NOT take: a partner editing a form would then discover their errors one request at a time. The whole request is validated and the full set reported, so one round of fixes is one call. <p><strong>Each entry names a member of the request just sent</strong>, and only that: the value to change and send again. A template field value is `Name` `FieldValues` with the template field in `FieldId`, one entry per failing field. <p><strong>When it is present.</strong> Only when the refusal points at something the partner fixes in a form, and then every such refusal carries it: - `UpdateCampaignAsset`: `FieldValues` (including a file the content scan declined, which is why a partner handles image failures and text failures the same way, through this list), `Layout`, `SendMode` and `ScheduledSendAt`; - `CreateCampaign` and `UpdateCampaign`: campaign settings and files; - `GetCampaignTemplate`: `Identifier`. <p>Every other `ValidationException` carries `Message` only — tags, ARNs, social connections, exports, and `CAMPAIGN_INCOMPLETE`, whose missing settings are not members of the request it refuses."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_partnercentral_marketing.types.validation_exception_reason

        out["Reason"] = (
            capo_partnercentral_marketing.types.validation_exception_reason.serialize_cbor(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_partnercentral_marketing.types.validation_exception_field_list

        out["FieldList"] = (
            capo_partnercentral_marketing.types.validation_exception_field_list.serialize_cbor(
                value["field_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_marketing.types.validation_exception_reason

        out["reason"] = (
            capo_partnercentral_marketing.types.validation_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    if data.get("FieldList") is not None:
        import capo_partnercentral_marketing.types.validation_exception_field_list

        out["field_list"] = (
            capo_partnercentral_marketing.types.validation_exception_field_list.deserialize_cbor(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_cbor(data), message, response=response)
