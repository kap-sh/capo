"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListResolvedTestRunTargetResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.resolved_target_resource_list


class ListResolvedTestRunTargetResourcesResponse(TypedDict, closed=True):
    resolved_target_resources: "capo_resiliencehubv2.types.resolved_target_resource_list.ResolvedTargetResourceList"
    """<p>The list of resolved target resources.</p>"""
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListResolvedTestRunTargetResourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.resolved_target_resource_list

    out["resolvedTargetResources"] = (
        capo_resiliencehubv2.types.resolved_target_resource_list.serialize_json(
            value["resolved_target_resources"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResolvedTestRunTargetResourcesResponse:
    out: ListResolvedTestRunTargetResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("resolvedTargetResources") is not None:
        import capo_resiliencehubv2.types.resolved_target_resource_list

        out["resolved_target_resources"] = (
            capo_resiliencehubv2.types.resolved_target_resource_list.deserialize_json(
                data["resolvedTargetResources"]
            )
        )
    else:
        out["resolved_target_resources"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
