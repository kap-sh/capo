"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateBuildOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.aws_credentials
    import capo_gamelift.types.build
    import capo_gamelift.types.s3_location


class CreateBuildOutput(TypedDict, closed=True):
    build: NotRequired["capo_gamelift.types.build.Build"]
    """<p>The newly created build resource, including a unique build ID and status. </p>"""
    upload_credentials: NotRequired[
        "capo_gamelift.types.aws_credentials.AwsCredentials"
    ]
    """<p>This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an Amazon S3 bucket that is owned by Amazon GameLift Servers. Credentials have a limited life span. To refresh these credentials, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html">RequestUploadCredentials</a>. </p>"""
    storage_location: NotRequired["capo_gamelift.types.s3_location.S3Location"]
    """<p>Amazon S3 location for your game build file, including bucket name and key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBuildOutput) -> dict:
    out: dict = {}
    if "build" in value:
        import capo_gamelift.types.build

        out["Build"] = capo_gamelift.types.build.serialize_aws_json_1_1(value["build"])
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


def deserialize_aws_json_1_1(data: dict) -> CreateBuildOutput:
    out: CreateBuildOutput = {}  # type: ignore[typeddict-item]
    if data.get("Build") is not None:
        import capo_gamelift.types.build

        out["build"] = capo_gamelift.types.build.deserialize_aws_json_1_1(data["Build"])
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
