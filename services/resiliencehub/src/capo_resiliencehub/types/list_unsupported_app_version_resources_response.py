"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListUnsupportedAppVersionResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.string255
    import capo_resiliencehub.types.unsupported_resource_list


class ListUnsupportedAppVersionResourcesResponse(TypedDict, closed=True):
    unsupported_resources: (
        "capo_resiliencehub.types.unsupported_resource_list.UnsupportedResourceList"
    )
    """<p>The unsupported resources for the application.</p>"""
    resolution_id: "capo_resiliencehub.types.string255.String255"
    """<p>The identifier for a specific resolution.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUnsupportedAppVersionResourcesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.unsupported_resource_list

    out["unsupportedResources"] = (
        capo_resiliencehub.types.unsupported_resource_list.serialize_json(
            value["unsupported_resources"]
        )
    )
    out["resolutionId"] = value["resolution_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUnsupportedAppVersionResourcesResponse:
    out: ListUnsupportedAppVersionResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("unsupportedResources") is not None:
        import capo_resiliencehub.types.unsupported_resource_list

        out["unsupported_resources"] = (
            capo_resiliencehub.types.unsupported_resource_list.deserialize_json(
                data["unsupportedResources"]
            )
        )
    else:
        out["unsupported_resources"] = []
    if data.get("resolutionId") is not None:
        out["resolution_id"] = data["resolutionId"]
    else:
        out["resolution_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
