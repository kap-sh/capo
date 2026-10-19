"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchExecuteStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.parti_ql_batch_request
    import capo_dynamodb.types.return_consumed_capacity


class BatchExecuteStatementInput(TypedDict, closed=True):
    statements: "capo_dynamodb.types.parti_ql_batch_request.PartiQLBatchRequest"
    """<p>The list of PartiQL statements representing the batch to run.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchExecuteStatementInput) -> dict:
    out: dict = {}
    import capo_dynamodb.types.parti_ql_batch_request

    out["Statements"] = (
        capo_dynamodb.types.parti_ql_batch_request.serialize_aws_json_1_0(
            value["statements"]
        )
    )
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchExecuteStatementInput:
    out: BatchExecuteStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("Statements") is not None:
        import capo_dynamodb.types.parti_ql_batch_request

        out["statements"] = (
            capo_dynamodb.types.parti_ql_batch_request.deserialize_aws_json_1_0(
                data["Statements"]
            )
        )
    else:
        out["statements"] = []
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    return out
