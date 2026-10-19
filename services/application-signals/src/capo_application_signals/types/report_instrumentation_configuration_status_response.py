"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ReportInstrumentationConfigurationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.unprocessed_status_event_list


class ReportInstrumentationConfigurationStatusResponse(TypedDict, closed=True):
    service: "str"
    """<p>The service name echoed from the request.</p>"""
    environment: "str"
    """<p>The environment echoed from the request.</p>"""
    unprocessed_status_events: "capo_application_signals.types.unprocessed_status_event_list.UnprocessedStatusEventList"
    """<p>Status events that failed to be processed. Each entry includes the configuration identifiers, status, timestamp, and a reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportInstrumentationConfigurationStatusResponse) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.unprocessed_status_event_list

    out["UnprocessedStatusEvents"] = (
        capo_application_signals.types.unprocessed_status_event_list.serialize_json(
            value["unprocessed_status_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReportInstrumentationConfigurationStatusResponse:
    out: ReportInstrumentationConfigurationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
    if data.get("UnprocessedStatusEvents") is not None:
        import capo_application_signals.types.unprocessed_status_event_list

        out["unprocessed_status_events"] = (
            capo_application_signals.types.unprocessed_status_event_list.deserialize_json(
                data["UnprocessedStatusEvents"]
            )
        )
    else:
        out["unprocessed_status_events"] = []
    return out
