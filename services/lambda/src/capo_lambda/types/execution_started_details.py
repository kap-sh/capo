"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionStartedDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.duration_seconds
    import capo_lambda.types.event_input


class ExecutionStartedDetails(TypedDict, closed=True):
    input: "capo_lambda.types.event_input.EventInput"
    """<p>The input payload provided for the durable execution.</p>"""
    execution_timeout: "capo_lambda.types.duration_seconds.DurationSeconds"
    """<p>The maximum amount of time that the durable execution is allowed to run, in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStartedDetails) -> dict:
    out: dict = {}
    import capo_lambda.types.event_input

    out["Input"] = capo_lambda.types.event_input.serialize_json(value["input"])
    out["ExecutionTimeout"] = value["execution_timeout"]
    return out


def deserialize_json(data: dict) -> ExecutionStartedDetails:
    out: ExecutionStartedDetails = {}  # type: ignore[typeddict-item]
    if data.get("Input") is not None:
        import capo_lambda.types.event_input

        out["input"] = capo_lambda.types.event_input.deserialize_json(data["Input"])
    else:
        raise DeserializationError("ExecutionStartedDetails.input required")
    if data.get("ExecutionTimeout") is not None:
        out["execution_timeout"] = data["ExecutionTimeout"]
    else:
        raise DeserializationError("ExecutionStartedDetails.execution_timeout required")
    return out


def redact_sensitive(value: ExecutionStartedDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_lambda.types.event_input

        out["input"] = capo_lambda.types.event_input.redact_sensitive(value["input"])
    return out
