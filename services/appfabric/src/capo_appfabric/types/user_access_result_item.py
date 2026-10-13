"""Generated from Smithy shape ``com.amazonaws.appfabric#UserAccessResultItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.email
    import capo_appfabric.types.result_status
    import capo_appfabric.types.sensitive_string2048
    import capo_appfabric.types.string255
    import capo_appfabric.types.string2048
    import capo_appfabric.types.task_error
    import capo_appfabric.types.tenant_identifier
    import capo_appfabric.types.uuid


class UserAccessResultItem(TypedDict, closed=True):
    app: NotRequired["capo_appfabric.types.string255.String255"]
    """<p>The name of the application.</p>"""
    tenant_id: NotRequired["capo_appfabric.types.tenant_identifier.TenantIdentifier"]
    """<p>The ID of the application tenant.</p>"""
    tenant_display_name: NotRequired["capo_appfabric.types.string2048.String2048"]
    """<p>The display name of the tenant.</p>"""
    task_id: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>The unique ID of the task.</p>"""
    result_status: NotRequired["capo_appfabric.types.result_status.ResultStatus"]
    """<p>The status of the user access result item.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>IN_PROGRESS</code>: The user access task is in progress.</p> </li> <li> <p> <code>COMPLETED</code>: The user access task completed successfully.</p> </li> <li> <p> <code>FAILED</code>: The user access task failed.</p> </li> <li> <p> <code>EXPIRED</code>: The user access task expired.</p> </li> </ul>"""
    email: NotRequired["capo_appfabric.types.email.Email"]
    """<p>The email address of the target user.</p>"""
    user_id: NotRequired[
        "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    ]
    """<p>The unique ID of user.</p>"""
    user_full_name: NotRequired[
        "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    ]
    """<p>The full name of the user.</p>"""
    user_first_name: NotRequired[
        "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    ]
    """<p>The first name of the user.</p>"""
    user_last_name: NotRequired[
        "capo_appfabric.types.sensitive_string2048.SensitiveString2048"
    ]
    """<p>The last name of the user.</p>"""
    user_status: NotRequired["str"]
    """<p>The status of the user returned by the application.</p>"""
    task_error: NotRequired["capo_appfabric.types.task_error.TaskError"]
    """<p>Contains information about an error returned from a user access task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessResultItem) -> dict:
    out: dict = {}
    if "app" in value:
        out["app"] = value["app"]
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    if "tenant_display_name" in value:
        out["tenantDisplayName"] = value["tenant_display_name"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "result_status" in value:
        import capo_appfabric.types.result_status

        out["resultStatus"] = capo_appfabric.types.result_status.serialize_json(
            value["result_status"]
        )
    if "email" in value:
        out["email"] = value["email"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "user_full_name" in value:
        out["userFullName"] = value["user_full_name"]
    if "user_first_name" in value:
        out["userFirstName"] = value["user_first_name"]
    if "user_last_name" in value:
        out["userLastName"] = value["user_last_name"]
    if "user_status" in value:
        out["userStatus"] = value["user_status"]
    if "task_error" in value:
        import capo_appfabric.types.task_error

        out["taskError"] = capo_appfabric.types.task_error.serialize_json(
            value["task_error"]
        )
    return out


def deserialize_json(data: dict) -> UserAccessResultItem:
    out: UserAccessResultItem = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        out["app"] = data["app"]
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    if data.get("tenantDisplayName") is not None:
        out["tenant_display_name"] = data["tenantDisplayName"]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("resultStatus") is not None:
        import capo_appfabric.types.result_status

        out["result_status"] = capo_appfabric.types.result_status.deserialize_json(
            data["resultStatus"]
        )
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("userFullName") is not None:
        out["user_full_name"] = data["userFullName"]
    if data.get("userFirstName") is not None:
        out["user_first_name"] = data["userFirstName"]
    if data.get("userLastName") is not None:
        out["user_last_name"] = data["userLastName"]
    if data.get("userStatus") is not None:
        out["user_status"] = data["userStatus"]
    if data.get("taskError") is not None:
        import capo_appfabric.types.task_error

        out["task_error"] = capo_appfabric.types.task_error.deserialize_json(
            data["taskError"]
        )
    return out


def redact_sensitive(value: UserAccessResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "user_id" in value:
        out["user_id"] = "*** Sensitive Data Redacted ***"
    if "user_full_name" in value:
        out["user_full_name"] = "*** Sensitive Data Redacted ***"
    if "user_first_name" in value:
        out["user_first_name"] = "*** Sensitive Data Redacted ***"
    if "user_last_name" in value:
        out["user_last_name"] = "*** Sensitive Data Redacted ***"
    return out
