"""Generated from Smithy shape ``com.amazonaws.datapipeline#ActivatePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.parameter_value_list
    import capo_data_pipeline.types.timestamp


class ActivatePipelineInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    parameter_values: NotRequired[
        "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
    ]
    """<p>A list of parameter values to pass to the pipeline at activation.</p>"""
    start_timestamp: NotRequired["capo_data_pipeline.types.timestamp.timestamp"]
    """<p>The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivatePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "parameter_values" in value:
        import capo_data_pipeline.types.parameter_value_list

        out["parameterValues"] = (
            capo_data_pipeline.types.parameter_value_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    if "start_timestamp" in value:
        import capo_data_pipeline.types.timestamp

        out["startTimestamp"] = (
            capo_data_pipeline.types.timestamp.serialize_aws_json_1_1(
                value["start_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivatePipelineInput:
    out: ActivatePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("parameterValues") is not None:
        import capo_data_pipeline.types.parameter_value_list

        out["parameter_values"] = (
            capo_data_pipeline.types.parameter_value_list.deserialize_aws_json_1_1(
                data["parameterValues"]
            )
        )
    if data.get("startTimestamp") is not None:
        import capo_data_pipeline.types.timestamp

        out["start_timestamp"] = (
            capo_data_pipeline.types.timestamp.deserialize_aws_json_1_1(
                data["startTimestamp"]
            )
        )
    return out
