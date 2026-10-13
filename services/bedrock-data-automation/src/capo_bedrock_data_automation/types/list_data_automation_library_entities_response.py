"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibraryEntitiesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_entity_summaries
    import capo_bedrock_data_automation.types.next_token


class ListDataAutomationLibraryEntitiesResponse(TypedDict, closed=True):
    entities: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_entity_summaries.DataAutomationLibraryEntitySummaries"
    ]
    """List of entities"""
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]
    """Pagination token for retrieving the next set of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibraryEntitiesResponse) -> dict:
    out: dict = {}
    if "entities" in value:
        import capo_bedrock_data_automation.types.data_automation_library_entity_summaries

        out["entities"] = (
            capo_bedrock_data_automation.types.data_automation_library_entity_summaries.serialize_json(
                value["entities"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibraryEntitiesResponse:
    out: ListDataAutomationLibraryEntitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_bedrock_data_automation.types.data_automation_library_entity_summaries

        out["entities"] = (
            capo_bedrock_data_automation.types.data_automation_library_entity_summaries.deserialize_json(
                data["entities"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(
    value: ListDataAutomationLibraryEntitiesResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entities" in value:
        import capo_bedrock_data_automation.types.data_automation_library_entity_summaries

        out["entities"] = (
            capo_bedrock_data_automation.types.data_automation_library_entity_summaries.redact_sensitive(
                value["entities"]
            )
        )
    return out
