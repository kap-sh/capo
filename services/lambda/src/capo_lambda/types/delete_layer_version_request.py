"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteLayerVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.layer_name_or_arn
    import capo_lambda.types.layer_version_number


class DeleteLayerVersionRequest(TypedDict, closed=True):
    layer_name: "capo_lambda.types.layer_name_or_arn.LayerNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLayerVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLayerVersionRequest:
    out: DeleteLayerVersionRequest = {}  # type: ignore[typeddict-item]
    return out
