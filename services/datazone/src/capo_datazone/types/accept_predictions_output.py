"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptPredictionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.domain_id
    import capo_datazone.types.revision


class AcceptPredictionsOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    asset_id: "capo_datazone.types.asset_id.AssetId"
    """<p>The ID of the asset.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The revision that is to be made to the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptPredictionsOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["assetId"] = value["asset_id"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> AcceptPredictionsOutput:
    out: AcceptPredictionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = ""
    return out
