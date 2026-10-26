"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_managed_runtime_type
    import capo_bedrock_agentcore_control.types.code
    import capo_bedrock_agentcore_control.types.entry_points


class CodeConfiguration(TypedDict, closed=True):
    code: "capo_bedrock_agentcore_control.types.code.Code"
    """<p>The source code location and configuration details.</p>"""
    runtime: "capo_bedrock_agentcore_control.types.agent_managed_runtime_type.AgentManagedRuntimeType"
    """<p>The runtime environment for executing the agent code. Specify the programming language and version to use for the agent runtime. For valid values, see the list of supported runtimes.</p>"""
    entry_point: "capo_bedrock_agentcore_control.types.entry_points.EntryPoints"
    """<p>The entry point for the code execution, specifying the function or method that should be invoked when the code runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.code

    out["code"] = capo_bedrock_agentcore_control.types.code.serialize_json(
        value["code"]
    )
    import capo_bedrock_agentcore_control.types.agent_managed_runtime_type

    out["runtime"] = (
        capo_bedrock_agentcore_control.types.agent_managed_runtime_type.serialize_json(
            value["runtime"]
        )
    )
    import capo_bedrock_agentcore_control.types.entry_points

    out["entryPoint"] = (
        capo_bedrock_agentcore_control.types.entry_points.serialize_json(
            value["entry_point"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodeConfiguration:
    out: CodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_bedrock_agentcore_control.types.code

        out["code"] = capo_bedrock_agentcore_control.types.code.deserialize_json(
            data["code"]
        )
    else:
        out["code"] = {"$unknown": {"name": ""}}
    if data.get("runtime") is not None:
        import capo_bedrock_agentcore_control.types.agent_managed_runtime_type

        out["runtime"] = (
            capo_bedrock_agentcore_control.types.agent_managed_runtime_type.deserialize_json(
                data["runtime"]
            )
        )
    else:
        import typing

        out["runtime"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_managed_runtime_type.AgentManagedRuntimeType",
            "",
        )
    if data.get("entryPoint") is not None:
        import capo_bedrock_agentcore_control.types.entry_points

        out["entry_point"] = (
            capo_bedrock_agentcore_control.types.entry_points.deserialize_json(
                data["entryPoint"]
            )
        )
    else:
        out["entry_point"] = []
    return out
