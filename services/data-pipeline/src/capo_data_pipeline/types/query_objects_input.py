"""Generated from Smithy shape ``com.amazonaws.datapipeline#QueryObjectsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.int
    import capo_data_pipeline.types.query
    import capo_data_pipeline.types.string


class QueryObjectsInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    query: NotRequired["capo_data_pipeline.types.query.Query"]
    """<p>The query that defines the objects to be returned. The <code>Query</code> object can contain a maximum of ten selectors. The conditions in the query are limited to top-level String fields in the object. These filters can be applied to components, instances, and attempts.</p>"""
    sphere: "capo_data_pipeline.types.string.string"
    """<p>Indicates whether the query applies to components or instances. The possible values are: <code>COMPONENT</code>, <code>INSTANCE</code>, and <code>ATTEMPT</code>.</p>"""
    marker: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>QueryObjects</code> with the marker value from the previous call to retrieve the next set of results.</p>"""
    limit: NotRequired["capo_data_pipeline.types.int.int"]
    """<p>The maximum number of object names that <code>QueryObjects</code> will return in a single call. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryObjectsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "query" in value:
        import capo_data_pipeline.types.query

        out["query"] = capo_data_pipeline.types.query.serialize_aws_json_1_1(
            value["query"]
        )
    out["sphere"] = value["sphere"]
    if "marker" in value:
        out["marker"] = value["marker"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryObjectsInput:
    out: QueryObjectsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("query") is not None:
        import capo_data_pipeline.types.query

        out["query"] = capo_data_pipeline.types.query.deserialize_aws_json_1_1(
            data["query"]
        )
    if data.get("sphere") is not None:
        out["sphere"] = data["sphere"]
    else:
        out["sphere"] = ""
    if data.get("marker") is not None:
        out["marker"] = data["marker"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
