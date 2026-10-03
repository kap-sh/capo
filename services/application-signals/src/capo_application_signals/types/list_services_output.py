"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.next_token
    import capo_application_signals.types.service_summaries


class ListServicesOutput(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    end_time: "datetime.datetime"
    """<p>The end of the time period that the returned information applies to. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>This displays the time that Application Signals used for the request. It might not match your request exactly, because it was rounded to the nearest hour.</p>"""
    service_summaries: (
        "capo_application_signals.types.service_summaries.ServiceSummaries"
    )
    """<p>An array of structures, where each structure contains some information about a service. To get complete information about a service, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetService.html">GetService</a>.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get next set of services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["StartTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_application_signals.types._prelude.timestamp

    out["EndTime"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import capo_application_signals.types.service_summaries

    out["ServiceSummaries"] = (
        capo_application_signals.types.service_summaries.serialize_json(
            value["service_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListServicesOutput.start_time required")
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    else:
        raise DeserializationError("ListServicesOutput.end_time required")
    if data.get("ServiceSummaries") is not None:
        import capo_application_signals.types.service_summaries

        out["service_summaries"] = (
            capo_application_signals.types.service_summaries.deserialize_json(
                data["ServiceSummaries"]
            )
        )
    else:
        raise DeserializationError("ListServicesOutput.service_summaries required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
