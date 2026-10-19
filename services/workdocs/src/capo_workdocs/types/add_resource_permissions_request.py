"""Generated from Smithy shape ``com.amazonaws.workdocs#AddResourcePermissionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.notification_options
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.share_principal_list


class AddResourcePermissionsRequest(TypedDict, closed=True):
    authentication_token: NotRequired[
        "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""
    resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType"
    """<p>The ID of the resource.</p>"""
    principals: "capo_workdocs.types.share_principal_list.SharePrincipalList"
    """<p>The users, groups, or organization being granted permission.</p>"""
    notification_options: NotRequired[
        "capo_workdocs.types.notification_options.NotificationOptions"
    ]
    """<p>The notification options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddResourcePermissionsRequest) -> dict:
    out: dict = {}
    import capo_workdocs.types.share_principal_list

    out["Principals"] = capo_workdocs.types.share_principal_list.serialize_json(
        value["principals"]
    )
    if "notification_options" in value:
        import capo_workdocs.types.notification_options

        out["NotificationOptions"] = (
            capo_workdocs.types.notification_options.serialize_json(
                value["notification_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddResourcePermissionsRequest:
    out: AddResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Principals") is not None:
        import capo_workdocs.types.share_principal_list

        out["principals"] = capo_workdocs.types.share_principal_list.deserialize_json(
            data["Principals"]
        )
    else:
        out["principals"] = []
    if data.get("NotificationOptions") is not None:
        import capo_workdocs.types.notification_options

        out["notification_options"] = (
            capo_workdocs.types.notification_options.deserialize_json(
                data["NotificationOptions"]
            )
        )
    return out


def redact_sensitive(value: AddResourcePermissionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_token" in value:
        out["authentication_token"] = "*** Sensitive Data Redacted ***"
    if "notification_options" in value:
        import capo_workdocs.types.notification_options

        out["notification_options"] = (
            capo_workdocs.types.notification_options.redact_sensitive(
                value["notification_options"]
            )
        )
    return out
