"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetInstrumentationConfigurationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_configuration_status
    import capo_application_signals.types.instrumentation_status_event_list
    import capo_application_signals.types.location
    import capo_application_signals.types.next_token


class GetInstrumentationConfigurationStatusResponse(TypedDict, closed=True):
    service: "str"
    """<p>The service name echoed from the request.</p>"""
    environment: "str"
    """<p>The environment echoed from the request.</p>"""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """<p>The telemetry signal type echoed from the request.</p>"""
    location: "capo_application_signals.types.location.Location"
    """<p>The code location echoed from the request.</p>"""
    status: "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
    """<p>The status that was queried. If not specified in the request, this is <code>ACTIVE</code>.</p>"""
    events: "capo_application_signals.types.instrumentation_status_event_list.InstrumentationStatusEventList"
    """<p>The list of status events within the requested time window, sorted with the most recent first. Error events include an error cause.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Pagination token to continue retrieving status events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstrumentationConfigurationStatusResponse) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.dynamic_instrumentation_signal_type

    out["SignalType"] = (
        capo_application_signals.types.dynamic_instrumentation_signal_type.serialize_json(
            value["signal_type"]
        )
    )
    import capo_application_signals.types.location

    out["Location"] = capo_application_signals.types.location.serialize_json(
        value["location"]
    )
    import capo_application_signals.types.instrumentation_configuration_status

    out["Status"] = (
        capo_application_signals.types.instrumentation_configuration_status.serialize_json(
            value["status"]
        )
    )
    import capo_application_signals.types.instrumentation_status_event_list

    out["Events"] = (
        capo_application_signals.types.instrumentation_status_event_list.serialize_json(
            value["events"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInstrumentationConfigurationStatusResponse:
    out: GetInstrumentationConfigurationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
    if data.get("SignalType") is not None:
        import capo_application_signals.types.dynamic_instrumentation_signal_type

        out["signal_type"] = (
            capo_application_signals.types.dynamic_instrumentation_signal_type.deserialize_json(
                data["SignalType"]
            )
        )
    else:
        import typing

        out["signal_type"] = typing.cast(
            "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
            "",
        )
    if data.get("Location") is not None:
        import capo_application_signals.types.location

        out["location"] = capo_application_signals.types.location.deserialize_json(
            data["Location"]
        )
    else:
        import capo_application_signals.types._unknown

        out["location"] = capo_application_signals.types._unknown.UnknownUnionMember("")
    if data.get("Status") is not None:
        import capo_application_signals.types.instrumentation_configuration_status

        out["status"] = (
            capo_application_signals.types.instrumentation_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus",
            "",
        )
    if data.get("Events") is not None:
        import capo_application_signals.types.instrumentation_status_event_list

        out["events"] = (
            capo_application_signals.types.instrumentation_status_event_list.deserialize_json(
                data["Events"]
            )
        )
    else:
        out["events"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
