"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListMigrationWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_summary_list
    import capo_migrationhuborchestrator.types.next_token


class ListMigrationWorkflowsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    migration_workflow_summary: "capo_migrationhuborchestrator.types.migration_workflow_summary_list.MigrationWorkflowSummaryList"
    """<p>The summary of the migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationWorkflowsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_migrationhuborchestrator.types.migration_workflow_summary_list

    out["migrationWorkflowSummary"] = (
        capo_migrationhuborchestrator.types.migration_workflow_summary_list.serialize_json(
            value["migration_workflow_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMigrationWorkflowsResponse:
    out: ListMigrationWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("migrationWorkflowSummary") is not None:
        import capo_migrationhuborchestrator.types.migration_workflow_summary_list

        out["migration_workflow_summary"] = (
            capo_migrationhuborchestrator.types.migration_workflow_summary_list.deserialize_json(
                data["migrationWorkflowSummary"]
            )
        )
    else:
        out["migration_workflow_summary"] = []
    return out
