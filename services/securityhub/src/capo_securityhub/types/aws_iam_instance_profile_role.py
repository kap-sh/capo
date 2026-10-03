"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamInstanceProfileRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_role_assume_role_policy_document
    import capo_securityhub.types.non_empty_string


class AwsIamInstanceProfileRole(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the role.</p>"""
    assume_role_policy_document: NotRequired[
        "capo_securityhub.types.aws_iam_role_assume_role_policy_document.AwsIamRoleAssumeRolePolicyDocument"
    ]
    """<p>The policy that grants an entity permission to assume the role.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the role was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the role.</p>"""
    role_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the role.</p>"""
    role_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamInstanceProfileRole) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "assume_role_policy_document" in value:
        out["AssumeRolePolicyDocument"] = value["assume_role_policy_document"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "path" in value:
        out["Path"] = value["path"]
    if "role_id" in value:
        out["RoleId"] = value["role_id"]
    if "role_name" in value:
        out["RoleName"] = value["role_name"]
    return out


def deserialize_json(data: dict) -> AwsIamInstanceProfileRole:
    out: AwsIamInstanceProfileRole = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AssumeRolePolicyDocument") is not None:
        out["assume_role_policy_document"] = data["AssumeRolePolicyDocument"]
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("RoleId") is not None:
        out["role_id"] = data["RoleId"]
    if data.get("RoleName") is not None:
        out["role_name"] = data["RoleName"]
    return out
