"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkModify``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.vnf_instance_id


class UpdateSolNetworkModify(TypedDict, closed=True):
    vnf_instance_id: "capo_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>ID of the network function instance.</p> <p>A network function instance is a function in a function package .</p>"""
    vnf_configurable_properties: "object"
    """<p>Provides values for the configurable properties declared in the function package descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkModify) -> dict:
    out: dict = {}
    out["vnfInstanceId"] = value["vnf_instance_id"]
    out["vnfConfigurableProperties"] = value["vnf_configurable_properties"]
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkModify:
    out: UpdateSolNetworkModify = {}  # type: ignore[typeddict-item]
    if data.get("vnfInstanceId") is not None:
        out["vnf_instance_id"] = data["vnfInstanceId"]
    else:
        out["vnf_instance_id"] = ""
    if data.get("vnfConfigurableProperties") is not None:
        out["vnf_configurable_properties"] = data["vnfConfigurableProperties"]
    else:
        out["vnf_configurable_properties"] = None
    return out
