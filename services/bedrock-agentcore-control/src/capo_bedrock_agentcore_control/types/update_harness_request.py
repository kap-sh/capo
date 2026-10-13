"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateHarnessRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.harness_allowed_tools
    import capo_bedrock_agentcore_control.types.harness_environment_provider_request
    import capo_bedrock_agentcore_control.types.harness_hooks
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_model_configuration
    import capo_bedrock_agentcore_control.types.harness_skills
    import capo_bedrock_agentcore_control.types.harness_system_prompt
    import capo_bedrock_agentcore_control.types.harness_tools
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.updated_authorizer_configuration
    import capo_bedrock_agentcore_control.types.updated_harness_environment_artifact
    import capo_bedrock_agentcore_control.types.updated_harness_memory_configuration


class UpdateHarnessRequest(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness to update.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.</p>"""
    environment: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
    ]
    """<p>The compute environment configuration for the harness. If not specified, the existing value is retained.</p>"""
    environment_artifact: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.UpdatedHarnessEnvironmentArtifact"
    ]
    """<p>The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
    ]
    model: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
    ]
    """<p>The model configuration for the harness. If not specified, the existing value is retained.</p>"""
    system_prompt: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
    ]
    """<p>The system prompt that defines the agent's behavior. If not specified, the existing value is retained.</p>"""
    tools: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
    ]
    """<p>The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.</p>"""
    skills: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
    ]
    """<p>The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.</p>"""
    allowed_tools: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
    ]
    """<p>The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.</p>"""
    memory: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.UpdatedHarnessMemoryConfiguration"
    ]
    """<p>The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>"""
    truncation: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
    ]
    """<p>The truncation configuration for managing conversation context. If not specified, the existing value is retained.</p>"""
    hooks: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
    ]
    """<p>The lifecycle hooks to run at defined points in the agent loop. If specified, this replaces all existing hooks. If not specified, the existing hooks are retained.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHarnessRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "environment" in value:
        import capo_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            capo_bedrock_agentcore_control.types.harness_environment_provider_request.serialize_json(
                value["environment"]
            )
        )
    if "environment_artifact" in value:
        import capo_bedrock_agentcore_control.types.updated_harness_environment_artifact

        out["environmentArtifact"] = (
            capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.serialize_json(
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
        import capo_bedrock_agentcore_control.types.updated_authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.updated_authorizer_configuration.serialize_json(
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
        import capo_bedrock_agentcore_control.types.updated_harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.serialize_json(
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
    return out


def deserialize_json(data: dict) -> UpdateHarnessRequest:
    out: UpdateHarnessRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("environment") is not None:
        import capo_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            capo_bedrock_agentcore_control.types.harness_environment_provider_request.deserialize_json(
                data["environment"]
            )
        )
    if data.get("environmentArtifact") is not None:
        import capo_bedrock_agentcore_control.types.updated_harness_environment_artifact

        out["environment_artifact"] = (
            capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.deserialize_json(
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
        import capo_bedrock_agentcore_control.types.updated_authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.updated_authorizer_configuration.deserialize_json(
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
        import capo_bedrock_agentcore_control.types.updated_harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.deserialize_json(
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
    return out


def redact_sensitive(value: UpdateHarnessRequest) -> dict[str, Any]:
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
