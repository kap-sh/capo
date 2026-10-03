"""Generated from Smithy shape ``com.amazonaws.imagebuilder#StartImagePipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.tag_map


class StartImagePipelineExecutionRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline that you want to manually invoke.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags for Image Builder to apply to the image resource that's created when pipeline execution starts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImagePipelineExecutionRequest) -> dict:
    out: dict = {}
    out["imagePipelineArn"] = value["image_pipeline_arn"]
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartImagePipelineExecutionRequest:
    out: StartImagePipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("imagePipelineArn") is not None:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    else:
        raise DeserializationError(
            "StartImagePipelineExecutionRequest.image_pipeline_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "StartImagePipelineExecutionRequest.client_token required"
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
