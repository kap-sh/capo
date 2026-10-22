"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DatabricksConnectionType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.databricks_delta_sharing_connection


class _DatabricksConnectionType_deltaSharing(TypedDict, closed=True):
    deltaSharing: "capo_cleanrooms.types.databricks_delta_sharing_connection.DatabricksDeltaSharingConnection"


DatabricksConnectionType: TypeAlias = (
    _DatabricksConnectionType_deltaSharing | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatabricksConnectionType) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DatabricksConnectionType: cannot serialize unknown variant {value.name!r}"
        )
    elif "deltaSharing" in value:
        import capo_cleanrooms.types.databricks_delta_sharing_connection

        return {
            "deltaSharing": capo_cleanrooms.types.databricks_delta_sharing_connection.serialize_json(
                value["deltaSharing"]
            )
        }
    else:
        raise SerializationError("DatabricksConnectionType: no variant present")


def deserialize_json(data: dict) -> DatabricksConnectionType:
    if data.get("deltaSharing") is not None:
        import capo_cleanrooms.types.databricks_delta_sharing_connection

        return {
            "deltaSharing": capo_cleanrooms.types.databricks_delta_sharing_connection.deserialize_json(
                data["deltaSharing"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DatabricksConnectionType: no recognized variant key"
        )
