"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpLambdaTargetConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_function_arn
    import capo_bedrock_agentcore_control.types.tool_schema


class McpLambdaTargetConfiguration(TypedDict, closed=True):
    lambda_arn: (
        "capo_bedrock_agentcore_control.types.lambda_function_arn.LambdaFunctionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to communicate with the target.</p>"""
    tool_schema: "capo_bedrock_agentcore_control.types.tool_schema.ToolSchema"
    """<p>The tool schema for the Lambda function. This schema defines the structure of the tools that the Lambda function provides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpLambdaTargetConfiguration) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    import capo_bedrock_agentcore_control.types.tool_schema

    out["toolSchema"] = capo_bedrock_agentcore_control.types.tool_schema.serialize_json(
        value["tool_schema"]
    )
    return out


def deserialize_json(data: dict) -> McpLambdaTargetConfiguration:
    out: McpLambdaTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        out["lambda_arn"] = ""
    if data.get("toolSchema") is not None:
        import capo_bedrock_agentcore_control.types.tool_schema

        out["tool_schema"] = (
            capo_bedrock_agentcore_control.types.tool_schema.deserialize_json(
                data["toolSchema"]
            )
        )
    else:
        out["tool_schema"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: McpLambdaTargetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tool_schema" in value:
        import capo_bedrock_agentcore_control.types.tool_schema

        out["tool_schema"] = (
            capo_bedrock_agentcore_control.types.tool_schema.redact_sensitive(
                value["tool_schema"]
            )
        )
    return out
