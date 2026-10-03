"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.log_group_references
    import capo_application_signals.types.service


class GetServiceOutput(TypedDict, closed=True):
    service: "capo_application_signals.types.service.Service"
    """<p>A structure containing information about the service.</p>"""
    start_time: "datetime.datetime"
    """<p>The start time of the data included in the response. In a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code>.</p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the data included in the response. In a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code>.</p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    log_group_references: NotRequired[
        "capo_application_signals.types.log_group_references.LogGroupReferences"
    ]
    """<p>An array of string-to-string maps that each contain information about one log group associated with this service. Each string-to-string map includes the following fields:</p> <ul> <li> <p> <code>"Type": "AWS::Resource"</code> </p> </li> <li> <p> <code>"ResourceType": "AWS::Logs::LogGroup"</code> </p> </li> <li> <p> <code>"Identifier": "<i>name-of-log-group</i>"</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types.service

    out["Service"] = capo_application_signals.types.service.serialize_json(
        value["service"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["EndTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    if "log_group_references" in value:
        import capo_application_signals.types.log_group_references

        out["LogGroupReferences"] = (
            capo_application_signals.types.log_group_references.serialize_json(
                value["log_group_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServiceOutput:
    out: GetServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        import capo_application_signals.types.service

        out["service"] = capo_application_signals.types.service.deserialize_json(
            data["Service"]
        )
    else:
        raise DeserializationError("GetServiceOutput.service required")
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("GetServiceOutput.start_time required")
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("GetServiceOutput.end_time required")
    if data.get("LogGroupReferences") is not None:
        import capo_application_signals.types.log_group_references

        out["log_group_references"] = (
            capo_application_signals.types.log_group_references.deserialize_json(
                data["LogGroupReferences"]
            )
        )
    return out
