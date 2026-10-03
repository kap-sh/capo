"""Generated from Smithy shape ``com.amazonaws.shield#AssociateDRTRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.role_arn


class AssociateDRTRoleRequest(TypedDict, closed=True):
    role_arn: "capo_shield.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the role the SRT will use to access your Amazon Web Services account.</p> <p>Prior to making the <code>AssociateDRTRole</code> request, you must attach the <a href="https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy">AWSShieldDRTAccessPolicy</a> managed policy to this role. For more information see <a href=" https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html">Attaching and Detaching IAM Policies</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateDRTRoleRequest) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateDRTRoleRequest:
    out: AssociateDRTRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("AssociateDRTRoleRequest.role_arn required")
    return out
