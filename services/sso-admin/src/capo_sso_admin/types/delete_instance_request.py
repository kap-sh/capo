"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn


class DeleteInstanceRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInstanceRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInstanceRequest:
    out: DeleteInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    return out
