"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteTransactionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.client_request_token
    import capo_dynamodb.types.parameterized_statements
    import capo_dynamodb.types.return_consumed_capacity


class ExecuteTransactionInput(TypedDict, closed=True):
    transact_statements: (
        "capo_dynamodb.types.parameterized_statements.ParameterizedStatements"
    )
    """<p>The list of PartiQL statements representing the transaction to run.</p>"""
    client_request_token: NotRequired[
        "capo_dynamodb.types.client_request_token.ClientRequestToken"
    ]
    """<p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    """<p>Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html">TransactGetItems</a> and <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html">TransactWriteItems</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteTransactionInput) -> dict:
    out: dict = {}
    import capo_dynamodb.types.parameterized_statements

    out["TransactStatements"] = (
        capo_dynamodb.types.parameterized_statements.serialize_aws_json_1_0(
            value["transact_statements"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteTransactionInput:
    out: ExecuteTransactionInput = {}  # type: ignore[typeddict-item]
    if data.get("TransactStatements") is not None:
        import capo_dynamodb.types.parameterized_statements

        out["transact_statements"] = (
            capo_dynamodb.types.parameterized_statements.deserialize_aws_json_1_0(
                data["TransactStatements"]
            )
        )
    else:
        raise DeserializationError(
            "ExecuteTransactionInput.transact_statements required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    return out
