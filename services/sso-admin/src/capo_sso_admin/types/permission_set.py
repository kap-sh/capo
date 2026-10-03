"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PermissionSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.date
    import capo_sso_admin.types.duration
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.permission_set_description
    import capo_sso_admin.types.permission_set_name
    import capo_sso_admin.types.relay_state


class PermissionSet(TypedDict, closed=True):
    name: NotRequired["capo_sso_admin.types.permission_set_name.PermissionSetName"]
    """<p>The name of the permission set.</p>"""
    permission_set_arn: NotRequired[
        "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    ]
    """<p>The ARN of the permission set. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    description: NotRequired[
        "capo_sso_admin.types.permission_set_description.PermissionSetDescription"
    ]
    """<p>The description of the <a>PermissionSet</a>.</p>"""
    created_date: NotRequired["capo_sso_admin.types.date.Date"]
    """<p>The date that the permission set was created.</p>"""
    session_duration: NotRequired["capo_sso_admin.types.duration.Duration"]
    """<p>The length of time that the application user sessions are valid for in the ISO-8601 standard.</p>"""
    relay_state: NotRequired["capo_sso_admin.types.relay_state.RelayState"]
    """<p>Used to redirect users within the application during the federation authentication process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionSet) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "permission_set_arn" in value:
        out["PermissionSetArn"] = value["permission_set_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_date" in value:
        import capo_sso_admin.types.date

        out["CreatedDate"] = capo_sso_admin.types.date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "session_duration" in value:
        out["SessionDuration"] = value["session_duration"]
    if "relay_state" in value:
        out["RelayState"] = value["relay_state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PermissionSet:
    out: PermissionSet = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedDate") is not None:
        import capo_sso_admin.types.date

        out["created_date"] = capo_sso_admin.types.date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("SessionDuration") is not None:
        out["session_duration"] = data["SessionDuration"]
    if data.get("RelayState") is not None:
        out["relay_state"] = data["RelayState"]
    return out
