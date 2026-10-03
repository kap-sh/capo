"""Generated from Smithy shape ``com.amazonaws.socialmessaging#PostWhatsAppMessageMediaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.s3_file
    import capo_socialmessaging.types.s3_presigned_url
    import capo_socialmessaging.types.whats_app_phone_number_id


class PostWhatsAppMessageMediaInput(TypedDict, closed=True):
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The ID of the phone number to associate with the WhatsApp media file. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""
    source_s3_presigned_url: NotRequired[
        "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
    ]
    """<p>The source presign url of the media file.</p>"""
    source_s3_file: NotRequired["capo_socialmessaging.types.s3_file.S3File"]
    """<p>The source S3 url for the media file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostWhatsAppMessageMediaInput) -> dict:
    out: dict = {}
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    if "source_s3_presigned_url" in value:
        import capo_socialmessaging.types.s3_presigned_url

        out["sourceS3PresignedUrl"] = (
            capo_socialmessaging.types.s3_presigned_url.serialize_json(
                value["source_s3_presigned_url"]
            )
        )
    if "source_s3_file" in value:
        import capo_socialmessaging.types.s3_file

        out["sourceS3File"] = capo_socialmessaging.types.s3_file.serialize_json(
            value["source_s3_file"]
        )
    return out


def deserialize_json(data: dict) -> PostWhatsAppMessageMediaInput:
    out: PostWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "PostWhatsAppMessageMediaInput.origination_phone_number_id required"
        )
    if data.get("sourceS3PresignedUrl") is not None:
        import capo_socialmessaging.types.s3_presigned_url

        out["source_s3_presigned_url"] = (
            capo_socialmessaging.types.s3_presigned_url.deserialize_json(
                data["sourceS3PresignedUrl"]
            )
        )
    if data.get("sourceS3File") is not None:
        import capo_socialmessaging.types.s3_file

        out["source_s3_file"] = capo_socialmessaging.types.s3_file.deserialize_json(
            data["sourceS3File"]
        )
    return out
