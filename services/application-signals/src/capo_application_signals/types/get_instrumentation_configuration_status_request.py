"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetInstrumentationConfigurationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_configuration_status
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.location_identifier
    import capo_application_signals.types.next_token


class GetInstrumentationConfigurationStatusRequest(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Type of instrumentation configuration (BREAKPOINT or PROBE). Required to identify the configuration to retrieve."""
    service: "str"
    """Service name for the instrumentation configuration."""
    environment: "str"
    """Environment name for the instrumentation configuration."""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """Signal type for the instrumentation configuration."""
    location_identifier: (
        "capo_application_signals.types.location_identifier.LocationIdentifier"
    )
    """Location identifier - either full code location or a pre-computed hash."""
    status: NotRequired[
        "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
    ]
    """<p>The single status to query for. If omitted, only <code>ACTIVE</code> status events are returned.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the time range to retrieve status events for. <code>StartTime</code> and <code>EndTime</code> must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end of the time range to retrieve status events for. <code>StartTime</code> and <code>EndTime</code> must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of status events to return in one call. The default is 60.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Use the token returned by a previous call to retrieve the next page of status events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstrumentationConfigurationStatusRequest) -> dict:
    out: dict = {}
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.dynamic_instrumentation_signal_type

    out["SignalType"] = (
        capo_application_signals.types.dynamic_instrumentation_signal_type.serialize_json(
            value["signal_type"]
        )
    )
    import capo_application_signals.types.location_identifier

    out["LocationIdentifier"] = (
        capo_application_signals.types.location_identifier.serialize_json(
            value["location_identifier"]
        )
    )
    if "status" in value:
        import capo_application_signals.types.instrumentation_configuration_status

        out["Status"] = (
            capo_application_signals.types.instrumentation_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["StartTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["EndTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["end_time"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInstrumentationConfigurationStatusRequest:
    out: GetInstrumentationConfigurationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstrumentationType") is not None:
        import capo_application_signals.types.instrumentation_type

        out["instrumentation_type"] = (
            capo_application_signals.types.instrumentation_type.deserialize_json(
                data["InstrumentationType"]
            )
        )
    else:
        import typing

        out["instrumentation_type"] = typing.cast(
            "capo_application_signals.types.instrumentation_type.InstrumentationType",
            "",
        )
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
    if data.get("LocationIdentifier") is not None:
        import capo_application_signals.types.location_identifier

        out["location_identifier"] = (
            capo_application_signals.types.location_identifier.deserialize_json(
                data["LocationIdentifier"]
            )
        )
    else:
        out["location_identifier"] = {"$unknown": {"name": ""}}
    if data.get("Status") is not None:
        import capo_application_signals.types.instrumentation_configuration_status

        out["status"] = (
            capo_application_signals.types.instrumentation_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["end_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
