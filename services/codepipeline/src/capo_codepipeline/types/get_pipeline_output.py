"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_declaration
    import capo_codepipeline.types.pipeline_metadata


class GetPipelineOutput(TypedDict, closed=True):
    pipeline: NotRequired[
        "capo_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    ]
    """<p>Represents the structure of actions and stages to be performed in the pipeline. </p>"""
    metadata: NotRequired["capo_codepipeline.types.pipeline_metadata.PipelineMetadata"]
    """<p>Represents the pipeline metadata information returned as part of the output of a <code>GetPipeline</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            capo_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
                value["pipeline"]
            )
        )
    if "metadata" in value:
        import capo_codepipeline.types.pipeline_metadata

        out["metadata"] = (
            capo_codepipeline.types.pipeline_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineOutput:
    out: GetPipelineOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            capo_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    if data.get("metadata") is not None:
        import capo_codepipeline.types.pipeline_metadata

        out["metadata"] = (
            capo_codepipeline.types.pipeline_metadata.deserialize_aws_json_1_1(
                data["metadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetPipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = capo_codepipeline.types.pipeline_declaration.serialize_cbor(
            value["pipeline"]
        )
    if "metadata" in value:
        import capo_codepipeline.types.pipeline_metadata

        out["metadata"] = capo_codepipeline.types.pipeline_metadata.serialize_cbor(
            value["metadata"]
        )
    return out


def deserialize_cbor(data: dict) -> GetPipelineOutput:
    out: GetPipelineOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = capo_codepipeline.types.pipeline_declaration.deserialize_cbor(
            data["pipeline"]
        )
    if data.get("metadata") is not None:
        import capo_codepipeline.types.pipeline_metadata

        out["metadata"] = capo_codepipeline.types.pipeline_metadata.deserialize_cbor(
            data["metadata"]
        )
    return out
