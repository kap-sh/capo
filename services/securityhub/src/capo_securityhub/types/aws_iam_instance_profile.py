"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamInstanceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_instance_profile_roles
    import capo_securityhub.types.non_empty_string


class AwsIamInstanceProfile(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the instance profile.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the instance profile was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    instance_profile_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the instance profile.</p>"""
    instance_profile_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the instance profile.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the instance profile.</p>"""
    roles: NotRequired[
        "capo_securityhub.types.aws_iam_instance_profile_roles.AwsIamInstanceProfileRoles"
    ]
    """<p>The roles associated with the instance profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamInstanceProfile) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "instance_profile_id" in value:
        out["InstanceProfileId"] = value["instance_profile_id"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "roles" in value:
        import capo_securityhub.types.aws_iam_instance_profile_roles

        out["Roles"] = (
            capo_securityhub.types.aws_iam_instance_profile_roles.serialize_json(
                value["roles"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamInstanceProfile:
    out: AwsIamInstanceProfile = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("InstanceProfileId") is not None:
        out["instance_profile_id"] = data["InstanceProfileId"]
    if data.get("InstanceProfileName") is not None:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Roles") is not None:
        import capo_securityhub.types.aws_iam_instance_profile_roles

        out["roles"] = (
            capo_securityhub.types.aws_iam_instance_profile_roles.deserialize_json(
                data["Roles"]
            )
        )
    return out
