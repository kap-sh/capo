"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.list_dataset_versions_filter


class ListDatasetVersionsRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    filter: NotRequired[
        "capo_bedrock_agentcore_control.types.list_dataset_versions_filter.ListDatasetVersionsFilter"
    ]
    """<p> A filter to apply to the dataset versions. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of versions to return per page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetVersionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_bedrock_agentcore_control.types.list_dataset_versions_filter

        out["filter"] = (
            capo_bedrock_agentcore_control.types.list_dataset_versions_filter.serialize_json(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListDatasetVersionsRequest:
    out: ListDatasetVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_bedrock_agentcore_control.types.list_dataset_versions_filter

        out["filter"] = (
            capo_bedrock_agentcore_control.types.list_dataset_versions_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
