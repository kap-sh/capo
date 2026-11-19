"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListDatasetGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_id


class ListDatasetGenerationsRequest(TypedDict, closed=True):
    dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response. The default is 20. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetGenerationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetGenerationsRequest:
    out: ListDatasetGenerationsRequest = {}  # type: ignore[typeddict-item]
    return out
