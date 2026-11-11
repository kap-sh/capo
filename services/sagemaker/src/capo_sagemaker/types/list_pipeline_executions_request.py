"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.pipeline_name_or_arn
    import capo_sagemaker.types.pipeline_version_alias
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.sort_pipeline_executions_by
    import capo_sagemaker.types.timestamp


class ListPipelineExecutionsRequest(TypedDict, closed=True):
    pipeline_name: NotRequired[
        "capo_sagemaker.types.pipeline_name_or_arn.PipelineNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the pipeline.</p>"""
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipeline executions that were created after a specified time.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipeline executions that were created before a specified time.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.sort_pipeline_executions_by.SortPipelineExecutionsBy"
    ]
    """<p>The field by which to sort results. The default is <code>CreatedTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineExecutions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipeline executions, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of pipeline executions to return in the response.</p>"""
    pipeline_version_alias: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias.PipelineVersionAlias"
    ]
    """<p>The alias of a pipeline version. The response includes only the executions of the version that has this alias when you make the request. If no version of the pipeline has this alias, the request fails with a <code>ResourceNotFound</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionsRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import capo_sagemaker.types.sort_pipeline_executions_by

        out["SortBy"] = (
            capo_sagemaker.types.sort_pipeline_executions_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "pipeline_version_alias" in value:
        out["PipelineVersionAlias"] = value["pipeline_version_alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionsRequest:
    out: ListPipelineExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    if data.get("CreatedAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if data.get("CreatedBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.sort_pipeline_executions_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_pipeline_executions_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("PipelineVersionAlias") is not None:
        out["pipeline_version_alias"] = data["PipelineVersionAlias"]
    return out
