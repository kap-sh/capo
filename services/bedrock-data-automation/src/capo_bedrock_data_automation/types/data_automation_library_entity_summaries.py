"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryEntitySummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary

DataAutomationLibraryEntitySummaries: TypeAlias = list[
    "capo_bedrock_data_automation.types.data_automation_library_entity_summary.DataAutomationLibraryEntitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryEntitySummaries) -> list:
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_entity_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibraryEntitySummaries:
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary

    out: DataAutomationLibraryEntitySummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_entity_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DataAutomationLibraryEntitySummaries) -> list[Any]:
    import capo_bedrock_data_automation.types.data_automation_library_entity_summary

    return [
        capo_bedrock_data_automation.types.data_automation_library_entity_summary.redact_sensitive(
            item
        )
        for item in value
    ]
