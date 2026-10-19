"""Generated from Smithy shape ``com.amazonaws.inspector#RegisterCrossAccountAccessRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn


class RegisterCrossAccountAccessRoleRequest(TypedDict, closed=True):
    role_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the IAM role that grants Amazon Inspector access to AWS Services needed to perform security assessments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterCrossAccountAccessRoleRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterCrossAccountAccessRoleRequest:
    out: RegisterCrossAccountAccessRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
