"""Generated from Smithy shape ``com.amazonaws.datapipeline#PutPipelineDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.parameter_object_list
    import capo_data_pipeline.types.parameter_value_list
    import capo_data_pipeline.types.pipeline_object_list


class PutPipelineDefinitionInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    pipeline_objects: "capo_data_pipeline.types.pipeline_object_list.PipelineObjectList"
    """<p>The objects that define the pipeline. These objects overwrite the existing pipeline definition.</p>"""
    parameter_objects: NotRequired[
        "capo_data_pipeline.types.parameter_object_list.ParameterObjectList"
    ]
    """<p>The parameter objects used with the pipeline.</p>"""
    parameter_values: NotRequired[
        "capo_data_pipeline.types.parameter_value_list.ParameterValueList"
    ]
    """<p>The parameter values used with the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPipelineDefinitionInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import capo_data_pipeline.types.pipeline_object_list

    out["pipelineObjects"] = (
        capo_data_pipeline.types.pipeline_object_list.serialize_aws_json_1_1(
            value["pipeline_objects"]
        )
    )
    if "parameter_objects" in value:
        import capo_data_pipeline.types.parameter_object_list

        out["parameterObjects"] = (
            capo_data_pipeline.types.parameter_object_list.serialize_aws_json_1_1(
                value["parameter_objects"]
            )
        )
    if "parameter_values" in value:
        import capo_data_pipeline.types.parameter_value_list

        out["parameterValues"] = (
            capo_data_pipeline.types.parameter_value_list.serialize_aws_json_1_1(
                value["parameter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPipelineDefinitionInput:
    out: PutPipelineDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("pipelineObjects") is not None:
        import capo_data_pipeline.types.pipeline_object_list

        out["pipeline_objects"] = (
            capo_data_pipeline.types.pipeline_object_list.deserialize_aws_json_1_1(
                data["pipelineObjects"]
            )
        )
    else:
        out["pipeline_objects"] = []
    if data.get("parameterObjects") is not None:
        import capo_data_pipeline.types.parameter_object_list

        out["parameter_objects"] = (
            capo_data_pipeline.types.parameter_object_list.deserialize_aws_json_1_1(
                data["parameterObjects"]
            )
        )
    if data.get("parameterValues") is not None:
        import capo_data_pipeline.types.parameter_value_list

        out["parameter_values"] = (
            capo_data_pipeline.types.parameter_value_list.deserialize_aws_json_1_1(
                data["parameterValues"]
            )
        )
    return out
