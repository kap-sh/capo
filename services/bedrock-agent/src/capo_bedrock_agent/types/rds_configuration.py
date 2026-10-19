"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RdsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.rds_arn
    import capo_bedrock_agent.types.rds_database_name
    import capo_bedrock_agent.types.rds_field_mapping
    import capo_bedrock_agent.types.rds_table_name
    import capo_bedrock_agent.types.secret_arn


class RdsConfiguration(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.rds_arn.RdsArn"
    """<p>The Amazon Resource Name (ARN) of the vector store.</p>"""
    credentials_secret_arn: "capo_bedrock_agent.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Amazon RDS database.</p>"""
    database_name: "capo_bedrock_agent.types.rds_database_name.RdsDatabaseName"
    """<p>The name of your Amazon RDS database.</p>"""
    table_name: "capo_bedrock_agent.types.rds_table_name.RdsTableName"
    """<p>The name of the table in the database.</p>"""
    field_mapping: "capo_bedrock_agent.types.rds_field_mapping.RdsFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsConfiguration) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    import capo_bedrock_agent.types.rds_field_mapping

    out["fieldMapping"] = capo_bedrock_agent.types.rds_field_mapping.serialize_json(
        value["field_mapping"]
    )
    return out


def deserialize_json(data: dict) -> RdsConfiguration:
    out: RdsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("credentialsSecretArn") is not None:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        out["credentials_secret_arn"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.rds_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.rds_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError("RdsConfiguration.field_mapping required")
    return out
