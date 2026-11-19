"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListDatasetGenerationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.dataset_generation_summary_list


class ListDatasetGenerationsResponse(TypedDict, closed=True):
    dataset_generations: "capo_bedrock_agentcore.types.dataset_generation_summary_list.DatasetGenerationSummaryList"
    """<p>The dataset generations.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetGenerationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.dataset_generation_summary_list

    out["datasetGenerations"] = (
        capo_bedrock_agentcore.types.dataset_generation_summary_list.serialize_json(
            value["dataset_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetGenerationsResponse:
    out: ListDatasetGenerationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetGenerations") is not None:
        import capo_bedrock_agentcore.types.dataset_generation_summary_list

        out["dataset_generations"] = (
            capo_bedrock_agentcore.types.dataset_generation_summary_list.deserialize_json(
                data["datasetGenerations"]
            )
        )
    else:
        out["dataset_generations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
