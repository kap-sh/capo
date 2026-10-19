"""Generated from Smithy shape ``com.amazonaws.dynamodb#ParameterizedStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.parti_ql_statement
    import capo_dynamodb.types.prepared_statement_parameters
    import capo_dynamodb.types.return_values_on_condition_check_failure


class ParameterizedStatement(TypedDict, closed=True):
    statement: "capo_dynamodb.types.parti_ql_statement.PartiQLStatement"
    """<p> A PartiQL statement that uses parameters. </p>"""
    parameters: NotRequired[
        "capo_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
    ]
    """<p> The parameter values. </p>"""
    return_values_on_condition_check_failure: NotRequired[
        "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>An optional parameter that returns the item attributes for a PartiQL <code>ParameterizedStatement</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterizedStatement) -> dict:
    out: dict = {}
    out["Statement"] = value["statement"]
    if "parameters" in value:
        import capo_dynamodb.types.prepared_statement_parameters

        out["Parameters"] = (
            capo_dynamodb.types.prepared_statement_parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "return_values_on_condition_check_failure" in value:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ParameterizedStatement:
    out: ParameterizedStatement = {}  # type: ignore[typeddict-item]
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
    if data.get("ReturnValuesOnConditionCheckFailure") is not None:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
