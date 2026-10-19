"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceDependenciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.next_token
    import capo_application_signals.types.service_dependencies


class ListServiceDependenciesOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    service_dependencies: (
        "capo_application_signals.types.service_dependencies.ServiceDependencies"
    )
    """<p>An array, where each object in the array contains information about one of the dependencies of this service.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get next set of service dependencies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceDependenciesOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["EndTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_application_signals.types.service_dependencies

    out["ServiceDependencies"] = (
        capo_application_signals.types.service_dependencies.serialize_json(
            value["service_dependencies"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceDependenciesOutput:
    out: ListServiceDependenciesOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("ServiceDependencies") is not None:
        import capo_application_signals.types.service_dependencies

        out["service_dependencies"] = (
            capo_application_signals.types.service_dependencies.deserialize_json(
                data["ServiceDependencies"]
            )
        )
    else:
        out["service_dependencies"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
