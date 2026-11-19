"""Generated from Smithy shape ``com.amazonaws.lambda#RemoveLayerVersionPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.layer_name_or_arn
    import capo_lambda.types.layer_version_number
    import capo_lambda.types.statement_id
    import capo_lambda.types.string


class RemoveLayerVersionPermissionRequest(TypedDict, closed=True):
    layer_name: "capo_lambda.types.layer_name_or_arn.LayerNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    version_number: "capo_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""
    statement_id: "capo_lambda.types.statement_id.StatementId"
    """<p>The identifier that was specified when the statement was added.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveLayerVersionPermissionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveLayerVersionPermissionRequest:
    out: RemoveLayerVersionPermissionRequest = {}  # type: ignore[typeddict-item]
    return out
