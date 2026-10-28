"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TableReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.athena_table_reference
    import capo_cleanrooms.types.databricks_table_reference
    import capo_cleanrooms.types.glue_table_reference
    import capo_cleanrooms.types.snowflake_table_reference


class TableReferenceGlueMember(TypedDict, closed=True):
    glue: "capo_cleanrooms.types.glue_table_reference.GlueTableReference"


class TableReferenceSnowflakeMember(TypedDict, closed=True):
    snowflake: "capo_cleanrooms.types.snowflake_table_reference.SnowflakeTableReference"


class TableReferenceAthenaMember(TypedDict, closed=True):
    athena: "capo_cleanrooms.types.athena_table_reference.AthenaTableReference"


class TableReferenceDatabricksMember(TypedDict, closed=True):
    databricks: (
        "capo_cleanrooms.types.databricks_table_reference.DatabricksTableReference"
    )


TableReference: TypeAlias = (
    TableReferenceGlueMember
    | TableReferenceSnowflakeMember
    | TableReferenceAthenaMember
    | TableReferenceDatabricksMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TableReference) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TableReference: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "glue" in value:
        import capo_cleanrooms.types.glue_table_reference

        return {
            "glue": capo_cleanrooms.types.glue_table_reference.serialize_json(
                value["glue"]
            )
        }
    elif "snowflake" in value:
        import capo_cleanrooms.types.snowflake_table_reference

        return {
            "snowflake": capo_cleanrooms.types.snowflake_table_reference.serialize_json(
                value["snowflake"]
            )
        }
    elif "athena" in value:
        import capo_cleanrooms.types.athena_table_reference

        return {
            "athena": capo_cleanrooms.types.athena_table_reference.serialize_json(
                value["athena"]
            )
        }
    elif "databricks" in value:
        import capo_cleanrooms.types.databricks_table_reference

        return {
            "databricks": capo_cleanrooms.types.databricks_table_reference.serialize_json(
                value["databricks"]
            )
        }
    else:
        raise SerializationError("TableReference: no variant present")


def deserialize_json(data: dict) -> TableReference:
    if data.get("glue") is not None:
        import capo_cleanrooms.types.glue_table_reference

        return {
            "glue": capo_cleanrooms.types.glue_table_reference.deserialize_json(
                data["glue"]
            )
        }
    elif data.get("snowflake") is not None:
        import capo_cleanrooms.types.snowflake_table_reference

        return {
            "snowflake": capo_cleanrooms.types.snowflake_table_reference.deserialize_json(
                data["snowflake"]
            )
        }
    elif data.get("athena") is not None:
        import capo_cleanrooms.types.athena_table_reference

        return {
            "athena": capo_cleanrooms.types.athena_table_reference.deserialize_json(
                data["athena"]
            )
        }
    elif data.get("databricks") is not None:
        import capo_cleanrooms.types.databricks_table_reference

        return {
            "databricks": capo_cleanrooms.types.databricks_table_reference.deserialize_json(
                data["databricks"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TableReference: no recognized variant key")
