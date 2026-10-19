"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration
    import capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration
    import capo_bedrock_agent.types.redshift_query_engine_storage_type


class RedshiftQueryEngineStorageConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.redshift_query_engine_storage_type.RedshiftQueryEngineStorageType"
    """<p>The data storage service to use.</p>"""
    aws_data_catalog_configuration: NotRequired[
        "capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.RedshiftQueryEngineAwsDataCatalogStorageConfiguration"
    ]
    """<p>Specifies configurations for storage in Glue Data Catalog.</p>"""
    redshift_configuration: NotRequired[
        "capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.RedshiftQueryEngineRedshiftStorageConfiguration"
    ]
    """<p>Specifies configurations for storage in Amazon Redshift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineStorageConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.redshift_query_engine_storage_type

    out["type"] = (
        capo_bedrock_agent.types.redshift_query_engine_storage_type.serialize_json(
            value["type"]
        )
    )
    if "aws_data_catalog_configuration" in value:
        import capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration

        out["awsDataCatalogConfiguration"] = (
            capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.serialize_json(
                value["aws_data_catalog_configuration"]
            )
        )
    if "redshift_configuration" in value:
        import capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration

        out["redshiftConfiguration"] = (
            capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.serialize_json(
                value["redshift_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftQueryEngineStorageConfiguration:
    out: RedshiftQueryEngineStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_storage_type

        out["type"] = (
            capo_bedrock_agent.types.redshift_query_engine_storage_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.redshift_query_engine_storage_type.RedshiftQueryEngineStorageType",
            "",
        )
    if data.get("awsDataCatalogConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration

        out["aws_data_catalog_configuration"] = (
            capo_bedrock_agent.types.redshift_query_engine_aws_data_catalog_storage_configuration.deserialize_json(
                data["awsDataCatalogConfiguration"]
            )
        )
    if data.get("redshiftConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration

        out["redshift_configuration"] = (
            capo_bedrock_agent.types.redshift_query_engine_redshift_storage_configuration.deserialize_json(
                data["redshiftConfiguration"]
            )
        )
    return out
