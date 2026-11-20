"""Generated from Smithy shape ``com.amazonaws.connectscheduling#GetTimeOffResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connectscheduling.types.actor_info
    import capo_connectscheduling.types.description
    import capo_connectscheduling.types.shift_activity_id
    import capo_connectscheduling.types.time_off_id
    import capo_connectscheduling.types.time_off_status
    import capo_connectscheduling.types.time_off_validation_results
    import capo_connectscheduling.types.user_id


class GetTimeOffResponse(TypedDict, closed=True):
    time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId"
    """<p>The identifier of the time off request.</p>"""
    user_id: "capo_connectscheduling.types.user_id.UserId"
    """<p>The identifier of the user the time off is for.</p>"""
    shift_activity_id: "capo_connectscheduling.types.shift_activity_id.ShiftActivityId"
    """<p>The identifier of the shift activity for the time off request.</p>"""
    start_at: "datetime.datetime"
    """<p>The start of the time off window, inclusive, as sent to <code>CreateTimeOff</code>.</p>"""
    end_at: "datetime.datetime"
    """<p>The end of the time off window, exclusive, as sent to <code>CreateTimeOff</code>.</p>"""
    status: "capo_connectscheduling.types.time_off_status.TimeOffStatus"
    """<p>The status of the time off request.</p> <ul> <li> <p> <code>PENDING</code>: Connect Customer is processing a change to the request, which then changes to another status. An edit in the Connect Customer admin website can also make a request <code>PENDING</code>, so an <code>APPROVED</code> request can become <code>PENDING</code> and then end <code>APPROVED</code> or <code>REJECTED</code>.</p> </li> <li> <p> <code>AWAITING_APPROVAL</code>: the request is waiting for an <code>ApproveTimeOff</code> or <code>RejectTimeOff</code> call.</p> </li> </ul>"""
    description: NotRequired["capo_connectscheduling.types.description.Description"]
    """<p>The description of the time off request. <code>CreateTimeOff</code> sets it, and <code>CancelTimeOff</code> replaces or removes it. An edit in the Connect Customer admin website can also change it. <code>GetTimeOff</code> doesn't return descriptions sent with <code>ApproveTimeOff</code> or <code>RejectTimeOff</code>.</p>"""
    validation_results: NotRequired[
        "capo_connectscheduling.types.time_off_validation_results.TimeOffValidationResults"
    ]
    """<p>Warnings or failures produced while processing the time off request.</p>"""
    created_by: "capo_connectscheduling.types.actor_info.ActorInfo"
    """<p>The identity that created the request. Immutable for the life of the request.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the time off request was created.</p>"""
    updated_by: NotRequired["capo_connectscheduling.types.actor_info.ActorInfo"]
    """<p>The identity that made the most recent <code>ApproveTimeOff</code>, <code>RejectTimeOff</code>, or <code>CancelTimeOff</code> call on the request, or took the same action in the Connect Customer admin website. Absent until one of those actions is taken, including after Connect Customer decides an <code>AUTOMATIC</code> request. <code>UpdatedAt</code> also changes when a <code>PENDING</code> request changes to another status and for other edits, which don't set <code>UpdatedBy</code>.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the time off request was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeOffResponse) -> dict:
    out: dict = {}
    out["TimeOffId"] = value["time_off_id"]
    out["UserId"] = value["user_id"]
    out["ShiftActivityId"] = value["shift_activity_id"]
    import capo_connectscheduling.types._prelude.timestamp

    out["StartAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["start_at"]
    )
    import capo_connectscheduling.types._prelude.timestamp

    out["EndAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["end_at"]
    )
    import capo_connectscheduling.types.time_off_status

    out["Status"] = capo_connectscheduling.types.time_off_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "validation_results" in value:
        import capo_connectscheduling.types.time_off_validation_results

        out["ValidationResults"] = (
            capo_connectscheduling.types.time_off_validation_results.serialize_json(
                value["validation_results"]
            )
        )
    import capo_connectscheduling.types.actor_info

    out["CreatedBy"] = capo_connectscheduling.types.actor_info.serialize_json(
        value["created_by"]
    )
    import capo_connectscheduling.types._prelude.timestamp

    out["CreatedAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_by" in value:
        import capo_connectscheduling.types.actor_info

        out["UpdatedBy"] = capo_connectscheduling.types.actor_info.serialize_json(
            value["updated_by"]
        )
    import capo_connectscheduling.types._prelude.timestamp

    out["UpdatedAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetTimeOffResponse:
    out: GetTimeOffResponse = {}  # type: ignore[typeddict-item]
    if data.get("TimeOffId") is not None:
        out["time_off_id"] = data["TimeOffId"]
    else:
        out["time_off_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("ShiftActivityId") is not None:
        out["shift_activity_id"] = data["ShiftActivityId"]
    else:
        out["shift_activity_id"] = ""
    if data.get("StartAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["start_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["StartAt"]
            )
        )
    else:
        import datetime

        out["start_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["end_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["EndAt"]
            )
        )
    else:
        import datetime

        out["end_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_connectscheduling.types.time_off_status

        out["status"] = capo_connectscheduling.types.time_off_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connectscheduling.types.time_off_status.TimeOffStatus", ""
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ValidationResults") is not None:
        import capo_connectscheduling.types.time_off_validation_results

        out["validation_results"] = (
            capo_connectscheduling.types.time_off_validation_results.deserialize_json(
                data["ValidationResults"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_connectscheduling.types.actor_info

        out["created_by"] = capo_connectscheduling.types.actor_info.deserialize_json(
            data["CreatedBy"]
        )
    else:
        out["created_by"] = {"$unknown": {"name": ""}}
    if data.get("CreatedAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["created_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedBy") is not None:
        import capo_connectscheduling.types.actor_info

        out["updated_by"] = capo_connectscheduling.types.actor_info.deserialize_json(
            data["UpdatedBy"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["updated_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: GetTimeOffResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
