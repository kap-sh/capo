"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteVcenterClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.vcenter_client_id


class DeleteVcenterClientRequest(TypedDict, closed=True):
    vcenter_client_id: "capo_mgn.types.vcenter_client_id.VcenterClientID"
    """<p>ID of resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVcenterClientRequest) -> dict:
    out: dict = {}
    out["vcenterClientID"] = value["vcenter_client_id"]
    return out


def deserialize_json(data: dict) -> DeleteVcenterClientRequest:
    out: DeleteVcenterClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("vcenterClientID") is not None:
        out["vcenter_client_id"] = data["vcenterClientID"]
    else:
        out["vcenter_client_id"] = ""
    return out
