"""Generated from Smithy shape ``com.amazonaws.mailmanager#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.private_network_configuration
    import capo_mailmanager.types.public_network_configuration


class _NetworkConfiguration_PublicNetworkConfiguration(TypedDict, closed=True):
    PublicNetworkConfiguration: (
        "capo_mailmanager.types.public_network_configuration.PublicNetworkConfiguration"
    )


class _NetworkConfiguration_PrivateNetworkConfiguration(TypedDict, closed=True):
    PrivateNetworkConfiguration: "capo_mailmanager.types.private_network_configuration.PrivateNetworkConfiguration"


NetworkConfiguration: TypeAlias = (
    _NetworkConfiguration_PublicNetworkConfiguration
    | _NetworkConfiguration_PrivateNetworkConfiguration
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NetworkConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PublicNetworkConfiguration" in value:
        import capo_mailmanager.types.public_network_configuration

        return {
            "PublicNetworkConfiguration": capo_mailmanager.types.public_network_configuration.serialize_aws_json_1_0(
                value["PublicNetworkConfiguration"]
            )
        }
    elif "PrivateNetworkConfiguration" in value:
        import capo_mailmanager.types.private_network_configuration

        return {
            "PrivateNetworkConfiguration": capo_mailmanager.types.private_network_configuration.serialize_aws_json_1_0(
                value["PrivateNetworkConfiguration"]
            )
        }
    else:
        raise SerializationError("NetworkConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> NetworkConfiguration:
    if data.get("PublicNetworkConfiguration") is not None:
        import capo_mailmanager.types.public_network_configuration

        return {
            "PublicNetworkConfiguration": capo_mailmanager.types.public_network_configuration.deserialize_aws_json_1_0(
                data["PublicNetworkConfiguration"]
            )
        }
    elif data.get("PrivateNetworkConfiguration") is not None:
        import capo_mailmanager.types.private_network_configuration

        return {
            "PrivateNetworkConfiguration": capo_mailmanager.types.private_network_configuration.deserialize_aws_json_1_0(
                data["PrivateNetworkConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NetworkConfiguration: no recognized variant key")
