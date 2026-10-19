"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationSchemaTypeProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.uuid


class ConfiguredTableAssociationSchemaTypeProperties(TypedDict, closed=True):
    configured_table_association_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the configured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationSchemaTypeProperties) -> dict:
    out: dict = {}
    out["configuredTableAssociationId"] = value["configured_table_association_id"]
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociationSchemaTypeProperties:
    out: ConfiguredTableAssociationSchemaTypeProperties = {}  # type: ignore[typeddict-item]
    if data.get("configuredTableAssociationId") is not None:
        out["configured_table_association_id"] = data["configuredTableAssociationId"]
    else:
        out["configured_table_association_id"] = ""
    return out
