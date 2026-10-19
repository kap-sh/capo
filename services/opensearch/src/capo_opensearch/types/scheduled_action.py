"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduledAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.action_severity
    import capo_opensearch.types.action_status
    import capo_opensearch.types.action_type
    import capo_opensearch.types.boolean
    import capo_opensearch.types.long
    import capo_opensearch.types.scheduled_by
    import capo_opensearch.types.string


class ScheduledAction(TypedDict, closed=True):
    id: "capo_opensearch.types.string.String"
    """<p>The unique identifier of the scheduled action.</p>"""
    type: "capo_opensearch.types.action_type.ActionType"
    """<p>The type of action that will be taken on the domain.</p>"""
    severity: "capo_opensearch.types.action_severity.ActionSeverity"
    """<p>The severity of the action.</p>"""
    scheduled_time: "capo_opensearch.types.long.Long"
    """<p>The time when the change is scheduled to happen.</p>"""
    description: NotRequired["capo_opensearch.types.string.String"]
    """<p>A description of the action to be taken.</p>"""
    scheduled_by: NotRequired["capo_opensearch.types.scheduled_by.ScheduledBy"]
    """<p>Whether the action was scheduled manually (<code>CUSTOMER</code>, or by OpenSearch Service automatically (<code>SYSTEM</code>).</p>"""
    status: NotRequired["capo_opensearch.types.action_status.ActionStatus"]
    """<p>The current status of the scheduled action.</p>"""
    mandatory: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether the action is required or optional.</p>"""
    cancellable: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether or not the scheduled action is cancellable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduledAction) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_opensearch.types.action_type

    out["Type"] = capo_opensearch.types.action_type.serialize_json(value["type"])
    import capo_opensearch.types.action_severity

    out["Severity"] = capo_opensearch.types.action_severity.serialize_json(
        value["severity"]
    )
    out["ScheduledTime"] = value["scheduled_time"]
    if "description" in value:
        out["Description"] = value["description"]
    if "scheduled_by" in value:
        import capo_opensearch.types.scheduled_by

        out["ScheduledBy"] = capo_opensearch.types.scheduled_by.serialize_json(
            value["scheduled_by"]
        )
    if "status" in value:
        import capo_opensearch.types.action_status

        out["Status"] = capo_opensearch.types.action_status.serialize_json(
            value["status"]
        )
    if "mandatory" in value:
        out["Mandatory"] = value["mandatory"]
    if "cancellable" in value:
        out["Cancellable"] = value["cancellable"]
    return out


def deserialize_json(data: dict) -> ScheduledAction:
    out: ScheduledAction = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Type") is not None:
        import capo_opensearch.types.action_type

        out["type"] = capo_opensearch.types.action_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_opensearch.types.action_type.ActionType", "")
    if data.get("Severity") is not None:
        import capo_opensearch.types.action_severity

        out["severity"] = capo_opensearch.types.action_severity.deserialize_json(
            data["Severity"]
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_opensearch.types.action_severity.ActionSeverity", ""
        )
    if data.get("ScheduledTime") is not None:
        out["scheduled_time"] = data["ScheduledTime"]
    else:
        out["scheduled_time"] = 0
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ScheduledBy") is not None:
        import capo_opensearch.types.scheduled_by

        out["scheduled_by"] = capo_opensearch.types.scheduled_by.deserialize_json(
            data["ScheduledBy"]
        )
    if data.get("Status") is not None:
        import capo_opensearch.types.action_status

        out["status"] = capo_opensearch.types.action_status.deserialize_json(
            data["Status"]
        )
    if data.get("Mandatory") is not None:
        out["mandatory"] = data["Mandatory"]
    if data.get("Cancellable") is not None:
        out["cancellable"] = data["Cancellable"]
    return out
