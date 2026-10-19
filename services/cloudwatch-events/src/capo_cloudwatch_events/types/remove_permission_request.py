"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RemovePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.boolean
    import capo_cloudwatch_events.types.non_partner_event_bus_name
    import capo_cloudwatch_events.types.statement_id


class RemovePermissionRequest(TypedDict, closed=True):
    statement_id: NotRequired["capo_cloudwatch_events.types.statement_id.StatementId"]
    """<p>The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.</p>"""
    remove_all_permissions: NotRequired["capo_cloudwatch_events.types.boolean.Boolean"]
    """<p>Specifies whether to remove all permissions.</p>"""
    event_bus_name: NotRequired[
        "capo_cloudwatch_events.types.non_partner_event_bus_name.NonPartnerEventBusName"
    ]
    """<p>The name of the event bus to revoke permissions for. If you omit this, the default event bus is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemovePermissionRequest) -> dict:
    out: dict = {}
    if "statement_id" in value:
        out["StatementId"] = value["statement_id"]
    if "remove_all_permissions" in value:
        out["RemoveAllPermissions"] = value["remove_all_permissions"]
    if "event_bus_name" in value:
        out["EventBusName"] = value["event_bus_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemovePermissionRequest:
    out: RemovePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatementId") is not None:
        out["statement_id"] = data["StatementId"]
    if data.get("RemoveAllPermissions") is not None:
        out["remove_all_permissions"] = data["RemoveAllPermissions"]
    if data.get("EventBusName") is not None:
        out["event_bus_name"] = data["EventBusName"]
    return out
