"""Generated from Smithy shape ``com.amazonaws.datazone#GlueConnectionType``."""

from typing import Literal, TypeAlias, cast

GlueConnectionType: TypeAlias = Literal[
    "SNOWFLAKE",
    "BIGQUERY",
    "DOCUMENTDB",
    "DYNAMODB",
    "MYSQL",
    "OPENSEARCH",
    "ORACLE",
    "POSTGRESQL",
    "REDSHIFT",
    "SAPHANA",
    "SQLSERVER",
    "TERADATA",
    "VERTICA",
    "ICEBERGRESTCATALOG",
    "SNOWFLAKEICEBERGRESTCATALOG",
    "DATABRICKSICEBERGRESTCATALOG",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlueConnectionType) -> str:
    return value


def deserialize_json(data: str) -> GlueConnectionType:
    return cast(GlueConnectionType, data)
