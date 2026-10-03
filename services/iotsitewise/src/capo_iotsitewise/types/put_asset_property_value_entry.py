"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutAssetPropertyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.asset_property_values
    import capo_iotsitewise.types.entry_id
    import capo_iotsitewise.types.id


class PutAssetPropertyValueEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The user specified ID for the entry. You can use this ID to identify which entries failed.</p>"""
    asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset to update.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property for this entry.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    property_values: "capo_iotsitewise.types.asset_property_values.AssetPropertyValues"
    """<p>The list of property values to upload. You can specify up to 10 <code>propertyValues</code> array elements. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetPropertyValueEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    import capo_iotsitewise.types.asset_property_values

    out["propertyValues"] = capo_iotsitewise.types.asset_property_values.serialize_json(
        value["property_values"]
    )
    return out


def deserialize_json(data: dict) -> PutAssetPropertyValueEntry:
    out: PutAssetPropertyValueEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError("PutAssetPropertyValueEntry.entry_id required")
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("propertyValues") is not None:
        import capo_iotsitewise.types.asset_property_values

        out["property_values"] = (
            capo_iotsitewise.types.asset_property_values.deserialize_json(
                data["propertyValues"]
            )
        )
    else:
        raise DeserializationError(
            "PutAssetPropertyValueEntry.property_values required"
        )
    return out
