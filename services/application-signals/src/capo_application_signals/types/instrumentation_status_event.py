"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationStatusEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.instrumentation_error_cause


class InstrumentationStatusEvent(TypedDict, closed=True):
    time: "datetime.datetime"
    """<p>The time when the status was reported, rounded to the nearest minute.</p>"""
    error_cause: NotRequired[
        "capo_application_signals.types.instrumentation_error_cause.InstrumentationErrorCause"
    ]
    """<p>The error cause when the status is <code>ERROR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationStatusEvent) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> InstrumentationStatusEvent:
    out: InstrumentationStatusEvent = {}  # type: ignore[typeddict-item]
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
