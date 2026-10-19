"""Generated from Smithy shape ``com.amazonaws.novaact#ListWorkflowDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.next_token
    import capo_nova_act.types.workflow_definition_summaries


class ListWorkflowDefinitionsResponse(TypedDict, closed=True):
    workflow_definition_summaries: (
        "capo_nova_act.types.workflow_definition_summaries.WorkflowDefinitionSummaries"
    )
    """<p>A list of summary information for workflow definitions.</p>"""
    next_token: NotRequired["capo_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_definition_summaries

    out["workflowDefinitionSummaries"] = (
        capo_nova_act.types.workflow_definition_summaries.serialize_json(
            value["workflow_definition_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowDefinitionsResponse:
    out: ListWorkflowDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("workflowDefinitionSummaries") is not None:
        import capo_nova_act.types.workflow_definition_summaries

        out["workflow_definition_summaries"] = (
            capo_nova_act.types.workflow_definition_summaries.deserialize_json(
                data["workflowDefinitionSummaries"]
            )
        )
    else:
        out["workflow_definition_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
