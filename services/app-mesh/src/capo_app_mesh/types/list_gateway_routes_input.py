"""Generated from Smithy shape ``com.amazonaws.appmesh#ListGatewayRoutesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.list_gateway_routes_limit
    import capo_app_mesh.types.resource_name


class ListGatewayRoutesInput(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh to list gateway routes in.</p>"""
    virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway to list gateway routes in.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListGatewayRoutes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>"""
    limit: NotRequired[
        "capo_app_mesh.types.list_gateway_routes_limit.ListGatewayRoutesLimit"
    ]
    """<p>The maximum number of results returned by <code>ListGatewayRoutes</code> in paginated output. When you use this parameter, <code>ListGatewayRoutes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListGatewayRoutes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListGatewayRoutes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    mesh_owner: NotRequired["capo_app_mesh.types.account_id.AccountId"]
    """<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRoutesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGatewayRoutesInput:
    out: ListGatewayRoutesInput = {}  # type: ignore[typeddict-item]
    return out
