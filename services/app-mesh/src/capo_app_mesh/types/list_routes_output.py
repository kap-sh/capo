"""Generated from Smithy shape ``com.amazonaws.appmesh#ListRoutesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.route_list


class ListRoutesOutput(TypedDict, closed=True):
    routes: "capo_app_mesh.types.route_list.RouteList"
    """<p>The list of existing routes for the specified service mesh and virtual router.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListRoutes</code> request. When the results of a <code>ListRoutes</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutesOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.route_list

    out["routes"] = capo_app_mesh.types.route_list.serialize_json(value["routes"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoutesOutput:
    out: ListRoutesOutput = {}  # type: ignore[typeddict-item]
    if data.get("routes") is not None:
        import capo_app_mesh.types.route_list

        out["routes"] = capo_app_mesh.types.route_list.deserialize_json(data["routes"])
    else:
        out["routes"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
