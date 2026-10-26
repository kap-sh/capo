"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessToolConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_browser_config
    import capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config
    import capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config
    import capo_bedrock_agentcore_control.types.harness_inline_function_config
    import capo_bedrock_agentcore_control.types.harness_remote_mcp_config


class _HarnessToolConfiguration_remoteMcp(TypedDict, closed=True):
    remoteMcp: "capo_bedrock_agentcore_control.types.harness_remote_mcp_config.HarnessRemoteMcpConfig"


class _HarnessToolConfiguration_agentCoreBrowser(TypedDict, closed=True):
    agentCoreBrowser: "capo_bedrock_agentcore_control.types.harness_agent_core_browser_config.HarnessAgentCoreBrowserConfig"


class _HarnessToolConfiguration_agentCoreGateway(TypedDict, closed=True):
    agentCoreGateway: "capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config.HarnessAgentCoreGatewayConfig"


class _HarnessToolConfiguration_inlineFunction(TypedDict, closed=True):
    inlineFunction: "capo_bedrock_agentcore_control.types.harness_inline_function_config.HarnessInlineFunctionConfig"


class _HarnessToolConfiguration_agentCoreCodeInterpreter(TypedDict, closed=True):
    agentCoreCodeInterpreter: "capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.HarnessAgentCoreCodeInterpreterConfig"


HarnessToolConfiguration: TypeAlias = (
    _HarnessToolConfiguration_remoteMcp
    | _HarnessToolConfiguration_agentCoreBrowser
    | _HarnessToolConfiguration_agentCoreGateway
    | _HarnessToolConfiguration_inlineFunction
    | _HarnessToolConfiguration_agentCoreCodeInterpreter
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessToolConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "remoteMcp" in value:
        import capo_bedrock_agentcore_control.types.harness_remote_mcp_config

        return {
            "remoteMcp": capo_bedrock_agentcore_control.types.harness_remote_mcp_config.serialize_json(
                value["remoteMcp"]
            )
        }
    elif "agentCoreBrowser" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_browser_config

        return {
            "agentCoreBrowser": capo_bedrock_agentcore_control.types.harness_agent_core_browser_config.serialize_json(
                value["agentCoreBrowser"]
            )
        }
    elif "agentCoreGateway" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config

        return {
            "agentCoreGateway": capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config.serialize_json(
                value["agentCoreGateway"]
            )
        }
    elif "inlineFunction" in value:
        import capo_bedrock_agentcore_control.types.harness_inline_function_config

        return {
            "inlineFunction": capo_bedrock_agentcore_control.types.harness_inline_function_config.serialize_json(
                value["inlineFunction"]
            )
        }
    elif "agentCoreCodeInterpreter" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config

        return {
            "agentCoreCodeInterpreter": capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.serialize_json(
                value["agentCoreCodeInterpreter"]
            )
        }
    else:
        raise SerializationError("HarnessToolConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessToolConfiguration:
    if data.get("remoteMcp") is not None:
        import capo_bedrock_agentcore_control.types.harness_remote_mcp_config

        return {
            "remoteMcp": capo_bedrock_agentcore_control.types.harness_remote_mcp_config.deserialize_json(
                data["remoteMcp"]
            )
        }
    elif data.get("agentCoreBrowser") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_browser_config

        return {
            "agentCoreBrowser": capo_bedrock_agentcore_control.types.harness_agent_core_browser_config.deserialize_json(
                data["agentCoreBrowser"]
            )
        }
    elif data.get("agentCoreGateway") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config

        return {
            "agentCoreGateway": capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config.deserialize_json(
                data["agentCoreGateway"]
            )
        }
    elif data.get("inlineFunction") is not None:
        import capo_bedrock_agentcore_control.types.harness_inline_function_config

        return {
            "inlineFunction": capo_bedrock_agentcore_control.types.harness_inline_function_config.deserialize_json(
                data["inlineFunction"]
            )
        }
    elif data.get("agentCoreCodeInterpreter") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config

        return {
            "agentCoreCodeInterpreter": capo_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.deserialize_json(
                data["agentCoreCodeInterpreter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessToolConfiguration: no recognized variant key"
        )


def redact_sensitive(value: HarnessToolConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remoteMcp" in value:
        import capo_bedrock_agentcore_control.types.harness_remote_mcp_config

        out["remoteMcp"] = (
            capo_bedrock_agentcore_control.types.harness_remote_mcp_config.redact_sensitive(
                value["remoteMcp"]
            )
        )
    if "agentCoreGateway" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config

        out["agentCoreGateway"] = (
            capo_bedrock_agentcore_control.types.harness_agent_core_gateway_config.redact_sensitive(
                value["agentCoreGateway"]
            )
        )
    if "inlineFunction" in value:
        import capo_bedrock_agentcore_control.types.harness_inline_function_config

        out["inlineFunction"] = (
            capo_bedrock_agentcore_control.types.harness_inline_function_config.redact_sensitive(
                value["inlineFunction"]
            )
        )
    return out
