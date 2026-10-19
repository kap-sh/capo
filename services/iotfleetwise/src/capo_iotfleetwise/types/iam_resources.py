"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#IamResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.iam_role_arn


class IamResources(TypedDict, closed=True):
    role_arn: "capo_iotfleetwise.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream. For example, <code>arn:aws:iam::123456789012:role/SERVICE-ROLE-ARN</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamResources) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamResources:
    out: IamResources = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
