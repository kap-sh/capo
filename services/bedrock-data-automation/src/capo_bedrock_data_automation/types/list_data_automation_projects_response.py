"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationProjectsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_summaries
    import capo_bedrock_data_automation.types.next_token


class ListDataAutomationProjectsResponse(TypedDict, closed=True):
    projects: "capo_bedrock_data_automation.types.data_automation_project_summaries.DataAutomationProjectSummaries"
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationProjectsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.data_automation_project_summaries

    out["projects"] = (
        capo_bedrock_data_automation.types.data_automation_project_summaries.serialize_json(
            value["projects"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationProjectsResponse:
    out: ListDataAutomationProjectsResponse = {}  # type: ignore[typeddict-item]
    if data.get("projects") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_summaries

        out["projects"] = (
            capo_bedrock_data_automation.types.data_automation_project_summaries.deserialize_json(
                data["projects"]
            )
        )
    else:
        raise DeserializationError(
            "ListDataAutomationProjectsResponse.projects required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListDataAutomationProjectsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "projects" in value:
        import capo_bedrock_data_automation.types.data_automation_project_summaries

        out["projects"] = (
            capo_bedrock_data_automation.types.data_automation_project_summaries.redact_sensitive(
                value["projects"]
            )
        )
    return out
