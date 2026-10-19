"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_type


class BatchDeleteScope(TypedDict, closed=True):
    service: "str"
    """Service name for the instrumentation configurations."""
    environment: "str"
    """Environment identifier for the instrumentation configurations."""
    instrumentation_type: (
        "capo_application_signals.types.instrumentation_type.InstrumentationType"
    )
    """Instrumentation type: BREAKPOINT or PROBE."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteScope) -> dict:
    out: dict = {}
    out["Service"] = value["service"]
    out["Environment"] = value["environment"]
    import capo_application_signals.types.instrumentation_type

    out["InstrumentationType"] = (
        capo_application_signals.types.instrumentation_type.serialize_json(
            value["instrumentation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteScope:
    out: BatchDeleteScope = {}  # type: ignore[typeddict-item]
    if data.get("Service") is not None:
        out["service"] = data["Service"]
    else:
        out["service"] = ""
    if data.get("Environment") is not None:
        out["environment"] = data["Environment"]
    else:
        out["environment"] = ""
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
    return out
