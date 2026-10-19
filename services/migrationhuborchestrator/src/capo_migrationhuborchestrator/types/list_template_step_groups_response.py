"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListTemplateStepGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_step_group_summary_list


class ListTemplateStepGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_step_group_summary: "capo_migrationhuborchestrator.types.template_step_group_summary_list.TemplateStepGroupSummaryList"
    """<p>The summary of the step group in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateStepGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_migrationhuborchestrator.types.template_step_group_summary_list

    out["templateStepGroupSummary"] = (
        capo_migrationhuborchestrator.types.template_step_group_summary_list.serialize_json(
            value["template_step_group_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTemplateStepGroupsResponse:
    out: ListTemplateStepGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("templateStepGroupSummary") is not None:
        import capo_migrationhuborchestrator.types.template_step_group_summary_list

        out["template_step_group_summary"] = (
            capo_migrationhuborchestrator.types.template_step_group_summary_list.deserialize_json(
                data["templateStepGroupSummary"]
            )
        )
    else:
        out["template_step_group_summary"] = []
    return out
