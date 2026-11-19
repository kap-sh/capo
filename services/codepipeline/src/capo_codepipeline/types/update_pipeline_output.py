"""Generated from Smithy shape ``com.amazonaws.codepipeline#UpdatePipelineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_declaration


class UpdatePipelineOutput(TypedDict, closed=True):
    pipeline: NotRequired[
        "capo_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    ]
    """<p>The structure of the updated pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            capo_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
                value["pipeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineOutput:
    out: UpdatePipelineOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            capo_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = capo_codepipeline.types.pipeline_declaration.serialize_cbor(
            value["pipeline"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdatePipelineOutput:
    out: UpdatePipelineOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = capo_codepipeline.types.pipeline_declaration.deserialize_cbor(
            data["pipeline"]
        )
    return out
