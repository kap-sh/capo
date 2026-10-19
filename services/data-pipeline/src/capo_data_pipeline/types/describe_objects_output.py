"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribeObjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.boolean
    import capo_data_pipeline.types.pipeline_object_list
    import capo_data_pipeline.types.string


class DescribeObjectsOutput(TypedDict, closed=True):
    pipeline_objects: "capo_data_pipeline.types.pipeline_object_list.PipelineObjectList"
    """<p>An array of object definitions.</p>"""
    marker: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The starting point for the next page of results. To view the next page of results, call <code>DescribeObjects</code> again with this marker value. If the value is null, there are no more results.</p>"""
    has_more_results: "capo_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether there are more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeObjectsOutput) -> dict:
    out: dict = {}
    import capo_data_pipeline.types.pipeline_object_list

    out["pipelineObjects"] = (
        capo_data_pipeline.types.pipeline_object_list.serialize_aws_json_1_1(
            value["pipeline_objects"]
        )
    )
    if "marker" in value:
        out["marker"] = value["marker"]
    out["hasMoreResults"] = value.get("has_more_results", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeObjectsOutput:
    out: DescribeObjectsOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineObjects") is not None:
        import capo_data_pipeline.types.pipeline_object_list

        out["pipeline_objects"] = (
            capo_data_pipeline.types.pipeline_object_list.deserialize_aws_json_1_1(
                data["pipelineObjects"]
            )
        )
    else:
        out["pipeline_objects"] = []
    if data.get("marker") is not None:
        out["marker"] = data["marker"]
    if data.get("hasMoreResults") is not None:
        out["has_more_results"] = data["hasMoreResults"]
    else:
        out["has_more_results"] = False
    return out
