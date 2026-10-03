"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.entry_id
    import capo_iotsitewise.types.id


class BatchGetAssetPropertyValueEntry(TypedDict, closed=True):
    entry_id: "capo_iotsitewise.types.entry_id.EntryId"
    """<p>The ID of the entry.</p>"""
    asset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset in which the asset property was created.</p>"""
    property_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the asset property, in UUID format.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyValueEntry:
    out: BatchGetAssetPropertyValueEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError("BatchGetAssetPropertyValueEntry.entry_id required")
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    return out
