"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationStatusReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_configuration_status
    import capo_application_signals.types.instrumentation_error_cause
    import capo_application_signals.types.instrumentation_type


class InstrumentationConfigurationStatusReport(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """<p>The type of instrumentation configuration being reported.</p>"""
    signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType"
    """<p>The telemetry signal type for this instrumentation configuration.</p>"""
    location_hash: "str"
    """<p>The stable hash of the instrumentation location that identifies the configuration being reported.</p>"""
    status: "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
    """<p>The status of the instrumentation configuration: <code>READY</code>, <code>ERROR</code>, <code>ACTIVE</code>, or <code>DISABLED</code>.</p>"""
    time: "datetime.datetime"
    """<p>The timestamp when the status event occurred.</p>"""
    error_cause: NotRequired[
        "capo_application_signals.types.instrumentation_error_cause.InstrumentationErrorCause"
    ]
    """<p>The error cause when the status is <code>ERROR</code>, such as the file or method not being found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationConfigurationStatusReport) -> dict:
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
    if "error_cause" in value:
        import capo_application_signals.types.instrumentation_error_cause

        out["ErrorCause"] = (
            capo_application_signals.types.instrumentation_error_cause.serialize_json(
                value["error_cause"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstrumentationConfigurationStatusReport:
    out: InstrumentationConfigurationStatusReport = {}  # type: ignore[typeddict-item]
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
    if data.get("ErrorCause") is not None:
        import capo_application_signals.types.instrumentation_error_cause

        out["error_cause"] = (
            capo_application_signals.types.instrumentation_error_cause.deserialize_json(
                data["ErrorCause"]
            )
        )
    return out
