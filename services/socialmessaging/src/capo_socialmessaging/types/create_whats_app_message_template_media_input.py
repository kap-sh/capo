"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateMediaInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.s3_file


class CreateWhatsAppMessageTemplateMediaInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this media upload.</p>"""
    source_s3_file: NotRequired["capo_socialmessaging.types.s3_file.S3File"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateMediaInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "source_s3_file" in value:
        import capo_socialmessaging.types.s3_file

        out["sourceS3File"] = capo_socialmessaging.types.s3_file.serialize_json(
            value["source_s3_file"]
        )
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateMediaInput:
    out: CreateWhatsAppMessageTemplateMediaInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "CreateWhatsAppMessageTemplateMediaInput.id required"
        )
    if data.get("sourceS3File") is not None:
        import capo_socialmessaging.types.s3_file

        out["source_s3_file"] = capo_socialmessaging.types.s3_file.deserialize_json(
            data["sourceS3File"]
        )
    return out


def redact_sensitive(value: CreateWhatsAppMessageTemplateMediaInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_s3_file" in value:
        out["source_s3_file"] = "*** Sensitive Data Redacted ***"
    return out
