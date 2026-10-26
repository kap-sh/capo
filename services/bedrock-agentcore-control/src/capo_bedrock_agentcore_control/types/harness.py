"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Harness``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.harness_allowed_tools
    import capo_bedrock_agentcore_control.types.harness_arn
    import capo_bedrock_agentcore_control.types.harness_environment_artifact
    import capo_bedrock_agentcore_control.types.harness_environment_provider
    import capo_bedrock_agentcore_control.types.harness_hooks
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_model_configuration
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_skills
    import capo_bedrock_agentcore_control.types.harness_status
    import capo_bedrock_agentcore_control.types.harness_system_prompt
    import capo_bedrock_agentcore_control.types.harness_tools
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration
    import capo_bedrock_agentcore_control.types.harness_version
    import capo_bedrock_agentcore_control.types.role_arn


class Harness(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness.</p>"""
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness.</p>"""
    arn: "capo_bedrock_agentcore_control.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness.</p>"""
    status: "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus"
    """<p>The status of the harness.</p>"""
    harness_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The version of the harness. Incremented on every successful UpdateHarness.</p>"""
    execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>IAM role the harness assumes when running.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The createdAt time of the harness.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The updatedAt time of the harness.</p>"""
    model: "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
    """<p>The configuration of the default model used by the Harness.</p>"""
    system_prompt: (
        "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
    )
    """<p>The system prompt of the harness.</p>"""
    tools: "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
    """<p>The tools of the harness.</p>"""
    skills: "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
    """<p>The skills of the harness.</p>"""
    allowed_tools: (
        "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
    )
    """<p>The allowed tools of the harness. All tools are allowed by default.</p>"""
    truncation: "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
    """<p>Configuration for truncating model context.</p>"""
    environment: "capo_bedrock_agentcore_control.types.harness_environment_provider.HarnessEnvironmentProvider"
    """<p>The compute environment on which the Harness runs.</p>"""
    environment_artifact: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
    ]
    """<p>The environment artifact (e.g., container) in which the Harness operates.</p>"""
    environment_variables: NotRequired[
        "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables exposed in the environment in which the harness operates.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    memory: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>AgentCore Memory instance configuration for short and long term memory.</p>"""
    hooks: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
    ]
    """<p>The lifecycle hooks configured for the harness.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations in the agent loop allowed before exiting per invocation.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration per invocation.</p>"""
    failure_reason: NotRequired["str"]
    """<p>Reason why create or update operations fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Harness) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["arn"] = value["arn"]
    import capo_bedrock_agentcore_control.types.harness_status

    out["status"] = capo_bedrock_agentcore_control.types.harness_status.serialize_json(
        value["status"]
    )
    if "harness_version" in value:
        out["harnessVersion"] = value["harness_version"]
    out["executionRoleArn"] = value["execution_role_arn"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.harness_model_configuration

    out["model"] = (
        capo_bedrock_agentcore_control.types.harness_model_configuration.serialize_json(
            value["model"]
        )
    )
    import capo_bedrock_agentcore_control.types.harness_system_prompt

    out["systemPrompt"] = (
        capo_bedrock_agentcore_control.types.harness_system_prompt.serialize_json(
            value["system_prompt"]
        )
    )
    import capo_bedrock_agentcore_control.types.harness_tools

    out["tools"] = capo_bedrock_agentcore_control.types.harness_tools.serialize_json(
        value["tools"]
    )
    import capo_bedrock_agentcore_control.types.harness_skills

    out["skills"] = capo_bedrock_agentcore_control.types.harness_skills.serialize_json(
        value["skills"]
    )
    import capo_bedrock_agentcore_control.types.harness_allowed_tools

    out["allowedTools"] = (
        capo_bedrock_agentcore_control.types.harness_allowed_tools.serialize_json(
            value["allowed_tools"]
        )
    )
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration

    out["truncation"] = (
        capo_bedrock_agentcore_control.types.harness_truncation_configuration.serialize_json(
            value["truncation"]
        )
    )
    import capo_bedrock_agentcore_control.types.harness_environment_provider

    out["environment"] = (
        capo_bedrock_agentcore_control.types.harness_environment_provider.serialize_json(
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
    if "memory" in value:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["memory"]
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
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> Harness:
    out: Harness = {}  # type: ignore[typeddict-item]
    if data.get("harnessId") is not None:
        out["harness_id"] = data["harnessId"]
    else:
        out["harness_id"] = ""
    if data.get("harnessName") is not None:
        out["harness_name"] = data["harnessName"]
    else:
        out["harness_name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.harness_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.harness_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus", ""
        )
    if data.get("harnessVersion") is not None:
        out["harness_version"] = data["harnessVersion"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("model") is not None:
        import capo_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            capo_bedrock_agentcore_control.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    else:
        out["model"] = {"$unknown": {"name": ""}}
    if data.get("systemPrompt") is not None:
        import capo_bedrock_agentcore_control.types.harness_system_prompt

        out["system_prompt"] = (
            capo_bedrock_agentcore_control.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    else:
        out["system_prompt"] = []
    if data.get("tools") is not None:
        import capo_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            capo_bedrock_agentcore_control.types.harness_tools.deserialize_json(
                data["tools"]
            )
        )
    else:
        out["tools"] = []
    if data.get("skills") is not None:
        import capo_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            capo_bedrock_agentcore_control.types.harness_skills.deserialize_json(
                data["skills"]
            )
        )
    else:
        out["skills"] = []
    if data.get("allowedTools") is not None:
        import capo_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowed_tools"] = (
            capo_bedrock_agentcore_control.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    else:
        out["allowed_tools"] = []
    if data.get("truncation") is not None:
        import capo_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            capo_bedrock_agentcore_control.types.harness_truncation_configuration.deserialize_json(
                data["truncation"]
            )
        )
    else:
        raise DeserializationError("Harness.truncation required")
    if data.get("environment") is not None:
        import capo_bedrock_agentcore_control.types.harness_environment_provider

        out["environment"] = (
            capo_bedrock_agentcore_control.types.harness_environment_provider.deserialize_json(
                data["environment"]
            )
        )
    else:
        out["environment"] = {"$unknown": {"name": ""}}
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
    if data.get("memory") is not None:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["memory"]
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
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out


def redact_sensitive(value: Harness) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
