"""Generated from Smithy shape ``com.amazonaws.novaact#InvokeActStepResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.calls
    import capo_nova_act.types.uuid_string


class InvokeActStepResponse(TypedDict, closed=True):
    calls: "capo_nova_act.types.calls.Calls"
    """<p>A list of tool calls that the act wants to execute in this step.</p>"""
    step_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for this execution step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeActStepResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.calls

    out["calls"] = capo_nova_act.types.calls.serialize_json(value["calls"])
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> InvokeActStepResponse:
    out: InvokeActStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("calls") is not None:
        import capo_nova_act.types.calls

        out["calls"] = capo_nova_act.types.calls.deserialize_json(data["calls"])
    else:
        raise DeserializationError("InvokeActStepResponse.calls required")
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("InvokeActStepResponse.step_id required")
    return out


def redact_sensitive(value: InvokeActStepResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "calls" in value:
        import capo_nova_act.types.calls

        out["calls"] = capo_nova_act.types.calls.redact_sensitive(value["calls"])
    return out
