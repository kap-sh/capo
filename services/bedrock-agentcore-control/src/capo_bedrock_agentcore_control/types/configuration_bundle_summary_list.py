"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary

ConfigurationBundleSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.configuration_bundle_summary.ConfigurationBundleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.configuration_bundle_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationBundleSummaryList:
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary

    out: ConfigurationBundleSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.configuration_bundle_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ConfigurationBundleSummaryList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary

    return [
        capo_bedrock_agentcore_control.types.configuration_bundle_summary.redact_sensitive(
            item
        )
        for item in value
    ]
