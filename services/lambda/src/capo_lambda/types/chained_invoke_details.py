"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.error_object
    import capo_lambda.types.operation_payload


class ChainedInvokeDetails(TypedDict, closed=True):
    result: NotRequired["capo_lambda.types.operation_payload.OperationPayload"]
    """<p>The response payload from the chained invocation.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Details about the chained invocation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeDetails) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> ChainedInvokeDetails:
    out: ChainedInvokeDetails = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        out["result"] = data["Result"]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    return out


def redact_sensitive(value: ChainedInvokeDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        out["result"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out
