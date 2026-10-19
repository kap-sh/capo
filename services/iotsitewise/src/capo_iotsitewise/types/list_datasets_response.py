"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_summaries
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.workspace_name


class ListDatasetsResponse(TypedDict, closed=True):
    dataset_summaries: "capo_iotsitewise.types.dataset_summaries.DatasetSummaries"
    """<p>A list that summarizes the dataset response.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.dataset_summaries

    out["datasetSummaries"] = capo_iotsitewise.types.dataset_summaries.serialize_json(
        value["dataset_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetSummaries") is not None:
        import capo_iotsitewise.types.dataset_summaries

        out["dataset_summaries"] = (
            capo_iotsitewise.types.dataset_summaries.deserialize_json(
                data["datasetSummaries"]
            )
        )
    else:
        out["dataset_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    return out
