"""Generated from Smithy shape ``com.amazonaws.emr#SessionMappingDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.identity_type
    import capo_emr.types.xml_string_max_len256


class SessionMappingDetail(TypedDict, closed=True):
    studio_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    identity_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The globally unique identifier (GUID) of the user or group.</p>"""
    identity_name: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The name of the user or group. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName">UserName</a> and <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>.</p>"""
    identity_type: NotRequired["capo_emr.types.identity_type.IdentityType"]
    """<p>Specifies whether the identity mapped to the Amazon EMR Studio is a user or a group.</p>"""
    session_policy_arn: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon Resource Name (ARN) of the session policy associated with the user or group.</p>"""
    creation_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The time the session mapping was created.</p>"""
    last_modified_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The time the session mapping was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionMappingDetail) -> dict:
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
    if "creation_time" in value:
        import capo_emr.types.date

        out["CreationTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_emr.types.date

        out["LastModifiedTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionMappingDetail:
    out: SessionMappingDetail = {}  # type: ignore[typeddict-item]
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
    if data.get("CreationTime") is not None:
        import capo_emr.types.date

        out["creation_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_emr.types.date

        out["last_modified_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    return out
