"""Generated from Smithy shape ``com.amazonaws.qapps#CreatePresignedUrlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.presigned_url_fields
    import capo_qapps.types.q_apps_timestamp


class CreatePresignedUrlOutput(TypedDict, closed=True):
    file_id: "str"
    """<p>The unique identifier assigned to the file to be uploaded.</p>"""
    presigned_url: "str"
    """<p>The URL for a presigned S3 POST operation used to upload a file.</p>"""
    presigned_url_fields: "capo_qapps.types.presigned_url_fields.PresignedUrlFields"
    """<p>The form fields to include in the presigned S3 POST operation used to upload a file.</p>"""
    presigned_url_expiration: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time that the presigned URL will expire in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresignedUrlOutput) -> dict:
    out: dict = {}
    out["fileId"] = value["file_id"]
    out["presignedUrl"] = value["presigned_url"]
    import capo_qapps.types.presigned_url_fields

    out["presignedUrlFields"] = capo_qapps.types.presigned_url_fields.serialize_json(
        value["presigned_url_fields"]
    )
    import capo_qapps.types.q_apps_timestamp

    out["presignedUrlExpiration"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["presigned_url_expiration"]
    )
    return out


def deserialize_json(data: dict) -> CreatePresignedUrlOutput:
    out: CreatePresignedUrlOutput = {}  # type: ignore[typeddict-item]
    if data.get("fileId") is not None:
        out["file_id"] = data["fileId"]
    else:
        out["file_id"] = ""
    if data.get("presignedUrl") is not None:
        out["presigned_url"] = data["presignedUrl"]
    else:
        out["presigned_url"] = ""
    if data.get("presignedUrlFields") is not None:
        import capo_qapps.types.presigned_url_fields

        out["presigned_url_fields"] = (
            capo_qapps.types.presigned_url_fields.deserialize_json(
                data["presignedUrlFields"]
            )
        )
    else:
        out["presigned_url_fields"] = {}
    if data.get("presignedUrlExpiration") is not None:
        import capo_qapps.types.q_apps_timestamp

        out["presigned_url_expiration"] = (
            capo_qapps.types.q_apps_timestamp.deserialize_json(
                data["presignedUrlExpiration"]
            )
        )
    else:
        import datetime

        out["presigned_url_expiration"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
