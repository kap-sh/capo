"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_core.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_vpc_egress_configuration


class _NetworkConnectorConfiguration_VpcEgressConfiguration(TypedDict, closed=True):
    VpcEgressConfiguration: "capo_lambda_core.types.network_connector_vpc_egress_configuration.NetworkConnectorVpcEgressConfiguration"


NetworkConnectorConfiguration: TypeAlias = (
    _NetworkConnectorConfiguration_VpcEgressConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorConfiguration) -> dict:
    if "VpcEgressConfiguration" in value:
        import capo_lambda_core.types.network_connector_vpc_egress_configuration

        return {
            "VpcEgressConfiguration": capo_lambda_core.types.network_connector_vpc_egress_configuration.serialize_json(
                value["VpcEgressConfiguration"]
            )
        }
    else:
        raise SerializationError("NetworkConnectorConfiguration: no variant present")


def deserialize_json(data: dict) -> NetworkConnectorConfiguration:
    if data.get("VpcEgressConfiguration") is not None:
        import capo_lambda_core.types.network_connector_vpc_egress_configuration

        return {
            "VpcEgressConfiguration": capo_lambda_core.types.network_connector_vpc_egress_configuration.deserialize_json(
                data["VpcEgressConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "NetworkConnectorConfiguration: no recognized variant key"
        )
