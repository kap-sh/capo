"""Generated from Smithy shape ``com.amazonaws.iotevents#IotSiteWiseAssetModelPropertyIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.asset_model_id
    import capo_iot_events.types.asset_property_id


class IotSiteWiseAssetModelPropertyIdentifier(TypedDict, closed=True):
    asset_model_id: "capo_iot_events.types.asset_model_id.AssetModelId"
    """<p> The ID of the AWS IoT SiteWise asset model. </p>"""
    property_id: "capo_iot_events.types.asset_property_id.AssetPropertyId"
    """<p> The ID of the AWS IoT SiteWise asset property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseAssetModelPropertyIdentifier) -> dict:
    out: dict = {}
    out["assetModelId"] = value["asset_model_id"]
    out["propertyId"] = value["property_id"]
    return out


def deserialize_json(data: dict) -> IotSiteWiseAssetModelPropertyIdentifier:
    out: IotSiteWiseAssetModelPropertyIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("assetModelId") is not None:
        out["asset_model_id"] = data["assetModelId"]
    else:
        out["asset_model_id"] = ""
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    else:
        out["property_id"] = ""
    return out
