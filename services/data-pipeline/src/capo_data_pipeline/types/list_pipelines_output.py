"""Generated from Smithy shape ``com.amazonaws.datapipeline#ListPipelinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.boolean
    import capo_data_pipeline.types.pipeline_list
    import capo_data_pipeline.types.string


class ListPipelinesOutput(TypedDict, closed=True):
    pipeline_id_list: "capo_data_pipeline.types.pipeline_list.pipelineList"
    """<p>The pipeline identifiers. If you require additional information about the pipelines, you can use these identifiers to call <a>DescribePipelines</a> and <a>GetPipelineDefinition</a>.</p>"""
    marker: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The starting point for the next page of results. To view the next page of results, call <code>ListPipelinesOutput</code> again with this marker value. If the value is null, there are no more results.</p>"""
    has_more_results: "capo_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether there are more results that can be obtained by a subsequent call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesOutput) -> dict:
    out: dict = {}
    import capo_data_pipeline.types.pipeline_list

    out["pipelineIdList"] = (
        capo_data_pipeline.types.pipeline_list.serialize_aws_json_1_1(
            value["pipeline_id_list"]
        )
    )
    if "marker" in value:
        out["marker"] = value["marker"]
    out["hasMoreResults"] = value.get("has_more_results", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesOutput:
    out: ListPipelinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineIdList") is not None:
        import capo_data_pipeline.types.pipeline_list

        out["pipeline_id_list"] = (
            capo_data_pipeline.types.pipeline_list.deserialize_aws_json_1_1(
                data["pipelineIdList"]
            )
        )
    else:
        out["pipeline_id_list"] = []
    if data.get("marker") is not None:
        out["marker"] = data["marker"]
    if data.get("hasMoreResults") is not None:
        out["has_more_results"] = data["hasMoreResults"]
    else:
        out["has_more_results"] = False
    return out
