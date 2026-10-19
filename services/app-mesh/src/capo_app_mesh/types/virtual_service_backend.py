"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceBackend``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.client_policy
    import capo_app_mesh.types.service_name


class VirtualServiceBackend(TypedDict, closed=True):
    virtual_service_name: "capo_app_mesh.types.service_name.ServiceName"
    """<p>The name of the virtual service that is acting as a virtual node backend.</p>"""
    client_policy: NotRequired["capo_app_mesh.types.client_policy.ClientPolicy"]
    """<p>A reference to an object that represents the client policy for a backend.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceBackend) -> dict:
    out: dict = {}
    out["virtualServiceName"] = value["virtual_service_name"]
    if "client_policy" in value:
        import capo_app_mesh.types.client_policy

        out["clientPolicy"] = capo_app_mesh.types.client_policy.serialize_json(
            value["client_policy"]
        )
    return out


def deserialize_json(data: dict) -> VirtualServiceBackend:
    out: VirtualServiceBackend = {}  # type: ignore[typeddict-item]
    if data.get("virtualServiceName") is not None:
        out["virtual_service_name"] = data["virtualServiceName"]
    else:
        out["virtual_service_name"] = ""
    if data.get("clientPolicy") is not None:
        import capo_app_mesh.types.client_policy

        out["client_policy"] = capo_app_mesh.types.client_policy.deserialize_json(
            data["clientPolicy"]
        )
    return out
