"""Generated from Smithy shape ``com.amazonaws.codepipeline#CreatePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_declaration
    import capo_codepipeline.types.tag_list


class CreatePipelineInput(TypedDict, closed=True):
    pipeline: "capo_codepipeline.types.pipeline_declaration.PipelineDeclaration"
    """<p>Represents the structure of actions and stages to be performed in the pipeline. </p>"""
    tags: NotRequired["capo_codepipeline.types.tag_list.TagList"]
    """<p>The tags for the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.pipeline_declaration

    out["pipeline"] = (
        capo_codepipeline.types.pipeline_declaration.serialize_aws_json_1_1(
            value["pipeline"]
        )
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineInput:
    out: CreatePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = (
            capo_codepipeline.types.pipeline_declaration.deserialize_aws_json_1_1(
                data["pipeline"]
            )
        )
    else:
        raise DeserializationError("CreatePipelineInput.pipeline required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreatePipelineInput) -> dict:
    out: dict = {}
    import capo_codepipeline.types.pipeline_declaration

    out["pipeline"] = capo_codepipeline.types.pipeline_declaration.serialize_cbor(
        value["pipeline"]
    )
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> CreatePipelineInput:
    out: CreatePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_codepipeline.types.pipeline_declaration

        out["pipeline"] = capo_codepipeline.types.pipeline_declaration.deserialize_cbor(
            data["pipeline"]
        )
    else:
        raise DeserializationError("CreatePipelineInput.pipeline required")
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_cbor(data["tags"])
    return out
