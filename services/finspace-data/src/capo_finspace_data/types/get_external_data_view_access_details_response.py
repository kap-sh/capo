"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetExternalDataViewAccessDetailsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.aws_credentials
    import capo_finspace_data.types.s3_location


class GetExternalDataViewAccessDetailsResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_finspace_data.types.aws_credentials.AwsCredentials"]
    """<p>The credentials required to access the external Dataview from the S3 location.</p>"""
    s3_location: NotRequired["capo_finspace_data.types.s3_location.S3Location"]
    """<p>The location where the external Dataview is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExternalDataViewAccessDetailsResponse) -> dict:
    out: dict = {}
    if "credentials" in value:
        import capo_finspace_data.types.aws_credentials

        out["credentials"] = capo_finspace_data.types.aws_credentials.serialize_json(
            value["credentials"]
        )
    if "s3_location" in value:
        import capo_finspace_data.types.s3_location

        out["s3Location"] = capo_finspace_data.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> GetExternalDataViewAccessDetailsResponse:
    out: GetExternalDataViewAccessDetailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentials") is not None:
        import capo_finspace_data.types.aws_credentials

        out["credentials"] = capo_finspace_data.types.aws_credentials.deserialize_json(
            data["credentials"]
        )
    if data.get("s3Location") is not None:
        import capo_finspace_data.types.s3_location

        out["s3_location"] = capo_finspace_data.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out


def redact_sensitive(value: GetExternalDataViewAccessDetailsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
