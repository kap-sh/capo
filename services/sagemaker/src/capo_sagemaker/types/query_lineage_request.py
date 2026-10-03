"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryLineageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.direction
    import capo_sagemaker.types.query_filters
    import capo_sagemaker.types.query_lineage_max_depth
    import capo_sagemaker.types.query_lineage_max_results
    import capo_sagemaker.types.query_lineage_start_arns
    import capo_sagemaker.types.string8192


class QueryLineageRequest(TypedDict, closed=True):
    start_arns: NotRequired[
        "capo_sagemaker.types.query_lineage_start_arns.QueryLineageStartArns"
    ]
    """<p>A list of resource Amazon Resource Name (ARN) that represent the starting point for your lineage query.</p>"""
    direction: NotRequired["capo_sagemaker.types.direction.Direction"]
    """<p>Associations between lineage entities have a direction. This parameter determines the direction from the StartArn(s) that the query traverses.</p>"""
    include_edges: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p> Setting this value to <code>True</code> retrieves not only the entities of interest but also the <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html">Associations</a> and lineage entities on the path. Set to <code>False</code> to only return lineage entities that match your query.</p>"""
    filters: NotRequired["capo_sagemaker.types.query_filters.QueryFilters"]
    """<p>A set of filtering parameters that allow you to specify which entities should be returned.</p> <ul> <li> <p>Properties - Key-value pairs to match on the lineage entities' properties.</p> </li> <li> <p>LineageTypes - A set of lineage entity types to match on. For example: <code>TrialComponent</code>, <code>Artifact</code>, or <code>Context</code>.</p> </li> <li> <p>CreatedBefore - Filter entities created before this date.</p> </li> <li> <p>ModifiedBefore - Filter entities modified before this date.</p> </li> <li> <p>ModifiedAfter - Filter entities modified after this date.</p> </li> </ul>"""
    max_depth: NotRequired[
        "capo_sagemaker.types.query_lineage_max_depth.QueryLineageMaxDepth"
    ]
    """<p>The maximum depth in lineage relationships from the <code>StartArns</code> that are traversed. Depth is a measure of the number of <code>Associations</code> from the <code>StartArn</code> entity to the matched results.</p>"""
    max_results: NotRequired[
        "capo_sagemaker.types.query_lineage_max_results.QueryLineageMaxResults"
    ]
    """<p>Limits the number of vertices in the results. Use the <code>NextToken</code> in a response to to retrieve the next page of results.</p>"""
    next_token: NotRequired["capo_sagemaker.types.string8192.String8192"]
    """<p>Limits the number of vertices in the request. Use the <code>NextToken</code> in a response to to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryLineageRequest) -> dict:
    out: dict = {}
    if "start_arns" in value:
        import capo_sagemaker.types.query_lineage_start_arns

        out["StartArns"] = (
            capo_sagemaker.types.query_lineage_start_arns.serialize_aws_json_1_1(
                value["start_arns"]
            )
        )
    if "direction" in value:
        import capo_sagemaker.types.direction

        out["Direction"] = capo_sagemaker.types.direction.serialize_aws_json_1_1(
            value["direction"]
        )
    if "include_edges" in value:
        out["IncludeEdges"] = value["include_edges"]
    if "filters" in value:
        import capo_sagemaker.types.query_filters

        out["Filters"] = capo_sagemaker.types.query_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_depth" in value:
        out["MaxDepth"] = value["max_depth"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryLineageRequest:
    out: QueryLineageRequest = {}  # type: ignore[typeddict-item]
    if data.get("StartArns") is not None:
        import capo_sagemaker.types.query_lineage_start_arns

        out["start_arns"] = (
            capo_sagemaker.types.query_lineage_start_arns.deserialize_aws_json_1_1(
                data["StartArns"]
            )
        )
    if data.get("Direction") is not None:
        import capo_sagemaker.types.direction

        out["direction"] = capo_sagemaker.types.direction.deserialize_aws_json_1_1(
            data["Direction"]
        )
    if data.get("IncludeEdges") is not None:
        out["include_edges"] = data["IncludeEdges"]
    if data.get("Filters") is not None:
        import capo_sagemaker.types.query_filters

        out["filters"] = capo_sagemaker.types.query_filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("MaxDepth") is not None:
        out["max_depth"] = data["MaxDepth"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
