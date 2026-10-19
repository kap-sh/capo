"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelResolveToResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summaries
    import capo_iotsitewise.types.next_token


class ListComputationModelResolveToResourcesResponse(TypedDict, closed=True):
    computation_model_resolve_to_resource_summaries: "capo_iotsitewise.types.computation_model_resolve_to_resource_summaries.ComputationModelResolveToResourceSummaries"
    """<p>A list of summaries describing the distinct resources that this computation model resolves to when actions were executed.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of paginated results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelResolveToResourcesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summaries

    out["computationModelResolveToResourceSummaries"] = (
        capo_iotsitewise.types.computation_model_resolve_to_resource_summaries.serialize_json(
            value["computation_model_resolve_to_resource_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComputationModelResolveToResourcesResponse:
    out: ListComputationModelResolveToResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("computationModelResolveToResourceSummaries") is not None:
        import capo_iotsitewise.types.computation_model_resolve_to_resource_summaries

        out["computation_model_resolve_to_resource_summaries"] = (
            capo_iotsitewise.types.computation_model_resolve_to_resource_summaries.deserialize_json(
                data["computationModelResolveToResourceSummaries"]
            )
        )
    else:
        out["computation_model_resolve_to_resource_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
