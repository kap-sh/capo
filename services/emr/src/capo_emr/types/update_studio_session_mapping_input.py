"""Generated from Smithy shape ``com.amazonaws.emr#UpdateStudioSessionMappingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.identity_type
    import capo_emr.types.xml_string_max_len256


class UpdateStudioSessionMappingInput(TypedDict, closed=True):
    studio_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    identity_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The globally unique identifier (GUID) of the user or group. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserId">UserId</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-GroupId">GroupId</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>"""
    identity_name: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The name of the user or group to update. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>. Either <code>IdentityName</code> or <code>IdentityId</code> must be specified.</p>"""
    identity_type: NotRequired["capo_emr.types.identity_type.IdentityType"]
    """<p>Specifies whether the identity to update is a user or a group.</p>"""
    session_policy_arn: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon Resource Name (ARN) of the session policy to associate with the specified user or group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStudioSessionMappingInput) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "identity_name" in value:
        out["IdentityName"] = value["identity_name"]
    if "identity_type" in value:
        import capo_emr.types.identity_type

        out["IdentityType"] = capo_emr.types.identity_type.serialize_aws_json_1_1(
            value["identity_type"]
        )
    if "session_policy_arn" in value:
        out["SessionPolicyArn"] = value["session_policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStudioSessionMappingInput:
    out: UpdateStudioSessionMappingInput = {}  # type: ignore[typeddict-item]
    if data.get("StudioId") is not None:
        out["studio_id"] = data["StudioId"]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    if data.get("IdentityName") is not None:
        out["identity_name"] = data["IdentityName"]
    if data.get("IdentityType") is not None:
        import capo_emr.types.identity_type

        out["identity_type"] = capo_emr.types.identity_type.deserialize_aws_json_1_1(
            data["IdentityType"]
        )
    if data.get("SessionPolicyArn") is not None:
        out["session_policy_arn"] = data["SessionPolicyArn"]
    return out
