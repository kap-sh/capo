"""Generated from Smithy shape ``com.amazonaws.lambda#ContextDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.error_object
    import capo_lambda.types.operation_payload
    import capo_lambda.types.replay_children


class ContextDetails(TypedDict, closed=True):
    replay_children: NotRequired["capo_lambda.types.replay_children.ReplayChildren"]
    """<p>Whether the state data of child operations of this completed context should be included in the invoke payload and <code>GetDurableExecutionState</code> response.</p>"""
    result: NotRequired["capo_lambda.types.operation_payload.OperationPayload"]
    """<p>The response payload from the context.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Details about the context failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextDetails) -> dict:
    out: dict = {}
    if "replay_children" in value:
        out["ReplayChildren"] = value["replay_children"]
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ContextDetails:
    out: ContextDetails = {}  # type: ignore[typeddict-item]
    if data.get("ReplayChildren") is not None:
        out["replay_children"] = data["ReplayChildren"]
    if data.get("Result") is not None:
        out["result"] = data["Result"]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    return out


def redact_sensitive(value: ContextDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        out["result"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out
