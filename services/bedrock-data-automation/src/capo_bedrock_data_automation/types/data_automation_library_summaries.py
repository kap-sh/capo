"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibrarySummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_summary

DataAutomationLibrarySummaries: TypeAlias = list[
    "capo_bedrock_data_automation.types.data_automation_library_summary.DataAutomationLibrarySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibrarySummaries) -> list:
    import capo_bedrock_data_automation.types.data_automation_library_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibrarySummaries:
    import capo_bedrock_data_automation.types.data_automation_library_summary

    out: DataAutomationLibrarySummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DataAutomationLibrarySummaries) -> list[Any]:
    import capo_bedrock_data_automation.types.data_automation_library_summary

    return [
        capo_bedrock_data_automation.types.data_automation_library_summary.redact_sensitive(
            item
        )
        for item in value
    ]
