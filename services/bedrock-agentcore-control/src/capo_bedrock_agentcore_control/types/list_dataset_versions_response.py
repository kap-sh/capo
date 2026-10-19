"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_version_summary_list


class ListDatasetVersionsResponse(TypedDict, closed=True):
    versions: "capo_bedrock_agentcore_control.types.dataset_version_summary_list.DatasetVersionSummaryList"
    """<p> The list of published dataset versions. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next page of results, or null if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetVersionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.dataset_version_summary_list

    out["versions"] = (
        capo_bedrock_agentcore_control.types.dataset_version_summary_list.serialize_json(
            value["versions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetVersionsResponse:
    out: ListDatasetVersionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("versions") is not None:
        import capo_bedrock_agentcore_control.types.dataset_version_summary_list

        out["versions"] = (
            capo_bedrock_agentcore_control.types.dataset_version_summary_list.deserialize_json(
                data["versions"]
            )
        )
    else:
        out["versions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
