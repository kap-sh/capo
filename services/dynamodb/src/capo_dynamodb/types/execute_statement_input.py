"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExecuteStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.parti_ql_next_token
    import capo_dynamodb.types.parti_ql_statement
    import capo_dynamodb.types.positive_integer_object
    import capo_dynamodb.types.prepared_statement_parameters
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.return_values_on_condition_check_failure


class ExecuteStatementInput(TypedDict, closed=True):
    statement: "capo_dynamodb.types.parti_ql_statement.PartiQLStatement"
    """<p>The PartiQL statement representing the operation to run.</p>"""
    parameters: NotRequired[
        "capo_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
    ]
    """<p>The parameters for the PartiQL statement, if any.</p>"""
    consistent_read: NotRequired["capo_dynamodb.types.consistent_read.ConsistentRead"]
    """<p>The consistency of a read operation. If set to <code>true</code>, then a strongly consistent read is used; otherwise, an eventually consistent read is used.</p>"""
    next_token: NotRequired["capo_dynamodb.types.parti_ql_next_token.PartiQLNextToken"]
    """<p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    limit: NotRequired[
        "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, along with a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation so you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. </p>"""
    return_values_on_condition_check_failure: NotRequired[
        "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for an <code>ExecuteStatement</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteStatementInput) -> dict:
    out: dict = {}
    out["Statement"] = value["statement"]
    if "parameters" in value:
        import capo_dynamodb.types.prepared_statement_parameters

        out["Parameters"] = (
            capo_dynamodb.types.prepared_statement_parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "return_values_on_condition_check_failure" in value:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteStatementInput:
    out: ExecuteStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("Statement") is not None:
        out["statement"] = data["Statement"]
    else:
        out["statement"] = ""
    if data.get("Parameters") is not None:
        import capo_dynamodb.types.prepared_statement_parameters

        out["parameters"] = (
            capo_dynamodb.types.prepared_statement_parameters.deserialize_aws_json_1_0(
                data["Parameters"]
            )
        )
    if data.get("ConsistentRead") is not None:
        out["consistent_read"] = data["ConsistentRead"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("ReturnValuesOnConditionCheckFailure") is not None:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
