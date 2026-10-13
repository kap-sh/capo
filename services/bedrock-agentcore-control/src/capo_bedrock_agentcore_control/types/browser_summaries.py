"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_summary

BrowserSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.browser_summary.BrowserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSummaries) -> list:
    import capo_bedrock_agentcore_control.types.browser_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.browser_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BrowserSummaries:
    import capo_bedrock_agentcore_control.types.browser_summary

    out: BrowserSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.browser_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BrowserSummaries) -> list[Any]:
    import capo_bedrock_agentcore_control.types.browser_summary

    return [
        capo_bedrock_agentcore_control.types.browser_summary.redact_sensitive(item)
        for item in value
    ]
