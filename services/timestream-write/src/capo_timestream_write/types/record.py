"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.dimensions
    import capo_timestream_write.types.measure_value_type
    import capo_timestream_write.types.measure_values
    import capo_timestream_write.types.record_version
    import capo_timestream_write.types.schema_name
    import capo_timestream_write.types.string_value256
    import capo_timestream_write.types.string_value2048
    import capo_timestream_write.types.time_unit


class Record(TypedDict, closed=True):
    dimensions: NotRequired["capo_timestream_write.types.dimensions.Dimensions"]
    """<p>Contains the list of dimensions for time-series data points.</p>"""
    measure_name: NotRequired["capo_timestream_write.types.schema_name.SchemaName"]
    """<p>Measure represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the RPM of a wind turbine are measures. </p>"""
    measure_value: NotRequired[
        "capo_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p> Contains the measure value for the time-series data point. </p>"""
    measure_value_type: NotRequired[
        "capo_timestream_write.types.measure_value_type.MeasureValueType"
    ]
    """<p> Contains the data type of the measure value for the time-series data point. Default type is <code>DOUBLE</code>. For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/writes.html#writes.data-types">Data types</a>.</p>"""
    time: NotRequired["capo_timestream_write.types.string_value256.StringValue256"]
    """<p> Contains the time at which the measure value for the data point was collected. The time value plus the unit provides the time elapsed since the epoch. For example, if the time value is <code>12345</code> and the unit is <code>ms</code>, then <code>12345 ms</code> have elapsed since the epoch. </p>"""
    time_unit: NotRequired["capo_timestream_write.types.time_unit.TimeUnit"]
    """<p> The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is <code>MILLISECONDS</code>. </p>"""
    version: NotRequired["capo_timestream_write.types.record_version.RecordVersion"]
    """<p>64-bit attribute used for record updates. Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, <code>Version</code> will still be updated. Default value is <code>1</code>.</p> <note> <p> <code>Version</code> must be <code>1</code> or greater, or you will receive a <code>ValidationException</code> error.</p> </note>"""
    measure_values: NotRequired[
        "capo_timestream_write.types.measure_values.MeasureValues"
    ]
    """<p> Contains the list of MeasureValue for time-series data points. </p> <p> This is only allowed for type <code>MULTI</code>. For scalar values, use <code>MeasureValue</code> attribute of the record directly. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Record) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_timestream_write.types.dimensions

        out["Dimensions"] = (
            capo_timestream_write.types.dimensions.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "measure_name" in value:
        out["MeasureName"] = value["measure_name"]
    if "measure_value" in value:
        out["MeasureValue"] = value["measure_value"]
    if "measure_value_type" in value:
        import capo_timestream_write.types.measure_value_type

        out["MeasureValueType"] = (
            capo_timestream_write.types.measure_value_type.serialize_aws_json_1_0(
                value["measure_value_type"]
            )
        )
    if "time" in value:
        out["Time"] = value["time"]
    if "time_unit" in value:
        import capo_timestream_write.types.time_unit

        out["TimeUnit"] = capo_timestream_write.types.time_unit.serialize_aws_json_1_0(
            value["time_unit"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "measure_values" in value:
        import capo_timestream_write.types.measure_values

        out["MeasureValues"] = (
            capo_timestream_write.types.measure_values.serialize_aws_json_1_0(
                value["measure_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_timestream_write.types.dimensions

        out["dimensions"] = (
            capo_timestream_write.types.dimensions.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    if data.get("MeasureName") is not None:
        out["measure_name"] = data["MeasureName"]
    if data.get("MeasureValue") is not None:
        out["measure_value"] = data["MeasureValue"]
    if data.get("MeasureValueType") is not None:
        import capo_timestream_write.types.measure_value_type

        out["measure_value_type"] = (
            capo_timestream_write.types.measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    if data.get("Time") is not None:
        out["time"] = data["Time"]
    if data.get("TimeUnit") is not None:
        import capo_timestream_write.types.time_unit

        out["time_unit"] = (
            capo_timestream_write.types.time_unit.deserialize_aws_json_1_0(
                data["TimeUnit"]
            )
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("MeasureValues") is not None:
        import capo_timestream_write.types.measure_values

        out["measure_values"] = (
            capo_timestream_write.types.measure_values.deserialize_aws_json_1_0(
                data["MeasureValues"]
            )
        )
    return out
