"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAssociationExecutionTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_id
    import capo_ssm.types.association_execution_targets_filter_list
    import capo_ssm.types.association_id
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class DescribeAssociationExecutionTargetsRequest(TypedDict, closed=True):
    association_id: "capo_ssm.types.association_id.AssociationId"
    """<p>The association ID that includes the execution for which you want to view details.</p>"""
    execution_id: "capo_ssm.types.association_execution_id.AssociationExecutionId"
    """<p>The execution ID for which you want to view details.</p>"""
    filters: NotRequired[
        "capo_ssm.types.association_execution_targets_filter_list.AssociationExecutionTargetsFilterList"
    ]
    """<p>Filters for the request. You can specify the following filters and values.</p> <p>Status (EQUAL)</p> <p>ResourceId (EQUAL)</p> <p>ResourceType (EQUAL)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAssociationExecutionTargetsRequest) -> dict:
    out: dict = {}
    out["AssociationId"] = value["association_id"]
    out["ExecutionId"] = value["execution_id"]
    if "filters" in value:
        import capo_ssm.types.association_execution_targets_filter_list

        out["Filters"] = (
            capo_ssm.types.association_execution_targets_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAssociationExecutionTargetsRequest:
    out: DescribeAssociationExecutionTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    else:
        out["association_id"] = ""
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    else:
        out["execution_id"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.association_execution_targets_filter_list

        out["filters"] = (
            capo_ssm.types.association_execution_targets_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
