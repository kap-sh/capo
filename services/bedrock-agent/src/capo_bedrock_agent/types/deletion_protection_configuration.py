"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeletionProtectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.enabled_or_disabled_state


class DeletionProtectionConfiguration(TypedDict, closed=True):
    deletion_protection_status: (
        "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState"
    )
    """<p>Enable or disable deletion protection for the connector.</p>"""
    deletion_protection_threshold: "int"
    """<p>The threshold is the maximum percentage of documents that a sync job can delete from your index. If a sync would delete more than this percentage, the sync skips its delete phase, leaving your indexed documents in place. Not supported for the Custom connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletionProtectionConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.enabled_or_disabled_state

    out["deletionProtectionStatus"] = (
        capo_bedrock_agent.types.enabled_or_disabled_state.serialize_json(
            value["deletion_protection_status"]
        )
    )
    out["deletionProtectionThreshold"] = value.get("deletion_protection_threshold", 15)
    return out


def deserialize_json(data: dict) -> DeletionProtectionConfiguration:
    out: DeletionProtectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("deletionProtectionStatus") is not None:
        import capo_bedrock_agent.types.enabled_or_disabled_state

        out["deletion_protection_status"] = (
            capo_bedrock_agent.types.enabled_or_disabled_state.deserialize_json(
                data["deletionProtectionStatus"]
            )
        )
    else:
        import typing

        out["deletion_protection_status"] = typing.cast(
            "capo_bedrock_agent.types.enabled_or_disabled_state.EnabledOrDisabledState",
            "",
        )
    if data.get("deletionProtectionThreshold") is not None:
        out["deletion_protection_threshold"] = data["deletionProtectionThreshold"]
    else:
        out["deletion_protection_threshold"] = 15
    return out
