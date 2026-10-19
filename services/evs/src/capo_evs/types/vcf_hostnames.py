"""Generated from Smithy shape ``com.amazonaws.evs#VcfHostnames``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.host_name


class VcfHostnames(TypedDict, closed=True):
    v_center: "capo_evs.types.host_name.HostName"
    """<p>The VMware vCenter hostname.</p>"""
    nsx: "capo_evs.types.host_name.HostName"
    """<p>The VMware NSX Virtual IP (VIP) hostname.</p>"""
    nsx_manager1: "capo_evs.types.host_name.HostName"
    """<p>The hostname for the first VMware NSX Manager virtual machine (VM).</p>"""
    nsx_manager2: "capo_evs.types.host_name.HostName"
    """<p>The hostname for the second VMware NSX Manager virtual machine (VM).</p>"""
    nsx_manager3: "capo_evs.types.host_name.HostName"
    """<p>The hostname for the third VMware NSX Manager virtual machine (VM).</p>"""
    nsx_edge1: "capo_evs.types.host_name.HostName"
    """<p>The hostname for the first NSX Edge node.</p>"""
    nsx_edge2: "capo_evs.types.host_name.HostName"
    """<p>The hostname for the second NSX Edge node.</p>"""
    sddc_manager: "capo_evs.types.host_name.HostName"
    """<p>The hostname for SDDC Manager.</p>"""
    cloud_builder: "capo_evs.types.host_name.HostName"
    """<p>The hostname for VMware Cloud Builder.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VcfHostnames) -> dict:
    out: dict = {}
    out["vCenter"] = value["v_center"]
    out["nsx"] = value["nsx"]
    out["nsxManager1"] = value["nsx_manager1"]
    out["nsxManager2"] = value["nsx_manager2"]
    out["nsxManager3"] = value["nsx_manager3"]
    out["nsxEdge1"] = value["nsx_edge1"]
    out["nsxEdge2"] = value["nsx_edge2"]
    out["sddcManager"] = value["sddc_manager"]
    out["cloudBuilder"] = value["cloud_builder"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VcfHostnames:
    out: VcfHostnames = {}  # type: ignore[typeddict-item]
    if data.get("vCenter") is not None:
        out["v_center"] = data["vCenter"]
    else:
        out["v_center"] = ""
    if data.get("nsx") is not None:
        out["nsx"] = data["nsx"]
    else:
        out["nsx"] = ""
    if data.get("nsxManager1") is not None:
        out["nsx_manager1"] = data["nsxManager1"]
    else:
        out["nsx_manager1"] = ""
    if data.get("nsxManager2") is not None:
        out["nsx_manager2"] = data["nsxManager2"]
    else:
        out["nsx_manager2"] = ""
    if data.get("nsxManager3") is not None:
        out["nsx_manager3"] = data["nsxManager3"]
    else:
        out["nsx_manager3"] = ""
    if data.get("nsxEdge1") is not None:
        out["nsx_edge1"] = data["nsxEdge1"]
    else:
        out["nsx_edge1"] = ""
    if data.get("nsxEdge2") is not None:
        out["nsx_edge2"] = data["nsxEdge2"]
    else:
        out["nsx_edge2"] = ""
    if data.get("sddcManager") is not None:
        out["sddc_manager"] = data["sddcManager"]
    else:
        out["sddc_manager"] = ""
    if data.get("cloudBuilder") is not None:
        out["cloud_builder"] = data["cloudBuilder"]
    else:
        out["cloud_builder"] = ""
    return out
