"""Generated from Smithy shape ``com.amazonaws.gamelift#RequestUploadCredentialsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.aws_credentials
    import capo_gamelift.types.s3_location


class RequestUploadCredentialsOutput(TypedDict, closed=True):
    upload_credentials: NotRequired[
        "capo_gamelift.types.aws_credentials.AwsCredentials"
    ]
    """<p>Amazon Web Services credentials required when uploading a game build to the storage location. These credentials have a limited lifespan and are valid only for the build they were issued for.</p>"""
    storage_location: NotRequired["capo_gamelift.types.s3_location.S3Location"]
    """<p>Amazon S3 path and key, identifying where the game build files are stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestUploadCredentialsOutput) -> dict:
    out: dict = {}
    if "upload_credentials" in value:
        import capo_gamelift.types.aws_credentials

        out["UploadCredentials"] = (
            capo_gamelift.types.aws_credentials.serialize_aws_json_1_1(
                value["upload_credentials"]
            )
        )
    if "storage_location" in value:
        import capo_gamelift.types.s3_location

        out["StorageLocation"] = capo_gamelift.types.s3_location.serialize_aws_json_1_1(
            value["storage_location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestUploadCredentialsOutput:
    out: RequestUploadCredentialsOutput = {}  # type: ignore[typeddict-item]
    if data.get("UploadCredentials") is not None:
        import capo_gamelift.types.aws_credentials

        out["upload_credentials"] = (
            capo_gamelift.types.aws_credentials.deserialize_aws_json_1_1(
                data["UploadCredentials"]
            )
        )
    if data.get("StorageLocation") is not None:
        import capo_gamelift.types.s3_location

        out["storage_location"] = (
            capo_gamelift.types.s3_location.deserialize_aws_json_1_1(
                data["StorageLocation"]
            )
        )
    return out


def redact_sensitive(value: RequestUploadCredentialsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "upload_credentials" in value:
        out["upload_credentials"] = "*** Sensitive Data Redacted ***"
    return out
