"""Generated from Smithy shape ``com.amazonaws.iotsitewise#EventDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.enrichment_trim_settings
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.time_series_id


class EventDetection(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The IoT SiteWise dataset ID containing the video time-series data to analyze. Query IoT SiteWise to discover available datasets in your workspace.</p>"""
    time_series_id: NotRequired["capo_iotsitewise.types.time_series_id.TimeSeriesId"]
    """<p>Unique system identifier for the video time series to analyze. Specify either timeSeriesId or propertyAlias, but not both. Use this when you have the system-generated time series identifier from IoT SiteWise.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>Human-readable alias for the video time series to analyze (e.g., /camera/warehouse/zone-a). Specify either propertyAlias or timeSeriesId, but not both. Use this when you have configured friendly aliases in IoT SiteWise for better readability.</p>"""
    trim_settings: (
        "capo_iotsitewise.types.enrichment_trim_settings.EnrichmentTrimSettings"
    )
    """<p>Time range settings defining which portion of the video time-series data to process. Required to ensure predictable processing time and prevent analyzing unbounded datasets. Start and end times must be within the dataset's time bounds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDetection) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    if "time_series_id" in value:
        out["timeSeriesId"] = value["time_series_id"]
    if "property_alias" in value:
        out["propertyAlias"] = value["property_alias"]
    import capo_iotsitewise.types.enrichment_trim_settings

    out["trimSettings"] = (
        capo_iotsitewise.types.enrichment_trim_settings.serialize_json(
            value["trim_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> EventDetection:
    out: EventDetection = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    if data.get("propertyAlias") is not None:
        out["property_alias"] = data["propertyAlias"]
    if data.get("trimSettings") is not None:
        import capo_iotsitewise.types.enrichment_trim_settings

        out["trim_settings"] = (
            capo_iotsitewise.types.enrichment_trim_settings.deserialize_json(
                data["trimSettings"]
            )
        )
    else:
        raise DeserializationError("EventDetection.trim_settings required")
    return out
