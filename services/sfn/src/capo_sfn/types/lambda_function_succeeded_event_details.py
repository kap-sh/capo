"""Generated from Smithy shape ``com.amazonaws.sfn#LambdaFunctionSucceededEventDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.history_event_execution_data_details
    import capo_sfn.types.sensitive_data


class LambdaFunctionSucceededEventDetails(TypedDict, closed=True):
    output: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON data output by the Lambda function. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    output_details: NotRequired[
        "capo_sfn.types.history_event_execution_data_details.HistoryEventExecutionDataDetails"
    ]
    """<p>Contains details about the output of an execution history event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionSucceededEventDetails) -> dict:
    out: dict = {}
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import capo_sfn.types.history_event_execution_data_details

        out["outputDetails"] = (
            capo_sfn.types.history_event_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionSucceededEventDetails:
    out: LambdaFunctionSucceededEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("output") is not None:
        out["output"] = data["output"]
    if data.get("outputDetails") is not None:
        import capo_sfn.types.history_event_execution_data_details

        out["output_details"] = (
            capo_sfn.types.history_event_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    return out


def redact_sensitive(value: LambdaFunctionSucceededEventDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output" in value:
        out["output"] = "*** Sensitive Data Redacted ***"
    return out
