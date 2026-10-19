"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceStatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.next_token
    import capo_application_signals.types.service_states


class ListServiceStatesOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>"""
    service_states: "capo_application_signals.types.service_states.ServiceStates"
    """<p>An array of structures, where each structure contains information about the state of one service, including its latest change events such as deployments.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of service states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceStatesOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["EndTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_application_signals.types.service_states

    out["ServiceStates"] = capo_application_signals.types.service_states.serialize_json(
        value["service_states"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceStatesOutput:
    out: ListServiceStatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ServiceStates") is not None:
        import capo_application_signals.types.service_states

        out["service_states"] = (
            capo_application_signals.types.service_states.deserialize_json(
                data["ServiceStates"]
            )
        )
    else:
        out["service_states"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
