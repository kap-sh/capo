"""Generated from Smithy shape ``com.amazonaws.tnb#ModifyVnfInfoMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.vnf_instance_id


class ModifyVnfInfoMetadata(TypedDict, closed=True):
    vnf_instance_id: "capo_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>The network function instance that was updated in the network instance.</p>"""
    vnf_configurable_properties: "object"
    """<p>The configurable properties used during update of the network function instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyVnfInfoMetadata) -> dict:
    out: dict = {}
    out["vnfInstanceId"] = value["vnf_instance_id"]
    out["vnfConfigurableProperties"] = value["vnf_configurable_properties"]
    return out


def deserialize_json(data: dict) -> ModifyVnfInfoMetadata:
    out: ModifyVnfInfoMetadata = {}  # type: ignore[typeddict-item]
    if data.get("vnfInstanceId") is not None:
        out["vnf_instance_id"] = data["vnfInstanceId"]
    else:
        out["vnf_instance_id"] = ""
    if data.get("vnfConfigurableProperties") is not None:
        out["vnf_configurable_properties"] = data["vnfConfigurableProperties"]
    else:
        out["vnf_configurable_properties"] = None
    return out
