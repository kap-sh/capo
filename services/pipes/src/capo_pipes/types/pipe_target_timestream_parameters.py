"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetTimestreamParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.dimension_mappings
    import capo_pipes.types.epoch_time_unit
    import capo_pipes.types.multi_measure_mappings
    import capo_pipes.types.single_measure_mappings
    import capo_pipes.types.time_field_type
    import capo_pipes.types.time_value
    import capo_pipes.types.timestamp_format
    import capo_pipes.types.version_value


class PipeTargetTimestreamParameters(TypedDict, closed=True):
    time_value: "capo_pipes.types.time_value.TimeValue"
    """<p>Dynamic path to the source data field that represents the time value for your data.</p>"""
    epoch_time_unit: NotRequired["capo_pipes.types.epoch_time_unit.EpochTimeUnit"]
    """<p>The granularity of the time units used. Default is <code>MILLISECONDS</code>.</p> <p>Required if <code>TimeFieldType</code> is specified as <code>EPOCH</code>.</p>"""
    time_field_type: NotRequired["capo_pipes.types.time_field_type.TimeFieldType"]
    """<p>The type of time value used.</p> <p>The default is <code>EPOCH</code>.</p>"""
    timestamp_format: NotRequired["capo_pipes.types.timestamp_format.TimestampFormat"]
    """<p>How to format the timestamps. For example, <code>yyyy-MM-dd'T'HH:mm:ss'Z'</code>.</p> <p>Required if <code>TimeFieldType</code> is specified as <code>TIMESTAMP_FORMAT</code>.</p>"""
    version_value: "capo_pipes.types.version_value.VersionValue"
    """<p>64 bit version value or source data field that represents the version value for your data.</p> <p>Write requests with a higher version number will update the existing measure values of the record and version. In cases where the measure value is the same, the version will still be updated. </p> <p>Default value is 1. </p> <p>Timestream for LiveAnalytics does not support updating partial measure values in a record.</p> <p>Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, <code>Version</code> will still be updated. Default value is <code>1</code>.</p> <note> <p> <code>Version</code> must be <code>1</code> or greater, or you will receive a <code>ValidationException</code> error.</p> </note>"""
    dimension_mappings: "capo_pipes.types.dimension_mappings.DimensionMappings"
    """<p>Map source data to dimensions in the target Timestream for LiveAnalytics table.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html">Amazon Timestream for LiveAnalytics concepts</a> </p>"""
    single_measure_mappings: NotRequired[
        "capo_pipes.types.single_measure_mappings.SingleMeasureMappings"
    ]
    """<p>Mappings of single source data fields to individual records in the specified Timestream for LiveAnalytics table.</p>"""
    multi_measure_mappings: NotRequired[
        "capo_pipes.types.multi_measure_mappings.MultiMeasureMappings"
    ]
    """<p>Maps multiple measures from the source event to the same record in the specified Timestream for LiveAnalytics table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetTimestreamParameters) -> dict:
    out: dict = {}
    out["TimeValue"] = value["time_value"]
    if "epoch_time_unit" in value:
        out["EpochTimeUnit"] = value["epoch_time_unit"]
    if "time_field_type" in value:
        out["TimeFieldType"] = value["time_field_type"]
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    out["VersionValue"] = value["version_value"]
    import capo_pipes.types.dimension_mappings

    out["DimensionMappings"] = capo_pipes.types.dimension_mappings.serialize_json(
        value["dimension_mappings"]
    )
    if "single_measure_mappings" in value:
        import capo_pipes.types.single_measure_mappings

        out["SingleMeasureMappings"] = (
            capo_pipes.types.single_measure_mappings.serialize_json(
                value["single_measure_mappings"]
            )
        )
    if "multi_measure_mappings" in value:
        import capo_pipes.types.multi_measure_mappings

        out["MultiMeasureMappings"] = (
            capo_pipes.types.multi_measure_mappings.serialize_json(
                value["multi_measure_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeTargetTimestreamParameters:
    out: PipeTargetTimestreamParameters = {}  # type: ignore[typeddict-item]
    if data.get("TimeValue") is not None:
        out["time_value"] = data["TimeValue"]
    else:
        raise DeserializationError("PipeTargetTimestreamParameters.time_value required")
    if data.get("EpochTimeUnit") is not None:
        out["epoch_time_unit"] = data["EpochTimeUnit"]
    if data.get("TimeFieldType") is not None:
        out["time_field_type"] = data["TimeFieldType"]
    if data.get("TimestampFormat") is not None:
        out["timestamp_format"] = data["TimestampFormat"]
    if data.get("VersionValue") is not None:
        out["version_value"] = data["VersionValue"]
    else:
        raise DeserializationError(
            "PipeTargetTimestreamParameters.version_value required"
        )
    if data.get("DimensionMappings") is not None:
        import capo_pipes.types.dimension_mappings

        out["dimension_mappings"] = (
            capo_pipes.types.dimension_mappings.deserialize_json(
                data["DimensionMappings"]
            )
        )
    else:
        raise DeserializationError(
            "PipeTargetTimestreamParameters.dimension_mappings required"
        )
    if data.get("SingleMeasureMappings") is not None:
        import capo_pipes.types.single_measure_mappings

        out["single_measure_mappings"] = (
            capo_pipes.types.single_measure_mappings.deserialize_json(
                data["SingleMeasureMappings"]
            )
        )
    if data.get("MultiMeasureMappings") is not None:
        import capo_pipes.types.multi_measure_mappings

        out["multi_measure_mappings"] = (
            capo_pipes.types.multi_measure_mappings.deserialize_json(
                data["MultiMeasureMappings"]
            )
        )
    return out
