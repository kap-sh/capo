"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceAdminsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_admin_list
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.next_token


class ListAppInstanceAdminsResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    app_instance_admins: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_admin_list.AppInstanceAdminList"
    ]
    """<p>The information for each administrator.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of administrators is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceAdminsResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_admins" in value:
        import capo_chime_sdk_identity.types.app_instance_admin_list

        out["AppInstanceAdmins"] = (
            capo_chime_sdk_identity.types.app_instance_admin_list.serialize_json(
                value["app_instance_admins"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceAdminsResponse:
    out: ListAppInstanceAdminsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if data.get("AppInstanceAdmins") is not None:
        import capo_chime_sdk_identity.types.app_instance_admin_list

        out["app_instance_admins"] = (
            capo_chime_sdk_identity.types.app_instance_admin_list.deserialize_json(
                data["AppInstanceAdmins"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAppInstanceAdminsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_admins" in value:
        import capo_chime_sdk_identity.types.app_instance_admin_list

        out["app_instance_admins"] = (
            capo_chime_sdk_identity.types.app_instance_admin_list.redact_sensitive(
                value["app_instance_admins"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
