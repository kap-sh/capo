"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.secrets_manager_arn
    import capo_cleanrooms.types.snowflake_account_identifier
    import capo_cleanrooms.types.snowflake_database_name
    import capo_cleanrooms.types.snowflake_schema_name
    import capo_cleanrooms.types.snowflake_table_name
    import capo_cleanrooms.types.snowflake_table_schema


class SnowflakeTableReference(TypedDict, closed=True):
    secret_arn: "capo_cleanrooms.types.secrets_manager_arn.SecretsManagerArn"
    """<p> The secret ARN of the Snowflake table reference.</p>"""
    account_identifier: (
        "capo_cleanrooms.types.snowflake_account_identifier.SnowflakeAccountIdentifier"
    )
    """<p> The account identifier for the Snowflake table reference.</p>"""
    database_name: "capo_cleanrooms.types.snowflake_database_name.SnowflakeDatabaseName"
    """<p> The name of the database the Snowflake table belongs to.</p>"""
    table_name: "capo_cleanrooms.types.snowflake_table_name.SnowflakeTableName"
    """<p> The name of the Snowflake table.</p>"""
    schema_name: "capo_cleanrooms.types.snowflake_schema_name.SnowflakeSchemaName"
    """<p> The schema name of the Snowflake table reference.</p>"""
    table_schema: "capo_cleanrooms.types.snowflake_table_schema.SnowflakeTableSchema"
    """<p> The schema of the Snowflake table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableReference) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["accountIdentifier"] = value["account_identifier"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    out["schemaName"] = value["schema_name"]
    import capo_cleanrooms.types.snowflake_table_schema

    out["tableSchema"] = capo_cleanrooms.types.snowflake_table_schema.serialize_json(
        value["table_schema"]
    )
    return out


def deserialize_json(data: dict) -> SnowflakeTableReference:
    out: SnowflakeTableReference = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("accountIdentifier") is not None:
        out["account_identifier"] = data["accountIdentifier"]
    else:
        out["account_identifier"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    else:
        out["schema_name"] = ""
    if data.get("tableSchema") is not None:
        import capo_cleanrooms.types.snowflake_table_schema

        out["table_schema"] = (
            capo_cleanrooms.types.snowflake_table_schema.deserialize_json(
                data["tableSchema"]
            )
        )
    else:
        out["table_schema"] = {"$unknown": {"name": ""}}
    return out
