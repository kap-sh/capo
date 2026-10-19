"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ListManagedResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.managed_resource_summaries


class ListManagedResourcesResponse(TypedDict, closed=True):
    items: (
        "capo_arc_zonal_shift.types.managed_resource_summaries.ManagedResourceSummaries"
    )
    """<p>The items in the response list.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedResourcesResponse) -> dict:
    out: dict = {}
    import capo_arc_zonal_shift.types.managed_resource_summaries

    out["items"] = capo_arc_zonal_shift.types.managed_resource_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedResourcesResponse:
    out: ListManagedResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_arc_zonal_shift.types.managed_resource_summaries

        out["items"] = (
            capo_arc_zonal_shift.types.managed_resource_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
