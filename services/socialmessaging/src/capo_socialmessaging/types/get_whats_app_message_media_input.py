"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppMessageMediaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.s3_file
    import capo_socialmessaging.types.s3_presigned_url
    import capo_socialmessaging.types.whats_app_media_id
    import capo_socialmessaging.types.whats_app_phone_number_id


class GetWhatsAppMessageMediaInput(TypedDict, closed=True):
    media_id: "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId"
    """<p>The unique identifier for the media file.</p>"""
    origination_phone_number_id: (
        "capo_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    """<p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href="https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""
    metadata_only: NotRequired["bool"]
    """<p>Set to <code>True</code> to get only the metadata for the file.</p>"""
    destination_s3_presigned_url: NotRequired[
        "capo_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
    ]
    """<p>The presign url of the media file.</p>"""
    destination_s3_file: NotRequired["capo_socialmessaging.types.s3_file.S3File"]
    """<p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppMessageMediaInput) -> dict:
    out: dict = {}
    out["mediaId"] = value["media_id"]
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    if "metadata_only" in value:
        out["metadataOnly"] = value["metadata_only"]
    if "destination_s3_presigned_url" in value:
        import capo_socialmessaging.types.s3_presigned_url

        out["destinationS3PresignedUrl"] = (
            capo_socialmessaging.types.s3_presigned_url.serialize_json(
                value["destination_s3_presigned_url"]
            )
        )
    if "destination_s3_file" in value:
        import capo_socialmessaging.types.s3_file

        out["destinationS3File"] = capo_socialmessaging.types.s3_file.serialize_json(
            value["destination_s3_file"]
        )
    return out


def deserialize_json(data: dict) -> GetWhatsAppMessageMediaInput:
    out: GetWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
    if data.get("mediaId") is not None:
        out["media_id"] = data["mediaId"]
    else:
        raise DeserializationError("GetWhatsAppMessageMediaInput.media_id required")
    if data.get("originationPhoneNumberId") is not None:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "GetWhatsAppMessageMediaInput.origination_phone_number_id required"
        )
    if data.get("metadataOnly") is not None:
        out["metadata_only"] = data["metadataOnly"]
    if data.get("destinationS3PresignedUrl") is not None:
        import capo_socialmessaging.types.s3_presigned_url

        out["destination_s3_presigned_url"] = (
            capo_socialmessaging.types.s3_presigned_url.deserialize_json(
                data["destinationS3PresignedUrl"]
            )
        )
    if data.get("destinationS3File") is not None:
        import capo_socialmessaging.types.s3_file

        out["destination_s3_file"] = (
            capo_socialmessaging.types.s3_file.deserialize_json(
                data["destinationS3File"]
            )
        )
    return out
