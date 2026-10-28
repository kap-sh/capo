"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpTargetConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_gateway_target_configuration
    import capo_bedrock_agentcore_control.types.api_schema_configuration
    import capo_bedrock_agentcore_control.types.connector_target_configuration
    import capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration
    import capo_bedrock_agentcore_control.types.mcp_server_target_configuration


class McpTargetConfigurationOpenApiSchemaMember(TypedDict, closed=True):
    openApiSchema: "capo_bedrock_agentcore_control.types.api_schema_configuration.ApiSchemaConfiguration"


class McpTargetConfigurationSmithyModelMember(TypedDict, closed=True):
    smithyModel: "capo_bedrock_agentcore_control.types.api_schema_configuration.ApiSchemaConfiguration"


McpTargetConfigurationLambdaMember = TypedDict(
    "McpTargetConfigurationLambdaMember",
    {
        "lambda": "capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration.McpLambdaTargetConfiguration",
    },
    closed=True,
)


class McpTargetConfigurationMcpServerMember(TypedDict, closed=True):
    mcpServer: "capo_bedrock_agentcore_control.types.mcp_server_target_configuration.McpServerTargetConfiguration"


class McpTargetConfigurationApiGatewayMember(TypedDict, closed=True):
    apiGateway: "capo_bedrock_agentcore_control.types.api_gateway_target_configuration.ApiGatewayTargetConfiguration"


class McpTargetConfigurationConnectorMember(TypedDict, closed=True):
    connector: "capo_bedrock_agentcore_control.types.connector_target_configuration.ConnectorTargetConfiguration"


McpTargetConfiguration: TypeAlias = (
    McpTargetConfigurationOpenApiSchemaMember
    | McpTargetConfigurationSmithyModelMember
    | McpTargetConfigurationLambdaMember
    | McpTargetConfigurationMcpServerMember
    | McpTargetConfigurationApiGatewayMember
    | McpTargetConfigurationConnectorMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: McpTargetConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"McpTargetConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "openApiSchema" in value:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "openApiSchema": capo_bedrock_agentcore_control.types.api_schema_configuration.serialize_json(
                value["openApiSchema"]
            )
        }
    elif "smithyModel" in value:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "smithyModel": capo_bedrock_agentcore_control.types.api_schema_configuration.serialize_json(
                value["smithyModel"]
            )
        }
    elif "lambda" in value:
        import capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration

        return {
            "lambda": capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration.serialize_json(
                value["lambda"]
            )
        }
    elif "mcpServer" in value:
        import capo_bedrock_agentcore_control.types.mcp_server_target_configuration

        return {
            "mcpServer": capo_bedrock_agentcore_control.types.mcp_server_target_configuration.serialize_json(
                value["mcpServer"]
            )
        }
    elif "apiGateway" in value:
        import capo_bedrock_agentcore_control.types.api_gateway_target_configuration

        return {
            "apiGateway": capo_bedrock_agentcore_control.types.api_gateway_target_configuration.serialize_json(
                value["apiGateway"]
            )
        }
    elif "connector" in value:
        import capo_bedrock_agentcore_control.types.connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.connector_target_configuration.serialize_json(
                value["connector"]
            )
        }
    else:
        raise SerializationError("McpTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> McpTargetConfiguration:
    if data.get("openApiSchema") is not None:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "openApiSchema": capo_bedrock_agentcore_control.types.api_schema_configuration.deserialize_json(
                data["openApiSchema"]
            )
        }
    elif data.get("smithyModel") is not None:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "smithyModel": capo_bedrock_agentcore_control.types.api_schema_configuration.deserialize_json(
                data["smithyModel"]
            )
        }
    elif data.get("lambda") is not None:
        import capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration

        return {
            "lambda": capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration.deserialize_json(
                data["lambda"]
            )
        }
    elif data.get("mcpServer") is not None:
        import capo_bedrock_agentcore_control.types.mcp_server_target_configuration

        return {
            "mcpServer": capo_bedrock_agentcore_control.types.mcp_server_target_configuration.deserialize_json(
                data["mcpServer"]
            )
        }
    elif data.get("apiGateway") is not None:
        import capo_bedrock_agentcore_control.types.api_gateway_target_configuration

        return {
            "apiGateway": capo_bedrock_agentcore_control.types.api_gateway_target_configuration.deserialize_json(
                data["apiGateway"]
            )
        }
    elif data.get("connector") is not None:
        import capo_bedrock_agentcore_control.types.connector_target_configuration

        return {
            "connector": capo_bedrock_agentcore_control.types.connector_target_configuration.deserialize_json(
                data["connector"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("McpTargetConfiguration: no recognized variant key")


def redact_sensitive(value: McpTargetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "openApiSchema" in value:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        out["openApiSchema"] = (
            capo_bedrock_agentcore_control.types.api_schema_configuration.redact_sensitive(
                value["openApiSchema"]
            )
        )
    if "smithyModel" in value:
        import capo_bedrock_agentcore_control.types.api_schema_configuration

        out["smithyModel"] = (
            capo_bedrock_agentcore_control.types.api_schema_configuration.redact_sensitive(
                value["smithyModel"]
            )
        )
    if "lambda" in value:
        import capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration

        out["lambda"] = (
            capo_bedrock_agentcore_control.types.mcp_lambda_target_configuration.redact_sensitive(
                value["lambda"]
            )
        )
    if "mcpServer" in value:
        import capo_bedrock_agentcore_control.types.mcp_server_target_configuration

        out["mcpServer"] = (
            capo_bedrock_agentcore_control.types.mcp_server_target_configuration.redact_sensitive(
                value["mcpServer"]
            )
        )
    return out
