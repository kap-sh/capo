"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.pipeline_managed_by
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.sort_pipelines_by
    import capo_sagemaker.types.timestamp


class ListPipelinesRequest(TypedDict, closed=True):
    pipeline_name_prefix: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The prefix of the pipeline name.</p>"""
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipelines that were created after a specified time.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipelines that were created before a specified time.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.sort_pipelines_by.SortPipelinesBy"]
    """<p>The field by which to sort results. The default is <code>CreatedTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelines</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipelines, use the token in the next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of pipelines to return in the response.</p>"""
    managed_by: NotRequired[
        "capo_sagemaker.types.pipeline_managed_by.PipelineManagedBy"
    ]
    """<p>Filters the pipelines by who manages them. Specify <code>AWS</code> to return pipelines that AWS manages, or <code>CUSTOMER</code> to return pipelines that you created. If you don't specify a value, the response includes both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesRequest) -> dict:
    out: dict = {}
    if "pipeline_name_prefix" in value:
        out["PipelineNamePrefix"] = value["pipeline_name_prefix"]
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
        import capo_sagemaker.types.sort_pipelines_by

        out["SortBy"] = capo_sagemaker.types.sort_pipelines_by.serialize_aws_json_1_1(
            value["sort_by"]
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
    if "managed_by" in value:
        import capo_sagemaker.types.pipeline_managed_by

        out["ManagedBy"] = (
            capo_sagemaker.types.pipeline_managed_by.serialize_aws_json_1_1(
                value["managed_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesRequest:
    out: ListPipelinesRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineNamePrefix") is not None:
        out["pipeline_name_prefix"] = data["PipelineNamePrefix"]
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
        import capo_sagemaker.types.sort_pipelines_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_pipelines_by.deserialize_aws_json_1_1(
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
    if data.get("ManagedBy") is not None:
        import capo_sagemaker.types.pipeline_managed_by

        out["managed_by"] = (
            capo_sagemaker.types.pipeline_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    return out
