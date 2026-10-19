"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribePipelinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.pipeline_description_list


class DescribePipelinesOutput(TypedDict, closed=True):
    pipeline_description_list: (
        "capo_data_pipeline.types.pipeline_description_list.PipelineDescriptionList"
    )
    """<p>An array of descriptions for the specified pipelines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelinesOutput) -> dict:
    out: dict = {}
    import capo_data_pipeline.types.pipeline_description_list

    out["pipelineDescriptionList"] = (
        capo_data_pipeline.types.pipeline_description_list.serialize_aws_json_1_1(
            value["pipeline_description_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelinesOutput:
    out: DescribePipelinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineDescriptionList") is not None:
        import capo_data_pipeline.types.pipeline_description_list

        out["pipeline_description_list"] = (
            capo_data_pipeline.types.pipeline_description_list.deserialize_aws_json_1_1(
                data["pipelineDescriptionList"]
            )
        )
    else:
        out["pipeline_description_list"] = []
    return out
