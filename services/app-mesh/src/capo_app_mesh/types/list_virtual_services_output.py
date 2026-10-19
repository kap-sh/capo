"""Generated from Smithy shape ``com.amazonaws.appmesh#ListVirtualServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_service_list


class ListVirtualServicesOutput(TypedDict, closed=True):
    virtual_services: "capo_app_mesh.types.virtual_service_list.VirtualServiceList"
    """<p>The list of existing virtual services for the specified service mesh.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListVirtualServices</code> request. When the results of a <code>ListVirtualServices</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVirtualServicesOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_service_list

    out["virtualServices"] = capo_app_mesh.types.virtual_service_list.serialize_json(
        value["virtual_services"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVirtualServicesOutput:
    out: ListVirtualServicesOutput = {}  # type: ignore[typeddict-item]
    if data.get("virtualServices") is not None:
        import capo_app_mesh.types.virtual_service_list

        out["virtual_services"] = (
            capo_app_mesh.types.virtual_service_list.deserialize_json(
                data["virtualServices"]
            )
        )
    else:
        out["virtual_services"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
