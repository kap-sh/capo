"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibrariesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_summaries
    import capo_bedrock_data_automation.types.next_token


class ListDataAutomationLibrariesResponse(TypedDict, closed=True):
    libraries: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_summaries.DataAutomationLibrarySummaries"
    ]
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibrariesResponse) -> dict:
    out: dict = {}
    if "libraries" in value:
        import capo_bedrock_data_automation.types.data_automation_library_summaries

        out["libraries"] = (
            capo_bedrock_data_automation.types.data_automation_library_summaries.serialize_json(
                value["libraries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibrariesResponse:
    out: ListDataAutomationLibrariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("libraries") is not None:
        import capo_bedrock_data_automation.types.data_automation_library_summaries

        out["libraries"] = (
            capo_bedrock_data_automation.types.data_automation_library_summaries.deserialize_json(
                data["libraries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDataAutomationLibrariesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "libraries" in value:
        import capo_bedrock_data_automation.types.data_automation_library_summaries

        out["libraries"] = (
            capo_bedrock_data_automation.types.data_automation_library_summaries.redact_sensitive(
                value["libraries"]
            )
        )
    return out
