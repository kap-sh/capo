"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MemoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enabled_memory_types
    import capo_bedrock_agent.types.session_summary_configuration
    import capo_bedrock_agent.types.storage_days


class MemoryConfiguration(TypedDict, closed=True):
    enabled_memory_types: (
        "capo_bedrock_agent.types.enabled_memory_types.EnabledMemoryTypes"
    )
    """<p>The type of memory that is stored. </p>"""
    storage_days: "capo_bedrock_agent.types.storage_days.StorageDays"
    """<p>The number of days the agent is configured to retain the conversational context.</p>"""
    session_summary_configuration: NotRequired[
        "capo_bedrock_agent.types.session_summary_configuration.SessionSummaryConfiguration"
    ]
    """<p>Contains the configuration for SESSION_SUMMARY memory type enabled for the agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enabled_memory_types

    out["enabledMemoryTypes"] = (
        capo_bedrock_agent.types.enabled_memory_types.serialize_json(
            value["enabled_memory_types"]
        )
    )
    out["storageDays"] = value.get("storage_days", 30)
    if "session_summary_configuration" in value:
        import capo_bedrock_agent.types.session_summary_configuration

        out["sessionSummaryConfiguration"] = (
            capo_bedrock_agent.types.session_summary_configuration.serialize_json(
                value["session_summary_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryConfiguration:
    out: MemoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabledMemoryTypes") is not None:
        import capo_bedrock_agent.types.enabled_memory_types

        out["enabled_memory_types"] = (
            capo_bedrock_agent.types.enabled_memory_types.deserialize_json(
                data["enabledMemoryTypes"]
            )
        )
    else:
        out["enabled_memory_types"] = []
    if data.get("storageDays") is not None:
        out["storage_days"] = data["storageDays"]
    else:
        out["storage_days"] = 30
    if data.get("sessionSummaryConfiguration") is not None:
        import capo_bedrock_agent.types.session_summary_configuration

        out["session_summary_configuration"] = (
            capo_bedrock_agent.types.session_summary_configuration.deserialize_json(
                data["sessionSummaryConfiguration"]
            )
        )
    return out
