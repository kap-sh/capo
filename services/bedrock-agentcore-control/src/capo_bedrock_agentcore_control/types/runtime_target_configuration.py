"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RuntimeTargetConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_api_schema_configuration
    import capo_bedrock_agentcore_control.types.runtime_arn
    import capo_bedrock_agentcore_control.types.runtime_qualifier


class RuntimeTargetConfiguration(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.runtime_arn.RuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime to route requests to.</p>"""
    qualifier: NotRequired[
        "capo_bedrock_agentcore_control.types.runtime_qualifier.RuntimeQualifier"
    ]
    """<p>The qualifier for the agent runtime, used to target a specific endpoint version. If not specified, the default endpoint is used.</p>"""
    schema: NotRequired[
        "capo_bedrock_agentcore_control.types.http_api_schema_configuration.HttpApiSchemaConfiguration"
    ]
    """<p>The API schema configuration that defines the structure of the runtime target's API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeTargetConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "qualifier" in value:
        out["qualifier"] = value["qualifier"]
    if "schema" in value:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.serialize_json(
                value["schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeTargetConfiguration:
    out: RuntimeTargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("qualifier") is not None:
        out["qualifier"] = data["qualifier"]
    if data.get("schema") is not None:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.deserialize_json(
                data["schema"]
            )
        )
    return out


def redact_sensitive(value: RuntimeTargetConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schema" in value:
        import capo_bedrock_agentcore_control.types.http_api_schema_configuration

        out["schema"] = (
            capo_bedrock_agentcore_control.types.http_api_schema_configuration.redact_sensitive(
                value["schema"]
            )
        )
    return out
