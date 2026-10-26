"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import DeserializationError, SerializationError
from capo_timestream_influxdb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.influx_d_bv2_parameters
    import capo_timestream_influxdb.types.influx_d_bv3_core_parameters
    import capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters


class _Parameters_InfluxDBv2(TypedDict, closed=True):
    InfluxDBv2: (
        "capo_timestream_influxdb.types.influx_d_bv2_parameters.InfluxDBv2Parameters"
    )


class _Parameters_InfluxDBv3Core(TypedDict, closed=True):
    InfluxDBv3Core: "capo_timestream_influxdb.types.influx_d_bv3_core_parameters.InfluxDBv3CoreParameters"


class _Parameters_InfluxDBv3Enterprise(TypedDict, closed=True):
    InfluxDBv3Enterprise: "capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.InfluxDBv3EnterpriseParameters"


Parameters: TypeAlias = (
    _Parameters_InfluxDBv2
    | _Parameters_InfluxDBv3Core
    | _Parameters_InfluxDBv3Enterprise
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Parameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Parameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "InfluxDBv2" in value:
        import capo_timestream_influxdb.types.influx_d_bv2_parameters

        return {
            "InfluxDBv2": capo_timestream_influxdb.types.influx_d_bv2_parameters.serialize_aws_json_1_0(
                value["InfluxDBv2"]
            )
        }
    elif "InfluxDBv3Core" in value:
        import capo_timestream_influxdb.types.influx_d_bv3_core_parameters

        return {
            "InfluxDBv3Core": capo_timestream_influxdb.types.influx_d_bv3_core_parameters.serialize_aws_json_1_0(
                value["InfluxDBv3Core"]
            )
        }
    elif "InfluxDBv3Enterprise" in value:
        import capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters

        return {
            "InfluxDBv3Enterprise": capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.serialize_aws_json_1_0(
                value["InfluxDBv3Enterprise"]
            )
        }
    else:
        raise SerializationError("Parameters: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Parameters:
    if data.get("InfluxDBv2") is not None:
        import capo_timestream_influxdb.types.influx_d_bv2_parameters

        return {
            "InfluxDBv2": capo_timestream_influxdb.types.influx_d_bv2_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv2"]
            )
        }
    elif data.get("InfluxDBv3Core") is not None:
        import capo_timestream_influxdb.types.influx_d_bv3_core_parameters

        return {
            "InfluxDBv3Core": capo_timestream_influxdb.types.influx_d_bv3_core_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv3Core"]
            )
        }
    elif data.get("InfluxDBv3Enterprise") is not None:
        import capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters

        return {
            "InfluxDBv3Enterprise": capo_timestream_influxdb.types.influx_d_bv3_enterprise_parameters.deserialize_aws_json_1_0(
                data["InfluxDBv3Enterprise"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Parameters: no recognized variant key")
