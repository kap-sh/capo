"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregate_types
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.entry_id
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.qualities
    import capo_iotsitewise.types.resolution
    import capo_iotsitewise.types.time_ordering
    import capo_iotsitewise.types.timestamp


class BatchGetAssetPropertyAggregatesEntry(TypedDict, closed=True):
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
    aggregate_types: "capo_iotsitewise.types.aggregate_types.AggregateTypes"
    """<p>The data aggregating function.</p>"""
    resolution: "capo_iotsitewise.types.resolution.Resolution"
    """<p>The time interval over which to aggregate data.</p>"""
    start_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    end_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>"""
    qualities: NotRequired["capo_iotsitewise.types.qualities.Qualities"]
    """<p>The quality by which to filter asset data.</p>"""
    time_ordering: NotRequired["capo_iotsitewise.types.time_ordering.TimeOrdering"]
    """<p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesEntry) -> dict:
    out: dict = {}
    out["entryId"] = value["entry_id"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "property_id" in value:
        out["propertyId"] = value["property_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    import capo_iotsitewise.types.aggregate_types

    out["aggregateTypes"] = capo_iotsitewise.types.aggregate_types.serialize_json(
        value["aggregate_types"]
    )
    out["resolution"] = value["resolution"]
    import capo_iotsitewise.types.timestamp

    out["startDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["start_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["endDate"] = capo_iotsitewise.types.timestamp.serialize_json(value["end_date"])
    if "qualities" in value:
        import capo_iotsitewise.types.qualities

        out["qualities"] = capo_iotsitewise.types.qualities.serialize_json(
            value["qualities"]
        )
    if "time_ordering" in value:
        import capo_iotsitewise.types.time_ordering

        out["timeOrdering"] = capo_iotsitewise.types.time_ordering.serialize_json(
            value["time_ordering"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAssetPropertyAggregatesEntry:
    out: BatchGetAssetPropertyAggregatesEntry = {}  # type: ignore[typeddict-item]
    if data.get("entryId") is not None:
        out["entry_id"] = data["entryId"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesEntry.entry_id required"
        )
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    if data.get("propertyId") is not None:
        out["property_id"] = data["propertyId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("aggregateTypes") is not None:
        import capo_iotsitewise.types.aggregate_types

        out["aggregate_types"] = (
            capo_iotsitewise.types.aggregate_types.deserialize_json(
                data["aggregateTypes"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesEntry.aggregate_types required"
        )
    if data.get("resolution") is not None:
        out["resolution"] = data["resolution"]
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesEntry.resolution required"
        )
    if data.get("startDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["start_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["startDate"]
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesEntry.start_date required"
        )
    if data.get("endDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["end_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["endDate"]
        )
    else:
        raise DeserializationError(
            "BatchGetAssetPropertyAggregatesEntry.end_date required"
        )
    if data.get("qualities") is not None:
        import capo_iotsitewise.types.qualities

        out["qualities"] = capo_iotsitewise.types.qualities.deserialize_json(
            data["qualities"]
        )
    if data.get("timeOrdering") is not None:
        import capo_iotsitewise.types.time_ordering

        out["time_ordering"] = capo_iotsitewise.types.time_ordering.deserialize_json(
            data["timeOrdering"]
        )
    return out
