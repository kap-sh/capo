"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_connector_configuration


class ConnectorConfigurationAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_connector_configuration.AzureConnectorConfiguration"


ConnectorConfiguration: TypeAlias = (
    ConnectorConfigurationAzureMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConnectorConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_connector_configuration

        return {
            "Azure": capo_observabilityadmin.types.azure_connector_configuration.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("ConnectorConfiguration: no variant present")


def deserialize_json(data: dict) -> ConnectorConfiguration:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_connector_configuration

        return {
            "Azure": capo_observabilityadmin.types.azure_connector_configuration.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConnectorConfiguration: no recognized variant key")
