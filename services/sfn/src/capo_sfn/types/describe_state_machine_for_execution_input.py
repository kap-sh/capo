"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineForExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.included_data


class DescribeStateMachineForExecutionInput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution you want state machine information for.</p>"""
    included_data: NotRequired["capo_sfn.types.included_data.IncludedData"]
    """<p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineForExecutionInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "included_data" in value:
        import capo_sfn.types.included_data

        out["includedData"] = capo_sfn.types.included_data.serialize_aws_json_1_0(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineForExecutionInput:
    out: DescribeStateMachineForExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("includedData") is not None:
        import capo_sfn.types.included_data

        out["included_data"] = capo_sfn.types.included_data.deserialize_aws_json_1_0(
            data["includedData"]
        )
    return out
