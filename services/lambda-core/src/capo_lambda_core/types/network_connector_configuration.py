"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_core.errors import DeserializationError, SerializationError
from capo_lambda_core.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_lambda_core.types.network_connector_vpc_egress_configuration


class NetworkConnectorConfigurationVpcEgressConfigurationMember(TypedDict, closed=True):
    VpcEgressConfiguration: "capo_lambda_core.types.network_connector_vpc_egress_configuration.NetworkConnectorVpcEgressConfiguration"


NetworkConnectorConfiguration: TypeAlias = (
    NetworkConnectorConfigurationVpcEgressConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectorConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NetworkConnectorConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "VpcEgressConfiguration" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "NetworkConnectorConfiguration: no recognized variant key"
        )
