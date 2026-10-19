"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UnprocessedStatusEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_configuration_status
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.unprocessed_status_event_failure_reason


class UnprocessedStatusEvent(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """<p>The type of instrumentation configuration for the unprocessed status event.</p>"""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """<p>The telemetry signal type for the unprocessed status event.</p>"""
    location_hash: "str"
    """<p>The stable hash of the instrumentation location for the unprocessed event.</p>"""
    status: "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
    """<p>The status that failed to be processed.</p>"""
    time: "datetime.datetime"
    """<p>The timestamp of the status event that failed to be processed.</p>"""
    failed_reason: "capo_application_signals.types.unprocessed_status_event_failure_reason.UnprocessedStatusEventFailureReason"
    """<p>The reason why this status event could not be processed, such as throttling or validation errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatusEvent) -> dict:
    out: dict = {}
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    import capo_application_signals.types.dynamic_instrumentation_signal_type

    out["SignalType"] = (
        capo_application_signals.types.dynamic_instrumentation_signal_type.serialize_json(
            value["signal_type"]
        )
    )
    out["LocationHash"] = value["location_hash"]
    import capo_application_signals.types.instrumentation_configuration_status

    out["Status"] = (
        capo_application_signals.types.instrumentation_configuration_status.serialize_json(
            value["status"]
        )
    )
    import capo_application_signals.types._prelude.timestamp

    out["Time"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["time"]
    )
    import capo_application_signals.types.unprocessed_status_event_failure_reason

    out["FailedReason"] = (
        capo_application_signals.types.unprocessed_status_event_failure_reason.serialize_json(
            value["failed_reason"]
        )
    )
    return out


def deserialize_json(data: dict) -> UnprocessedStatusEvent:
    out: UnprocessedStatusEvent = {}  # type: ignore[typeddict-item]
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
    if data.get("LocationHash") is not None:
        out["location_hash"] = data["LocationHash"]
    else:
        out["location_hash"] = ""
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
    if data.get("Time") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["Time"]
            )
        )
    else:
        import datetime

        out["time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("FailedReason") is not None:
        import capo_application_signals.types.unprocessed_status_event_failure_reason

        out["failed_reason"] = (
            capo_application_signals.types.unprocessed_status_event_failure_reason.deserialize_json(
                data["FailedReason"]
            )
        )
    else:
        import typing

        out["failed_reason"] = typing.cast(
            "capo_application_signals.types.unprocessed_status_event_failure_reason.UnprocessedStatusEventFailureReason",
            "",
        )
    return out
