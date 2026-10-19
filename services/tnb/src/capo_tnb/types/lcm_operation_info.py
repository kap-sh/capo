"""Generated from Smithy shape ``com.amazonaws.tnb#LcmOperationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_lcm_op_occ_id


class LcmOperationInfo(TypedDict, closed=True):
    ns_lcm_op_occ_id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>The identifier of the network operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LcmOperationInfo) -> dict:
    out: dict = {}
    out["nsLcmOpOccId"] = value["ns_lcm_op_occ_id"]
    return out


def deserialize_json(data: dict) -> LcmOperationInfo:
    out: LcmOperationInfo = {}  # type: ignore[typeddict-item]
    if data.get("nsLcmOpOccId") is not None:
        out["ns_lcm_op_occ_id"] = data["nsLcmOpOccId"]
    else:
        out["ns_lcm_op_occ_id"] = ""
    return out
