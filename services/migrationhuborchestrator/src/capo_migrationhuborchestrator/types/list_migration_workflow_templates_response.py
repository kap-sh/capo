"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.template_summary_list


class ListMigrationWorkflowTemplatesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    template_summary: (
        "capo_migrationhuborchestrator.types.template_summary_list.TemplateSummaryList"
    )
    """<p>The summary of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowTemplatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_migrationhuborchestrator.types.template_summary_list

    out["templateSummary"] = (
        capo_migrationhuborchestrator.types.template_summary_list.serialize_json(
            value["template_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowTemplatesResponse:
    out: ListMigrationWorkflowTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("templateSummary") is not None:
        import capo_migrationhuborchestrator.types.template_summary_list

        out["template_summary"] = (
            capo_migrationhuborchestrator.types.template_summary_list.deserialize_json(
                data["templateSummary"]
            )
        )
    else:
        out["template_summary"] = []
    return out
