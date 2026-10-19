"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#Duration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.duration_type


class Duration(TypedDict, closed=True):
    duration_type: "capo_timestream_influxdb.types.duration_type.DurationType"
    """<p>The type of duration for InfluxDB parameters.</p>"""
    value: "int"
    """<p>The value of duration for InfluxDB parameters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Duration) -> dict:
    out: dict = {}
    import capo_timestream_influxdb.types.duration_type

    out["durationType"] = (
        capo_timestream_influxdb.types.duration_type.serialize_aws_json_1_0(
            value["duration_type"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if data.get("durationType") is not None:
        import capo_timestream_influxdb.types.duration_type

        out["duration_type"] = (
            capo_timestream_influxdb.types.duration_type.deserialize_aws_json_1_0(
                data["durationType"]
            )
        )
    else:
        import typing

        out["duration_type"] = typing.cast(
            "capo_timestream_influxdb.types.duration_type.DurationType", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
