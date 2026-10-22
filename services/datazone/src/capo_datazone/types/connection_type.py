"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "ATHENA",
    "BIGQUERY",
    "DATABRICKS",
    "DOCUMENTDB",
    "DYNAMODB",
    "HYPERPOD",
    "IAM",
    "MYSQL",
    "OPENSEARCH",
    "ORACLE",
    "POSTGRESQL",
    "REDSHIFT",
    "S3",
    "SAPHANA",
    "SNOWFLAKE",
    "SPARK",
    "SQLSERVER",
    "TERADATA",
    "VERTICA",
    "WORKFLOWS_MWAA",
    "AMAZON_Q",
    "MLFLOW",
    "VPC",
    "GIT",
    "ICEBERGRESTCATALOG",
    "SNOWFLAKEICEBERGRESTCATALOG",
    "DATABRICKSICEBERGRESTCATALOG",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
