"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetSageMakerPipelineParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.sage_maker_pipeline_parameter_list


class PipeTargetSageMakerPipelineParameters(TypedDict, closed=True):
    pipeline_parameter_list: NotRequired[
        "capo_pipes.types.sage_maker_pipeline_parameter_list.SageMakerPipelineParameterList"
    ]
    """<p>List of Parameter names and values for SageMaker Model Building Pipeline execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetSageMakerPipelineParameters) -> dict:
    out: dict = {}
    if "pipeline_parameter_list" in value:
        import capo_pipes.types.sage_maker_pipeline_parameter_list

        out["PipelineParameterList"] = (
            capo_pipes.types.sage_maker_pipeline_parameter_list.serialize_json(
                value["pipeline_parameter_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeTargetSageMakerPipelineParameters:
    out: PipeTargetSageMakerPipelineParameters = {}  # type: ignore[typeddict-item]
    if data.get("PipelineParameterList") is not None:
        import capo_pipes.types.sage_maker_pipeline_parameter_list

        out["pipeline_parameter_list"] = (
            capo_pipes.types.sage_maker_pipeline_parameter_list.deserialize_json(
                data["PipelineParameterList"]
            )
        )
    return out


def redact_sensitive(value: PipeTargetSageMakerPipelineParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pipeline_parameter_list" in value:
        import capo_pipes.types.sage_maker_pipeline_parameter_list

        out["pipeline_parameter_list"] = (
            capo_pipes.types.sage_maker_pipeline_parameter_list.redact_sensitive(
                value["pipeline_parameter_list"]
            )
        )
    return out
