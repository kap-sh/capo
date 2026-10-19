"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DataSegmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.data_segment_enrichment
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.property_data_type
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.time_series_id


class DataSegmentSummary(TypedDict, closed=True):
    source_dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the source dataset that contains the data segment.</p>"""
    time_series_id: "capo_iotsitewise.types.time_series_id.TimeSeriesId"
    """<p>The ID of the time series.</p>"""
    start_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision start time of the data segment.</p>"""
    end_timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The nanosecond-precision end time of the data segment.</p>"""
    alias: "capo_iotsitewise.types.property_alias.PropertyAlias"
    """<p>The alias of the time series.</p>"""
    data_type: "capo_iotsitewise.types.property_data_type.PropertyDataType"
    """<p>The data type of the time series.</p>"""
    enrichment: NotRequired[
        "capo_iotsitewise.types.data_segment_enrichment.DataSegmentEnrichment"
    ]
    """<p>The enrichment information for the data segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSegmentSummary) -> dict:
    out: dict = {}
    out["sourceDatasetId"] = value["source_dataset_id"]
    out["timeSeriesId"] = value["time_series_id"]
    import capo_iotsitewise.types.time_in_nanos

    out["startTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["start_timestamp"]
    )
    import capo_iotsitewise.types.time_in_nanos

    out["endTimestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["end_timestamp"]
    )
    out["alias"] = value["alias"]
    import capo_iotsitewise.types.property_data_type

    out["dataType"] = capo_iotsitewise.types.property_data_type.serialize_json(
        value["data_type"]
    )
    if "enrichment" in value:
        import capo_iotsitewise.types.data_segment_enrichment

        out["enrichment"] = (
            capo_iotsitewise.types.data_segment_enrichment.serialize_json(
                value["enrichment"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSegmentSummary:
    out: DataSegmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("sourceDatasetId") is not None:
        out["source_dataset_id"] = data["sourceDatasetId"]
    else:
        out["source_dataset_id"] = ""
    if data.get("timeSeriesId") is not None:
        out["time_series_id"] = data["timeSeriesId"]
    else:
        out["time_series_id"] = ""
    if data.get("startTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["start_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["startTimestamp"]
        )
    else:
        raise DeserializationError("DataSegmentSummary.start_timestamp required")
    if data.get("endTimestamp") is not None:
        import capo_iotsitewise.types.time_in_nanos

        out["end_timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["endTimestamp"]
        )
    else:
        raise DeserializationError("DataSegmentSummary.end_timestamp required")
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    else:
        out["alias"] = ""
    if data.get("dataType") is not None:
        import capo_iotsitewise.types.property_data_type

        out["data_type"] = capo_iotsitewise.types.property_data_type.deserialize_json(
            data["dataType"]
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_iotsitewise.types.property_data_type.PropertyDataType", ""
        )
    if data.get("enrichment") is not None:
        import capo_iotsitewise.types.data_segment_enrichment

        out["enrichment"] = (
            capo_iotsitewise.types.data_segment_enrichment.deserialize_json(
                data["enrichment"]
            )
        )
    return out
