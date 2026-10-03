"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CancelImageCreationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_build_version_arn


class CancelImageCreationRequest(TypedDict, closed=True):
    image_build_version_arn: (
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the image that you want to cancel creation for.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelImageCreationRequest) -> dict:
    out: dict = {}
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelImageCreationRequest:
    out: CancelImageCreationRequest = {}  # type: ignore[typeddict-item]
    if data.get("imageBuildVersionArn") is not None:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError(
            "CancelImageCreationRequest.image_build_version_arn required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CancelImageCreationRequest.client_token required")
    return out
