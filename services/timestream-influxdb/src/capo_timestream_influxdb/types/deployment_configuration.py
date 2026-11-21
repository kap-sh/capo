"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeploymentConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_timestream_influxdb.errors import DeserializationError, SerializationError
from capo_timestream_influxdb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration


class DeploymentConfigurationInfluxDBv3EnterpriseMember(TypedDict, closed=True):
    InfluxDBv3Enterprise: "capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration.InfluxDBv3EnterpriseDeploymentConfiguration"


DeploymentConfiguration: TypeAlias = (
    DeploymentConfigurationInfluxDBv3EnterpriseMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DeploymentConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "InfluxDBv3Enterprise" in value:
        import capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration

        return {
            "InfluxDBv3Enterprise": capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration.serialize_aws_json_1_0(
                value["InfluxDBv3Enterprise"]
            )
        }
    else:
        raise SerializationError("DeploymentConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DeploymentConfiguration:
    if data.get("InfluxDBv3Enterprise") is not None:
        import capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration

        return {
            "InfluxDBv3Enterprise": capo_timestream_influxdb.types.influx_d_bv3_enterprise_deployment_configuration.deserialize_aws_json_1_0(
                data["InfluxDBv3Enterprise"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DeploymentConfiguration: no recognized variant key")
