"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_summary

BrowserProfileSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.browser_profile_summary.BrowserProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileSummaries) -> list:
    import capo_bedrock_agentcore_control.types.browser_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.browser_profile_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BrowserProfileSummaries:
    import capo_bedrock_agentcore_control.types.browser_profile_summary

    out: BrowserProfileSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.browser_profile_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BrowserProfileSummaries) -> list[Any]:
    import capo_bedrock_agentcore_control.types.browser_profile_summary

    return [
        capo_bedrock_agentcore_control.types.browser_profile_summary.redact_sensitive(
            item
        )
        for item in value
    ]
