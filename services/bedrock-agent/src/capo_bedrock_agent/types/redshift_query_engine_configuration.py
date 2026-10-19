"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_provisioned_configuration
    import capo_bedrock_agent.types.redshift_query_engine_type
    import capo_bedrock_agent.types.redshift_serverless_configuration


class RedshiftQueryEngineConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.redshift_query_engine_type.RedshiftQueryEngineType"
    """<p>The type of query engine.</p>"""
    serverless_configuration: NotRequired[
        "capo_bedrock_agent.types.redshift_serverless_configuration.RedshiftServerlessConfiguration"
    ]
    """<p>Specifies configurations for a serverless Amazon Redshift query engine.</p>"""
    provisioned_configuration: NotRequired[
        "capo_bedrock_agent.types.redshift_provisioned_configuration.RedshiftProvisionedConfiguration"
    ]
    """<p>Specifies configurations for a provisioned Amazon Redshift query engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.redshift_query_engine_type

    out["type"] = capo_bedrock_agent.types.redshift_query_engine_type.serialize_json(
        value["type"]
    )
    if "serverless_configuration" in value:
        import capo_bedrock_agent.types.redshift_serverless_configuration

        out["serverlessConfiguration"] = (
            capo_bedrock_agent.types.redshift_serverless_configuration.serialize_json(
                value["serverless_configuration"]
            )
        )
    if "provisioned_configuration" in value:
        import capo_bedrock_agent.types.redshift_provisioned_configuration

        out["provisionedConfiguration"] = (
            capo_bedrock_agent.types.redshift_provisioned_configuration.serialize_json(
                value["provisioned_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftQueryEngineConfiguration:
    out: RedshiftQueryEngineConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.redshift_query_engine_type

        out["type"] = (
            capo_bedrock_agent.types.redshift_query_engine_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.redshift_query_engine_type.RedshiftQueryEngineType",
            "",
        )
    if data.get("serverlessConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_serverless_configuration

        out["serverless_configuration"] = (
            capo_bedrock_agent.types.redshift_serverless_configuration.deserialize_json(
                data["serverlessConfiguration"]
            )
        )
    if data.get("provisionedConfiguration") is not None:
        import capo_bedrock_agent.types.redshift_provisioned_configuration

        out["provisioned_configuration"] = (
            capo_bedrock_agent.types.redshift_provisioned_configuration.deserialize_json(
                data["provisionedConfiguration"]
            )
        )
    return out
