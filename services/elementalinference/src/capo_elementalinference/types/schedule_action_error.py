"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.schedule_action_error_code


class ScheduleActionError(TypedDict, closed=True):
    error_code: "capo_elementalinference.types.schedule_action_error_code.ScheduleActionErrorCode"
    """<p>The type of failure. Valid values are the following:</p> <dl> <dt>INVALID_ACTION_TARGET</dt> <dd> <p>The action referred to something that didn't exist or wasn't valid at the scheduled time, for example an output that you deleted. </p> </dd> <dt>INTERNAL_ERROR</dt> <dd> <p>An unexpected error prevented the action from completing.</p> </dd> </dl>"""
    error_message: "str"
    """<p>A description of the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionError) -> dict:
    out: dict = {}
    import capo_elementalinference.types.schedule_action_error_code

    out["errorCode"] = (
        capo_elementalinference.types.schedule_action_error_code.serialize_json(
            value["error_code"]
        )
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ScheduleActionError:
    out: ScheduleActionError = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_elementalinference.types.schedule_action_error_code

        out["error_code"] = (
            capo_elementalinference.types.schedule_action_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_elementalinference.types.schedule_action_error_code.ScheduleActionErrorCode",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
