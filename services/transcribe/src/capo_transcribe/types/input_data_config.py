"""Generated from Smithy shape ``com.amazonaws.transcribe#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.uri


class InputDataConfig(TypedDict, closed=True):
    s3_uri: "capo_transcribe.types.uri.Uri"
    """<p>The Amazon S3 location (URI) of the text files you want to use to train your custom language model.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-model-training-data/</code> </p>"""
    tuning_data_s3_uri: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location (URI) of the text files you want to use to tune your custom language model.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-model-tuning-data/</code> </p>"""
    data_access_role_arn: "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "tuning_data_s3_uri" in value:
        out["TuningDataS3Uri"] = value["tuning_data_s3_uri"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        raise DeserializationError("InputDataConfig.s3_uri required")
    if data.get("TuningDataS3Uri") is not None:
        out["tuning_data_s3_uri"] = data["TuningDataS3Uri"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError("InputDataConfig.data_access_role_arn required")
    return out
