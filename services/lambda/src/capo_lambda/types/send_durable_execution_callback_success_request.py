"""Generated from Smithy shape ``com.amazonaws.lambda#SendDurableExecutionCallbackSuccessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.binary_operation_payload
    import capo_lambda.types.callback_id


class SendDurableExecutionCallbackSuccessRequest(TypedDict, closed=True):
    callback_id: "capo_lambda.types.callback_id.CallbackId"
    """<p>The unique identifier for the callback operation.</p>"""
    result: NotRequired[
        "capo_lambda.types.binary_operation_payload.BinaryOperationPayload"
    ]
    """<p>The result data from the successful callback operation. Maximum size is 256 KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDurableExecutionCallbackSuccessRequest) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_lambda.types.binary_operation_payload

        out["Result"] = capo_lambda.types.binary_operation_payload.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> SendDurableExecutionCallbackSuccessRequest:
    out: SendDurableExecutionCallbackSuccessRequest = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_lambda.types.binary_operation_payload

        out["result"] = capo_lambda.types.binary_operation_payload.deserialize_json(
            data["Result"]
        )
    return out


def redact_sensitive(
    value: SendDurableExecutionCallbackSuccessRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "result" in value:
        out["result"] = "*** Sensitive Data Redacted ***"
    return out
