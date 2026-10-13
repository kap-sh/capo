"""Generated from Smithy shape ``com.amazonaws.pipes#SageMakerPipelineParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.sage_maker_pipeline_parameter

SageMakerPipelineParameterList: TypeAlias = list[
    "capo_pipes.types.sage_maker_pipeline_parameter.SageMakerPipelineParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameterList) -> list:
    import capo_pipes.types.sage_maker_pipeline_parameter

    out: list = []
    for item in value:
        out.append(capo_pipes.types.sage_maker_pipeline_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SageMakerPipelineParameterList:
    import capo_pipes.types.sage_maker_pipeline_parameter

    out: SageMakerPipelineParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pipes.types.sage_maker_pipeline_parameter.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SageMakerPipelineParameterList) -> list[Any]:
    import capo_pipes.types.sage_maker_pipeline_parameter

    return [
        capo_pipes.types.sage_maker_pipeline_parameter.redact_sensitive(item)
        for item in value
    ]
