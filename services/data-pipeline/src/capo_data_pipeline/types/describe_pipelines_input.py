"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribePipelinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id_list


class DescribePipelinesInput(TypedDict, closed=True):
    pipeline_ids: "capo_data_pipeline.types.id_list.idList"
    """<p>The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call <a>ListPipelines</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelinesInput) -> dict:
    out: dict = {}
    import capo_data_pipeline.types.id_list

    out["pipelineIds"] = capo_data_pipeline.types.id_list.serialize_aws_json_1_1(
        value["pipeline_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelinesInput:
    out: DescribePipelinesInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineIds") is not None:
        import capo_data_pipeline.types.id_list

        out["pipeline_ids"] = capo_data_pipeline.types.id_list.deserialize_aws_json_1_1(
            data["pipelineIds"]
        )
    else:
        out["pipeline_ids"] = []
    return out
