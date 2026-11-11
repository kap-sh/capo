"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineVersionAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_version_alias

PipelineVersionAliasList: TypeAlias = list[
    "capo_sagemaker.types.pipeline_version_alias.PipelineVersionAlias"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersionAliasList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PipelineVersionAliasList:
    return [item for item in data if item is not None]
