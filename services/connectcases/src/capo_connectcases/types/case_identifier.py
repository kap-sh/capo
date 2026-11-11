"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.reference_id
    import capo_connectcases.types.reference_number


class CaseIdentifier(TypedDict, closed=True):
    case_id: NotRequired["capo_connectcases.types.case_id.CaseId"]
    """<p>The unique identifier of the case.</p>"""
    reference_number: NotRequired[
        "capo_connectcases.types.reference_number.ReferenceNumber"
    ]
    """<p>The reference number of the case. Reference numbers aren't guaranteed to be unique. <code>BatchUpdateCase</code> and <code>BatchCreateRelatedItem</code> don't return this value.</p>"""
    reference_id: NotRequired["capo_connectcases.types.reference_id.ReferenceId"]
    """<p>The reference ID of the case. Cases created before reference IDs were available don't have one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseIdentifier) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "reference_number" in value:
        out["referenceNumber"] = value["reference_number"]
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> CaseIdentifier:
    out: CaseIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("referenceNumber") is not None:
        out["reference_number"] = data["referenceNumber"]
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    return out
