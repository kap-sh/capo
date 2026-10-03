"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DisassociateAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.custom_id


class DisassociateAssetsRequest(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the parent asset from which to disassociate the child asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    hierarchy_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    child_asset_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the child asset to disassociate. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAssetsRequest) -> dict:
    out: dict = {}
    out["hierarchyId"] = value["hierarchy_id"]
    out["childAssetId"] = value["child_asset_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateAssetsRequest:
    out: DisassociateAssetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("hierarchyId") is not None:
        out["hierarchy_id"] = data["hierarchyId"]
    else:
        raise DeserializationError("DisassociateAssetsRequest.hierarchy_id required")
    if data.get("childAssetId") is not None:
        out["child_asset_id"] = data["childAssetId"]
    else:
        raise DeserializationError("DisassociateAssetsRequest.child_asset_id required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
