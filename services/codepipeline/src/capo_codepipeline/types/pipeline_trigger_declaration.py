"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineTriggerDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.git_configuration
    import capo_codepipeline.types.pipeline_trigger_provider_type


class PipelineTriggerDeclaration(TypedDict, closed=True):
    provider_type: "capo_codepipeline.types.pipeline_trigger_provider_type.PipelineTriggerProviderType"
    """<p>The source provider for the event, such as connections configured for a repository with Git tags, for the specified trigger configuration.</p>"""
    git_configuration: "capo_codepipeline.types.git_configuration.GitConfiguration"
    """<p>Provides the filter criteria and the source stage for the repository event that starts the pipeline, such as Git tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineTriggerDeclaration) -> dict:
    out: dict = {}
    import capo_codepipeline.types.pipeline_trigger_provider_type

    out["providerType"] = (
        capo_codepipeline.types.pipeline_trigger_provider_type.serialize_aws_json_1_1(
            value["provider_type"]
        )
    )
    import capo_codepipeline.types.git_configuration

    out["gitConfiguration"] = (
        capo_codepipeline.types.git_configuration.serialize_aws_json_1_1(
            value["git_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineTriggerDeclaration:
    out: PipelineTriggerDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("providerType") is not None:
        import capo_codepipeline.types.pipeline_trigger_provider_type

        out["provider_type"] = (
            capo_codepipeline.types.pipeline_trigger_provider_type.deserialize_aws_json_1_1(
                data["providerType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_codepipeline.types.pipeline_trigger_provider_type.PipelineTriggerProviderType",
            "",
        )
    if data.get("gitConfiguration") is not None:
        import capo_codepipeline.types.git_configuration

        out["git_configuration"] = (
            capo_codepipeline.types.git_configuration.deserialize_aws_json_1_1(
                data["gitConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PipelineTriggerDeclaration.git_configuration required"
        )
    return out
