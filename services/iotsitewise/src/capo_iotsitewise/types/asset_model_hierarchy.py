"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelHierarchy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.name


class AssetModelHierarchy(TypedDict, closed=True):
    id: NotRequired["capo_iotsitewise.types.custom_id.CustomID"]
    """<p>The ID of the asset model hierarchy. This ID is a <code>hierarchyId</code>.</p> <ul> <li> <p>If you are callling <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> to create a <i>new</i> hierarchy: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p> </li> <li> <p>If you are calling UpdateAssetModel to modify an <i>existing</i> hierarchy: This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p> </li> </ul>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID (if any) provided in the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html">CreateAssetModel</a> or <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> operation. You can assign an external ID by specifying this value as part of a call to <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a>. However, you can't change the external ID if one is already assigned. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the asset model hierarchy that you specify by using the <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html">CreateAssetModel</a> or <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a> API operation.</p>"""
    child_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model, in UUID format. All assets in this hierarchy must be instances of the <code>childAssetModelId</code> asset model. IoT SiteWise will always return the actual asset model ID for this value. However, when you are specifying this value as part of a call to <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html">UpdateAssetModel</a>, you may provide either the asset model ID or else <code>externalId:</code> followed by the asset model's external ID. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelHierarchy) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["name"] = value["name"]
    out["childAssetModelId"] = value["child_asset_model_id"]
    return out


def deserialize_json(data: dict) -> AssetModelHierarchy:
    out: AssetModelHierarchy = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetModelHierarchy.name required")
    if data.get("childAssetModelId") is not None:
        out["child_asset_model_id"] = data["childAssetModelId"]
    else:
        raise DeserializationError("AssetModelHierarchy.child_asset_model_id required")
    return out
