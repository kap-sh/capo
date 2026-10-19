"""Generated from Smithy shape ``com.amazonaws.appmesh#ListVirtualGatewaysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_list


class ListVirtualGatewaysOutput(TypedDict, closed=True):
    virtual_gateways: "capo_app_mesh.types.virtual_gateway_list.VirtualGatewayList"
    """<p>The list of existing virtual gateways for the specified service mesh.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListVirtualGateways</code> request. When the results of a <code>ListVirtualGateways</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualGatewaysOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_gateway_list

    out["virtualGateways"] = capo_app_mesh.types.virtual_gateway_list.serialize_json(
        value["virtual_gateways"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVirtualGatewaysOutput:
    out: ListVirtualGatewaysOutput = {}  # type: ignore[typeddict-item]
    if data.get("virtualGateways") is not None:
        import capo_app_mesh.types.virtual_gateway_list

        out["virtual_gateways"] = (
            capo_app_mesh.types.virtual_gateway_list.deserialize_json(
                data["virtualGateways"]
            )
        )
    else:
        out["virtual_gateways"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
