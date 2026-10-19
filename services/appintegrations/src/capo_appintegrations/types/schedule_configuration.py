"""Generated from Smithy shape ``com.amazonaws.appintegrations#ScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.non_blank_string
    import capo_appintegrations.types.object


class ScheduleConfiguration(TypedDict, closed=True):
    first_execution_from: NotRequired[
        "capo_appintegrations.types.non_blank_string.NonBlankString"
    ]
    """<p>The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.</p>"""
    object: NotRequired["capo_appintegrations.types.object.Object"]
    """<p>The name of the object to pull from the data source.</p>"""
    schedule_expression: "capo_appintegrations.types.non_blank_string.NonBlankString"
    """<p>How often the data should be pulled from data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    if "first_execution_from" in value:
        out["FirstExecutionFrom"] = value["first_execution_from"]
    if "object" in value:
        out["Object"] = value["object"]
    out["ScheduleExpression"] = value["schedule_expression"]
    return out


def deserialize_json(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FirstExecutionFrom") is not None:
        out["first_execution_from"] = data["FirstExecutionFrom"]
    if data.get("Object") is not None:
        out["object"] = data["Object"]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    else:
        out["schedule_expression"] = ""
    return out
