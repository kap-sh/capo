"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_path
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.property_notification
    import capo_iotsitewise.types.property_unit


class AssetPropertySummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the property.</p>"""
    external_id: NotRequired["capo_iotsitewise.types.external_id.ExternalId"]
    """<p>The external ID of the property. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    alias: NotRequired["capo_iotsitewise.types.property_alias.PropertyAlias"]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    unit: NotRequired["capo_iotsitewise.types.property_unit.PropertyUnit"]
    """<p> The unit of measure (such as Newtons or RPM) of the asset property. </p>"""
    notification: NotRequired[
        "capo_iotsitewise.types.property_notification.PropertyNotification"
    ]
    asset_composite_model_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p> The ID of the composite model that contains the asset property. </p>"""
    path: NotRequired["capo_iotsitewise.types.asset_property_path.AssetPropertyPath"]
    """<p>The structured path to the property from the root of the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "notification" in value:
        import capo_iotsitewise.types.property_notification

        out["notification"] = (
            capo_iotsitewise.types.property_notification.serialize_json(
                value["notification"]
            )
        )
    if "asset_composite_model_id" in value:
        out["assetCompositeModelId"] = value["asset_composite_model_id"]
    if "path" in value:
        import capo_iotsitewise.types.asset_property_path

        out["path"] = capo_iotsitewise.types.asset_property_path.serialize_json(
            value["path"]
        )
    return out


def deserialize_json(data: dict) -> AssetPropertySummary:
    out: AssetPropertySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssetPropertySummary.id required")
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("notification") is not None:
        import capo_iotsitewise.types.property_notification

        out["notification"] = (
            capo_iotsitewise.types.property_notification.deserialize_json(
                data["notification"]
            )
        )
    if data.get("assetCompositeModelId") is not None:
        out["asset_composite_model_id"] = data["assetCompositeModelId"]
    if data.get("path") is not None:
        import capo_iotsitewise.types.asset_property_path

        out["path"] = capo_iotsitewise.types.asset_property_path.deserialize_json(
            data["path"]
        )
    return out
