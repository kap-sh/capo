"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateHarnessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.harness_allowed_tools
    import capo_bedrock_agentcore_control.types.harness_environment_artifact
    import capo_bedrock_agentcore_control.types.harness_environment_provider_request
    import capo_bedrock_agentcore_control.types.harness_hooks
    import capo_bedrock_agentcore_control.types.harness_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_model_configuration
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_skills
    import capo_bedrock_agentcore_control.types.harness_system_prompt
    import capo_bedrock_agentcore_control.types.harness_tools
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.tags_map


class CreateHarnessRequest(TypedDict, closed=True):
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.</p>"""
    environment: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
    ]
    """<p>The compute environment configuration for the harness, including network and lifecycle settings.</p>"""
    environment_artifact: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
    ]
    """<p>The environment artifact for the harness, such as a custom container image containing additional dependencies.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables to set in the harness runtime environment.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    model: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
    ]
    """<p>The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.</p>"""
    system_prompt: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
    ]
    """<p>The system prompt that defines the agent's behavior and instructions.</p>"""
    tools: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
    ]
    """<p>The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.</p>"""
    skills: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
    ]
    """<p>The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.</p>"""
    allowed_tools: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
    ]
    """<p>The tools that the agent is allowed to use. Supports glob patterns such as * for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.</p>"""
    memory: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>The AgentCore Memory configuration for persisting conversation context across sessions.</p>"""
    truncation: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
    ]
    """<p>The truncation configuration for managing conversation context when it exceeds model limits.</p>"""
    hooks: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
    ]
    """<p>The lifecycle hooks to run at defined points in the agent loop.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations the agent loop can execute per invocation.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds for the agent loop execution per invocation.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>Tags to apply to the harness resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarnessRequest) -> dict:
    out: dict = {}
    out["harnessName"] = value["harness_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "environment" in value:
        import capo_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            capo_bedrock_agentcore_control.types.harness_environment_provider_request.serialize_json(
                value["environment"]
            )
        )
    if "environment_artifact" in value:
        import capo_bedrock_agentcore_control.types.harness_environment_artifact

        out["environmentArtifact"] = (
            capo_bedrock_agentcore_control.types.harness_environment_artifact.serialize_json(
                value["environment_artifact"]
            )
        )
    if "environment_variables" in value:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environmentVariables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "model" in value:
        import capo_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore_control.types.harness_model_configuration.serialize_json(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import capo_bedrock_agentcore_control.types.harness_system_prompt

        out["systemPrompt"] = (
            capo_bedrock_agentcore_control.types.harness_system_prompt.serialize_json(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import capo_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            capo_bedrock_agentcore_control.types.harness_tools.serialize_json(
                value["tools"]
            )
        )
    if "skills" in value:
        import capo_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            capo_bedrock_agentcore_control.types.harness_skills.serialize_json(
                value["skills"]
            )
        )
    if "allowed_tools" in value:
        import capo_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowedTools"] = (
            capo_bedrock_agentcore_control.types.harness_allowed_tools.serialize_json(
                value["allowed_tools"]
            )
        )
    if "memory" in value:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["memory"]
            )
        )
    if "truncation" in value:
        import capo_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_configuration.serialize_json(
                value["truncation"]
            )
        )
    if "hooks" in value:
        import capo_bedrock_agentcore_control.types.harness_hooks

        out["hooks"] = (
            capo_bedrock_agentcore_control.types.harness_hooks.serialize_json(
                value["hooks"]
            )
        )
    if "max_iterations" in value:
        out["maxIterations"] = value["max_iterations"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateHarnessRequest:
    out: CreateHarnessRequest = {}  # type: ignore[typeddict-item]
    if data.get("harnessName") is not None:
        out["harness_name"] = data["harnessName"]
    else:
        out["harness_name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("environment") is not None:
        import capo_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            capo_bedrock_agentcore_control.types.harness_environment_provider_request.deserialize_json(
                data["environment"]
            )
        )
    if data.get("environmentArtifact") is not None:
        import capo_bedrock_agentcore_control.types.harness_environment_artifact

        out["environment_artifact"] = (
            capo_bedrock_agentcore_control.types.harness_environment_artifact.deserialize_json(
                data["environmentArtifact"]
            )
        )
    if data.get("environmentVariables") is not None:
        import capo_bedrock_agentcore_control.types.environment_variables_map

        out["environment_variables"] = (
            capo_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("model") is not None:
        import capo_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore_control.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    if data.get("systemPrompt") is not None:
        import capo_bedrock_agentcore_control.types.harness_system_prompt

        out["system_prompt"] = (
            capo_bedrock_agentcore_control.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    if data.get("tools") is not None:
        import capo_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            capo_bedrock_agentcore_control.types.harness_tools.deserialize_json(
                data["tools"]
            )
        )
    if data.get("skills") is not None:
        import capo_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            capo_bedrock_agentcore_control.types.harness_skills.deserialize_json(
                data["skills"]
            )
        )
    if data.get("allowedTools") is not None:
        import capo_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowed_tools"] = (
            capo_bedrock_agentcore_control.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    if data.get("memory") is not None:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["memory"]
            )
        )
    if data.get("truncation") is not None:
        import capo_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_configuration.deserialize_json(
                data["truncation"]
            )
        )
    if data.get("hooks") is not None:
        import capo_bedrock_agentcore_control.types.harness_hooks

        out["hooks"] = (
            capo_bedrock_agentcore_control.types.harness_hooks.deserialize_json(
                data["hooks"]
            )
        )
    if data.get("maxIterations") is not None:
        out["max_iterations"] = data["maxIterations"]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateHarnessRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        import capo_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore_control.types.harness_model_configuration.redact_sensitive(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import capo_bedrock_agentcore_control.types.harness_system_prompt

        out["system_prompt"] = (
            capo_bedrock_agentcore_control.types.harness_system_prompt.redact_sensitive(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import capo_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            capo_bedrock_agentcore_control.types.harness_tools.redact_sensitive(
                value["tools"]
            )
        )
    return out
