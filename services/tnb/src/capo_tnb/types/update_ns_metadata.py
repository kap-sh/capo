"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateNsMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id


class UpdateNsMetadata(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>The network service descriptor used for updating the network instance.</p>"""
    additional_params_for_ns: NotRequired["object"]
    """<p>The configurable properties used during update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNsMetadata) -> dict:
    out: dict = {}
    out["nsdInfoId"] = value["nsd_info_id"]
    if "additional_params_for_ns" in value:
        out["additionalParamsForNs"] = value["additional_params_for_ns"]
    return out


def deserialize_json(data: dict) -> UpdateNsMetadata:
    out: UpdateNsMetadata = {}  # type: ignore[typeddict-item]
    if data.get("nsdInfoId") is not None:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        out["nsd_info_id"] = ""
    if data.get("additionalParamsForNs") is not None:
        out["additional_params_for_ns"] = data["additionalParamsForNs"]
    return out
