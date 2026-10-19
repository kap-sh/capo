"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationAsyncResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.invocation_arn


class InvokeDataAutomationAsyncResponse(TypedDict, closed=True):
    invocation_arn: (
        "capo_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn"
    )
    """ARN of the automation job"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationAsyncResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationAsyncResponse:
    out: InvokeDataAutomationAsyncResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationArn") is not None:
        out["invocation_arn"] = data["invocationArn"]
    else:
        out["invocation_arn"] = ""
    return out
