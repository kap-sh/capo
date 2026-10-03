"""Generated from Smithy shape ``com.amazonaws.glue#TableStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.error_detail
    import capo_glue.types.name_string
    import capo_glue.types.resource_action
    import capo_glue.types.resource_state
    import capo_glue.types.status_details
    import capo_glue.types.timestamp


class TableStatus(TypedDict, closed=True):
    requested_by: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The ARN of the user who requested the asynchronous change.</p>"""
    updated_by: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The ARN of the user to last manually alter the asynchronous change (requesting cancellation, etc).</p>"""
    request_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>An ISO 8601 formatted date string indicating the time that the change was initiated.</p>"""
    update_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>An ISO 8601 formatted date string indicating the time that the state was last updated.</p>"""
    action: NotRequired["capo_glue.types.resource_action.ResourceAction"]
    """<p>Indicates which action was called on the table, currently only <code>CREATE</code> or <code>UPDATE</code>.</p>"""
    state: NotRequired["capo_glue.types.resource_state.ResourceState"]
    """<p>A generic status for the change in progress, such as QUEUED, IN_PROGRESS, SUCCESS, or FAILED.</p>"""
    error: NotRequired["capo_glue.types.error_detail.ErrorDetail"]
    """<p>An error that will only appear when the state is "FAILED". This is a parent level exception message, there may be different <code>Error</code>s for each dialect.</p>"""
    details: NotRequired["capo_glue.types.status_details.StatusDetails"]
    """<p>A <code>StatusDetails</code> object with information about the requested change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableStatus) -> dict:
    out: dict = {}
    if "requested_by" in value:
        out["RequestedBy"] = value["requested_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    if "request_time" in value:
        import capo_glue.types.timestamp

        out["RequestTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["request_time"]
        )
    if "update_time" in value:
        import capo_glue.types.timestamp

        out["UpdateTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    if "action" in value:
        import capo_glue.types.resource_action

        out["Action"] = capo_glue.types.resource_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "state" in value:
        import capo_glue.types.resource_state

        out["State"] = capo_glue.types.resource_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "error" in value:
        import capo_glue.types.error_detail

        out["Error"] = capo_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    if "details" in value:
        import capo_glue.types.status_details

        out["Details"] = capo_glue.types.status_details.serialize_aws_json_1_1(
            value["details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableStatus:
    out: TableStatus = {}  # type: ignore[typeddict-item]
    if data.get("RequestedBy") is not None:
        out["requested_by"] = data["RequestedBy"]
    if data.get("UpdatedBy") is not None:
        out["updated_by"] = data["UpdatedBy"]
    if data.get("RequestTime") is not None:
        import capo_glue.types.timestamp

        out["request_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RequestTime"]
        )
    if data.get("UpdateTime") is not None:
        import capo_glue.types.timestamp

        out["update_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    if data.get("Action") is not None:
        import capo_glue.types.resource_action

        out["action"] = capo_glue.types.resource_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("State") is not None:
        import capo_glue.types.resource_state

        out["state"] = capo_glue.types.resource_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Error") is not None:
        import capo_glue.types.error_detail

        out["error"] = capo_glue.types.error_detail.deserialize_aws_json_1_1(
            data["Error"]
        )
    if data.get("Details") is not None:
        import capo_glue.types.status_details

        out["details"] = capo_glue.types.status_details.deserialize_aws_json_1_1(
            data["Details"]
        )
    return out
