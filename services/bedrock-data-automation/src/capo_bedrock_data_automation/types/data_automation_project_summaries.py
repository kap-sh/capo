"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_summary

DataAutomationProjectSummaries: TypeAlias = list[
    "capo_bedrock_data_automation.types.data_automation_project_summary.DataAutomationProjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectSummaries) -> list:
    import capo_bedrock_data_automation.types.data_automation_project_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.data_automation_project_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationProjectSummaries:
    import capo_bedrock_data_automation.types.data_automation_project_summary

    out: DataAutomationProjectSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.data_automation_project_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DataAutomationProjectSummaries) -> list[Any]:
    import capo_bedrock_data_automation.types.data_automation_project_summary

    return [
        capo_bedrock_data_automation.types.data_automation_project_summary.redact_sensitive(
            item
        )
        for item in value
    ]
