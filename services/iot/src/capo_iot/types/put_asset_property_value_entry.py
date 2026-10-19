"""Generated from Smithy shape ``com.amazonaws.iot#PutAssetPropertyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.asset_id
    import capo_iot.types.asset_property_alias
    import capo_iot.types.asset_property_entry_id
    import capo_iot.types.asset_property_id
    import capo_iot.types.asset_property_value_list


class PutAssetPropertyValueEntry(TypedDict, closed=True):
    entry_id: NotRequired["capo_iot.types.asset_property_entry_id.AssetPropertyEntryId"]
    """<p>Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.</p>"""
    asset_id: NotRequired["capo_iot.types.asset_id.AssetId"]
    """<p>The ID of the IoT SiteWise asset. You must specify either a <code>propertyAlias</code> or both an <code>aliasId</code> and a <code>propertyId</code>. Accepts substitution templates.</p>"""
    property_id: NotRequired["capo_iot.types.asset_property_id.AssetPropertyId"]
    """<p>The ID of the asset's property. You must specify either a <code>propertyAlias</code> or both an <code>aliasId</code> and a <code>propertyId</code>. Accepts substitution templates.</p>"""
    property_alias: NotRequired[
        "capo_iot.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The name of the property alias associated with your asset property. You must specify either a <code>propertyAlias</code> or both an <code>aliasId</code> and a <code>propertyId</code>. Accepts substitution templates.</p>"""
    property_values: "capo_iot.types.asset_property_value_list.AssetPropertyValueList"
    """<p>A list of property values to insert that each contain timestamp, quality, and value (TQV) information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetPropertyValueEntry) -> dict:
    out: dict = {}
    if "entry_id" in value:
        out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    import capo_iot.types.asset_property_value_list

    out["propertyValues"] = capo_iot.types.asset_property_value_list.serialize_json(
        value["property_values"]
    )
    return out


def deserialize_json(data: dict) -> PutAssetPropertyValueEntry:
    out: PutAssetPropertyValueEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("propertyValues") is not None:
        import capo_iot.types.asset_property_value_list

        out["property_values"] = (
            capo_iot.types.asset_property_value_list.deserialize_json(
                data["propertyValues"]
            )
        )
    else:
        out["property_values"] = []
    return out
