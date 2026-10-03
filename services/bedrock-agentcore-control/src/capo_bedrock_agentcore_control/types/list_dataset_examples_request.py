"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetExamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_version


class ListDatasetExamplesRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_version: NotRequired[
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    ]
    """<p> Version to paginate: "DRAFT" or a version number. Defaults to DRAFT if absent. Only used on the first request; for subsequent pages, the version is extracted from the pagination token. </p>"""
    max_results: NotRequired["int"]
    """<p> Maximum number of examples to return per page. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExamplesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetExamplesRequest:
    out: ListDatasetExamplesRequest = {}  # type: ignore[typeddict-item]
    return out
