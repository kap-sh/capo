"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteNetworkMigrationDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id


class DeleteNetworkMigrationDefinitionRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkMigrationDefinitionRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    return out


def deserialize_json(data: dict) -> DeleteNetworkMigrationDefinitionRequest:
    out: DeleteNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    return out
