"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#GetSamplingOperationResultOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.request_status
    import capo_sagemakertrainingsessionruntime.types.sample_operation_result


class GetSamplingOperationResultOutput(TypedDict, closed=True):
    status: "capo_sagemakertrainingsessionruntime.types.request_status.RequestStatus"
    """<p>The current status of the sample operation. Possible values are <code>Pending</code>, <code>InProgress</code>, <code>Completed</code>, or <code>Failed</code>.</p>"""
    operation_result: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.sample_operation_result.SampleOperationResult"
    ]
    """<p>The result payload of the sample operation. The service populates this field only when the status is <code>Completed</code>.</p>"""
    error_details: NotRequired["str"]
    """<p>A message describing why the sample operation failed. The service populates this field only when the status is <code>Failed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingOperationResultOutput) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.request_status

    out["status"] = (
        capo_sagemakertrainingsessionruntime.types.request_status.serialize_json(
            value["status"]
        )
    )
    if "operation_result" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_operation_result

        out["operationResult"] = (
            capo_sagemakertrainingsessionruntime.types.sample_operation_result.serialize_json(
                value["operation_result"]
            )
        )
    if "error_details" in value:
        out["errorDetails"] = value["error_details"]
    return out


def deserialize_json(data: dict) -> GetSamplingOperationResultOutput:
    out: GetSamplingOperationResultOutput = {}  # type: ignore[typeddict-item]
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
        import capo_sagemakertrainingsessionruntime.types.sample_operation_result

        out["operation_result"] = (
            capo_sagemakertrainingsessionruntime.types.sample_operation_result.deserialize_json(
                data["operationResult"]
            )
        )
    if data.get("errorDetails") is not None:
        out["error_details"] = data["errorDetails"]
    return out


def redact_sensitive(value: GetSamplingOperationResultOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "operation_result" in value:
        import capo_sagemakertrainingsessionruntime.types.sample_operation_result

        out["operation_result"] = (
            capo_sagemakertrainingsessionruntime.types.sample_operation_result.redact_sensitive(
                value["operation_result"]
            )
        )
    return out
