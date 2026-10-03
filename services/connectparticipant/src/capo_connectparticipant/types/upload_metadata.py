"""Generated from Smithy shape ``com.amazonaws.connectparticipant#UploadMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.iso8601_datetime
    import capo_connectparticipant.types.upload_metadata_signed_headers
    import capo_connectparticipant.types.upload_metadata_url


class UploadMetadata(TypedDict, closed=True):
    url: NotRequired[
        "capo_connectparticipant.types.upload_metadata_url.UploadMetadataUrl"
    ]
    """<p>This is the pre-signed URL that can be used for uploading the file to Amazon S3 when used in response to <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartAttachmentUpload.html">StartAttachmentUpload</a>.</p>"""
    url_expiry: NotRequired[
        "capo_connectparticipant.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""
    headers_to_include: NotRequired[
        "capo_connectparticipant.types.upload_metadata_signed_headers.UploadMetadataSignedHeaders"
    ]
    """<p>The headers to be provided while uploading the file to the URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadMetadata) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "url_expiry" in value:
        out["UrlExpiry"] = value["url_expiry"]
    if "headers_to_include" in value:
        import capo_connectparticipant.types.upload_metadata_signed_headers

        out["HeadersToInclude"] = (
            capo_connectparticipant.types.upload_metadata_signed_headers.serialize_json(
                value["headers_to_include"]
            )
        )
    return out


def deserialize_json(data: dict) -> UploadMetadata:
    out: UploadMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("UrlExpiry") is not None:
        out["url_expiry"] = data["UrlExpiry"]
    if data.get("HeadersToInclude") is not None:
        import capo_connectparticipant.types.upload_metadata_signed_headers

        out["headers_to_include"] = (
            capo_connectparticipant.types.upload_metadata_signed_headers.deserialize_json(
                data["HeadersToInclude"]
            )
        )
    return out
