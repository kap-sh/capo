"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteAssetModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_version_type
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.select_all


class DeleteAssetModelRequest(TypedDict, closed=True):
    asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model to delete. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    if_match: NotRequired["capo_iotsitewise.types.e_tag.ETag"]
    """<p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    if_none_match: NotRequired["capo_iotsitewise.types.select_all.SelectAll"]
    """<p>Accepts <b>*</b> to reject the delete request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>"""
    match_for_version_type: NotRequired[
        "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
    ]
    """<p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the delete operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetModelRequest:
    out: DeleteAssetModelRequest = {}  # type: ignore[typeddict-item]
    return out
