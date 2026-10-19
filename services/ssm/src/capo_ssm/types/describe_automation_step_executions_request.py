"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAutomationStepExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.boolean
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.step_execution_filter_list


class DescribeAutomationStepExecutionsRequest(TypedDict, closed=True):
    automation_execution_id: (
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The Automation execution ID for which you want step execution descriptions.</p>"""
    filters: NotRequired[
        "capo_ssm.types.step_execution_filter_list.StepExecutionFilterList"
    ]
    """<p>One or more filters to limit the number of step executions returned by the request.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    reverse_order: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>Indicates whether to list step executions in reverse order by start time. The default value is 'false'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutomationStepExecutionsRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    if "filters" in value:
        import capo_ssm.types.step_execution_filter_list

        out["Filters"] = (
            capo_ssm.types.step_execution_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "reverse_order" in value:
        out["ReverseOrder"] = value["reverse_order"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutomationStepExecutionsRequest:
    out: DescribeAutomationStepExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        out["automation_execution_id"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.step_execution_filter_list

        out["filters"] = (
            capo_ssm.types.step_execution_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ReverseOrder") is not None:
        out["reverse_order"] = data["ReverseOrder"]
    return out
