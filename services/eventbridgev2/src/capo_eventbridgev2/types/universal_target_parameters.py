"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#UniversalTargetParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.string
    import capo_eventbridgev2.types.universal_target_input


class UniversalTargetParameters(TypedDict, closed=True):
    input: "capo_eventbridgev2.types.universal_target_input.UniversalTargetInput"
    """JSON string or JSONata expression that produces the API request. Supports {% ... %} JSONata expressions for dynamic values from the event."""
    invocation_timeout_seconds: NotRequired["capo_eventbridgev2.types.string.String"]
    """Timeout in seconds for each invocation of the target (1-30, default 30). Accepts a literal integer or a {% ... %} JSONata expression evaluated against the event at invocation time. A JSONata expression is syntax-checked at create time. Resolved values outside of the range [1, 30] will be constrained to the nearest bound at delivery time. Defaults to 30 seconds when unset."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UniversalTargetParameters) -> dict:
    out: dict = {}
    out["Input"] = value["input"]
    if "invocation_timeout_seconds" in value:
        out["InvocationTimeoutSeconds"] = value["invocation_timeout_seconds"]
    return out


def deserialize_cbor(data: dict) -> UniversalTargetParameters:
    out: UniversalTargetParameters = {}  # type: ignore[typeddict-item]
    if data.get("Input") is not None:
        out["input"] = data["Input"]
    else:
        out["input"] = ""
    if data.get("InvocationTimeoutSeconds") is not None:
        out["invocation_timeout_seconds"] = data["InvocationTimeoutSeconds"]
    return out
