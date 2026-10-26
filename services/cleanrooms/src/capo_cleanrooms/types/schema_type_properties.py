"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association_schema_type_properties
    import capo_cleanrooms.types.id_mapping_table_schema_type_properties
    import capo_cleanrooms.types.intermediate_table_schema_type_properties


class _SchemaTypeProperties_idMappingTable(TypedDict, closed=True):
    idMappingTable: "capo_cleanrooms.types.id_mapping_table_schema_type_properties.IdMappingTableSchemaTypeProperties"


class _SchemaTypeProperties_intermediateTable(TypedDict, closed=True):
    intermediateTable: "capo_cleanrooms.types.intermediate_table_schema_type_properties.IntermediateTableSchemaTypeProperties"


class _SchemaTypeProperties_configuredTableAssociation(TypedDict, closed=True):
    configuredTableAssociation: "capo_cleanrooms.types.configured_table_association_schema_type_properties.ConfiguredTableAssociationSchemaTypeProperties"


SchemaTypeProperties: TypeAlias = (
    _SchemaTypeProperties_idMappingTable
    | _SchemaTypeProperties_intermediateTable
    | _SchemaTypeProperties_configuredTableAssociation
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SchemaTypeProperties) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SchemaTypeProperties: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "idMappingTable" in value:
        import capo_cleanrooms.types.id_mapping_table_schema_type_properties

        return {
            "idMappingTable": capo_cleanrooms.types.id_mapping_table_schema_type_properties.serialize_json(
                value["idMappingTable"]
            )
        }
    elif "intermediateTable" in value:
        import capo_cleanrooms.types.intermediate_table_schema_type_properties

        return {
            "intermediateTable": capo_cleanrooms.types.intermediate_table_schema_type_properties.serialize_json(
                value["intermediateTable"]
            )
        }
    elif "configuredTableAssociation" in value:
        import capo_cleanrooms.types.configured_table_association_schema_type_properties

        return {
            "configuredTableAssociation": capo_cleanrooms.types.configured_table_association_schema_type_properties.serialize_json(
                value["configuredTableAssociation"]
            )
        }
    else:
        raise SerializationError("SchemaTypeProperties: no variant present")


def deserialize_json(data: dict) -> SchemaTypeProperties:
    if data.get("idMappingTable") is not None:
        import capo_cleanrooms.types.id_mapping_table_schema_type_properties

        return {
            "idMappingTable": capo_cleanrooms.types.id_mapping_table_schema_type_properties.deserialize_json(
                data["idMappingTable"]
            )
        }
    elif data.get("intermediateTable") is not None:
        import capo_cleanrooms.types.intermediate_table_schema_type_properties

        return {
            "intermediateTable": capo_cleanrooms.types.intermediate_table_schema_type_properties.deserialize_json(
                data["intermediateTable"]
            )
        }
    elif data.get("configuredTableAssociation") is not None:
        import capo_cleanrooms.types.configured_table_association_schema_type_properties

        return {
            "configuredTableAssociation": capo_cleanrooms.types.configured_table_association_schema_type_properties.deserialize_json(
                data["configuredTableAssociation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SchemaTypeProperties: no recognized variant key")
