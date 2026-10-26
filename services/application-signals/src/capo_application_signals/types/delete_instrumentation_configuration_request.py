"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DeleteInstrumentationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.location_identifier


class DeleteInstrumentationConfigurationRequest(TypedDict, closed=True):
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Type of instrumentation configuration (BREAKPOINT or PROBE). Required to identify the configuration to delete."""
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


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstrumentationConfigurationRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> DeleteInstrumentationConfigurationRequest:
    out: DeleteInstrumentationConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    return out
