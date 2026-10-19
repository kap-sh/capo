"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkServiceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id


class UpdateSolNetworkServiceData(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor.</p>"""
    additional_params_for_ns: NotRequired["object"]
    """<p>Values for the configurable properties declared in the network service descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkServiceData) -> dict:
    out: dict = {}
    out["nsdInfoId"] = value["nsd_info_id"]
    if "additional_params_for_ns" in value:
        out["additionalParamsForNs"] = value["additional_params_for_ns"]
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkServiceData:
    out: UpdateSolNetworkServiceData = {}  # type: ignore[typeddict-item]
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        out["nsd_info_id"] = ""
    if data.get("additionalParamsForNs") is not None:
        out["additional_params_for_ns"] = data["additionalParamsForNs"]
    return out
