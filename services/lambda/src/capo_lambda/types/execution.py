"""Generated from Smithy shape ``com.amazonaws.lambda#Execution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.execution_status
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.name_spaced_function_arn


class Execution(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution, if this execution is a durable execution.</p>"""
    durable_execution_name: (
        "capo_lambda.types.durable_execution_name.DurableExecutionName"
    )
    """<p>The unique name of the durable execution, if one was provided when the execution was started.</p>"""
    function_arn: "capo_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function.</p>"""
    status: "capo_lambda.types.execution_status.ExecutionStatus"
    """<p>The current status of the durable execution.</p>"""
    start_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the durable execution started, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>The date and time when the durable execution ended, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Execution) -> dict:
    out: dict = {}
    out["DurableExecutionArn"] = value["durable_execution_arn"]
    out["DurableExecutionName"] = value["durable_execution_name"]
    out["FunctionArn"] = value["function_arn"]
    import capo_lambda.types.execution_status

    out["Status"] = capo_lambda.types.execution_status.serialize_json(value["status"])
    import capo_lambda.types.execution_timestamp

    out["StartTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    if "end_timestamp" in value:
        import capo_lambda.types.execution_timestamp

        out["EndTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> Execution:
    out: Execution = {}  # type: ignore[typeddict-item]
    if data.get("DurableExecutionArn") is not None:
        out["durable_execution_arn"] = data["DurableExecutionArn"]
    else:
        raise DeserializationError("Execution.durable_execution_arn required")
    if data.get("DurableExecutionName") is not None:
        out["durable_execution_name"] = data["DurableExecutionName"]
    else:
        raise DeserializationError("Execution.durable_execution_name required")
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError("Execution.function_arn required")
    if data.get("Status") is not None:
        import capo_lambda.types.execution_status

        out["status"] = capo_lambda.types.execution_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Execution.status required")
    if data.get("StartTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["start_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    else:
        raise DeserializationError("Execution.start_timestamp required")
    if data.get("EndTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["end_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["EndTimestamp"]
        )
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    return out
