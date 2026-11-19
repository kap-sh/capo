"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetExamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_version
    import capo_bedrock_agentcore_control.types.list_dataset_examples_filter


class ListDatasetExamplesRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_version: NotRequired[
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    ]
    """<p> Version to paginate: "DRAFT" or a version number. Defaults to DRAFT if absent on the first request. With a pagination token, the version comes from the token: you can omit this member, and a value that differs from the token's version is rejected with a <code>ValidationException</code>. </p>"""
    filter: NotRequired[
        "capo_bedrock_agentcore_control.types.list_dataset_examples_filter.ListDatasetExamplesFilter"
    ]
    """<p> A filter to apply to the examples. </p>"""
    max_results: NotRequired["int"]
    """<p> Maximum number of examples to return per page. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExamplesRequest) -> dict:
    out: dict = {}
    if "dataset_version" in value:
        out["datasetVersion"] = value["dataset_version"]
    if "filter" in value:
        import capo_bedrock_agentcore_control.types.list_dataset_examples_filter

        out["filter"] = (
            capo_bedrock_agentcore_control.types.list_dataset_examples_filter.serialize_json(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetExamplesRequest:
    out: ListDatasetExamplesRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    if data.get("filter") is not None:
        import capo_bedrock_agentcore_control.types.list_dataset_examples_filter

        out["filter"] = (
            capo_bedrock_agentcore_control.types.list_dataset_examples_filter.deserialize_json(
                data["filter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
