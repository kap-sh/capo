"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackFailureRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.callback_id
    import capo_lambda.types.error_object


class SendDurableExecutionCallbackFailureRequest(TypedDict, closed=True):
    callback_id: "capo_lambda.types.callback_id.CallbackId"
    """<p>The unique identifier for the callback operation.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Error details describing why the callback operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackFailureRequest) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackFailureRequest:
    out: SendDurableExecutionCallbackFailureRequest = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    return out


def redact_sensitive(
    value: SendDurableExecutionCallbackFailureRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out
