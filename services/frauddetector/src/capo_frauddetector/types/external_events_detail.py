"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalEventsDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.iam_role_arn
    import capo_frauddetector.types.s3_bucket_location


class ExternalEventsDetail(TypedDict, closed=True):
    data_location: "capo_frauddetector.types.s3_bucket_location.s3BucketLocation"
    """<p>The Amazon S3 bucket location for the data.</p>"""
    data_access_role_arn: "capo_frauddetector.types.iam_role_arn.iamRoleArn"
    """<p>The ARN of the role that provides Amazon Fraud Detector access to the data location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalEventsDetail) -> dict:
    out: dict = {}
    out["dataLocation"] = value["data_location"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalEventsDetail:
    out: ExternalEventsDetail = {}  # type: ignore[typeddict-item]
    if data.get("dataLocation") is not None:
        out["data_location"] = data["dataLocation"]
    else:
        out["data_location"] = ""
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        out["data_access_role_arn"] = ""
    return out
