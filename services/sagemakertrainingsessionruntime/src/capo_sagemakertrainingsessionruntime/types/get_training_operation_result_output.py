"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#GetTrainingOperationResultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.operation_result
    import capo_sagemakertrainingsessionruntime.types.request_status
    import capo_sagemakertrainingsessionruntime.types.training_token_usage


class GetTrainingOperationResultOutput(TypedDict, closed=True):
    status: "capo_sagemakertrainingsessionruntime.types.request_status.RequestStatus"
    """<p>The current status of the operation. Possible values are <code>Pending</code>, <code>InProgress</code>, <code>Completed</code>, <code>Failed</code>, or <code>Skipped</code>.</p>"""
    operation_result: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.operation_result.OperationResult"
    ]
    """<p>The result payload of the operation. The service populates this field only when the status is <code>Completed</code>. The populated member of the union corresponds to the operation type that was submitted.</p>"""
    error_details: NotRequired["str"]
    """<p>A message describing why the operation failed. The service populates this field only when the status is <code>Failed</code>.</p>"""
    token_usage: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.training_token_usage.TrainingTokenUsage"
    ]
    """<p>The token usage statistics for metering purposes. The service populates this field for forward and forwardBackward operations upon completion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainingOperationResultOutput) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.request_status

    out["status"] = (
        capo_sagemakertrainingsessionruntime.types.request_status.serialize_json(
            value["status"]
        )
    )
    if "operation_result" in value:
        import capo_sagemakertrainingsessionruntime.types.operation_result

        out["operationResult"] = (
            capo_sagemakertrainingsessionruntime.types.operation_result.serialize_json(
                value["operation_result"]
            )
        )
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    if "token_usage" in value:
        import capo_sagemakertrainingsessionruntime.types.training_token_usage

        out["tokenUsage"] = (
            capo_sagemakertrainingsessionruntime.types.training_token_usage.serialize_json(
                value["token_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTrainingOperationResultOutput:
    out: GetTrainingOperationResultOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_sagemakertrainingsessionruntime.types.request_status

        out["status"] = (
            capo_sagemakertrainingsessionruntime.types.request_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_sagemakertrainingsessionruntime.types.request_status.RequestStatus",
            "",
        )
    if data.get("operationResult") is not None:
        import capo_sagemakertrainingsessionruntime.types.operation_result

        out["operation_result"] = (
            capo_sagemakertrainingsessionruntime.types.operation_result.deserialize_json(
                data["operationResult"]
            )
        )
    if data.get("errorDetails") is not None:
        out["error_details"] = data["errorDetails"]
    if data.get("tokenUsage") is not None:
        import capo_sagemakertrainingsessionruntime.types.training_token_usage

        out["token_usage"] = (
            capo_sagemakertrainingsessionruntime.types.training_token_usage.deserialize_json(
                data["tokenUsage"]
            )
        )
    return out
