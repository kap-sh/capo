"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUsersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user_list
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.next_token


class ListAppInstanceUsersResponse(TypedDict, closed=True):
    app_instance_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    app_instance_users: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_user_list.AppInstanceUserList"
    ]
    """<p>The information for each requested <code>AppInstanceUser</code>.</p>"""
    next_token: NotRequired["capo_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUsersResponse) -> dict:
    out: dict = {}
    if "app_instance_arn" in value:
        out["AppInstanceArn"] = value["app_instance_arn"]
    if "app_instance_users" in value:
        import capo_chime_sdk_identity.types.app_instance_user_list

        out["AppInstanceUsers"] = (
            capo_chime_sdk_identity.types.app_instance_user_list.serialize_json(
                value["app_instance_users"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceUsersResponse:
    out: ListAppInstanceUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    if data.get("AppInstanceUsers") is not None:
        import capo_chime_sdk_identity.types.app_instance_user_list

        out["app_instance_users"] = (
            capo_chime_sdk_identity.types.app_instance_user_list.deserialize_json(
                data["AppInstanceUsers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAppInstanceUsersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_users" in value:
        import capo_chime_sdk_identity.types.app_instance_user_list

        out["app_instance_users"] = (
            capo_chime_sdk_identity.types.app_instance_user_list.redact_sensitive(
                value["app_instance_users"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
