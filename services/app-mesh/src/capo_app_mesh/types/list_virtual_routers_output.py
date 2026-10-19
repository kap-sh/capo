"""Generated from Smithy shape ``com.amazonaws.appmesh#ListVirtualRoutersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_list


class ListVirtualRoutersOutput(TypedDict, closed=True):
    virtual_routers: "capo_app_mesh.types.virtual_router_list.VirtualRouterList"
    """<p>The list of existing virtual routers for the specified service mesh.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListVirtualRouters</code> request. When the results of a <code>ListVirtualRouters</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualRoutersOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_router_list

    out["virtualRouters"] = capo_app_mesh.types.virtual_router_list.serialize_json(
        value["virtual_routers"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVirtualRoutersOutput:
    out: ListVirtualRoutersOutput = {}  # type: ignore[typeddict-item]
    if data.get("virtualRouters") is not None:
        import capo_app_mesh.types.virtual_router_list

        out["virtual_routers"] = (
            capo_app_mesh.types.virtual_router_list.deserialize_json(
                data["virtualRouters"]
            )
        )
    else:
        out["virtual_routers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
