"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConnectorQuery``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_connector_query


class ConnectorQueryAzureMember(TypedDict, closed=True):
    Azure: "capo_observabilityadmin.types.azure_connector_query.AzureConnectorQuery"


ConnectorQuery: TypeAlias = ConnectorQueryAzureMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorQuery) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConnectorQuery: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_observabilityadmin.types.azure_connector_query

        return {
            "Azure": capo_observabilityadmin.types.azure_connector_query.serialize_json(
                value["Azure"]
            )
        }
    else:
        raise SerializationError("ConnectorQuery: no variant present")


def deserialize_json(data: dict) -> ConnectorQuery:
    if data.get("Azure") is not None:
        import capo_observabilityadmin.types.azure_connector_query

        return {
            "Azure": capo_observabilityadmin.types.azure_connector_query.deserialize_json(
                data["Azure"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConnectorQuery: no recognized variant key")
