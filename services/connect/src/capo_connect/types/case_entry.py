"""Generated from Smithy shape ``com.amazonaws.connect#CaseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.case_id
    import capo_connect.types.case_reference_number


class CaseEntry(TypedDict, closed=True):
    case_id: NotRequired["capo_connect.types.case_id.CaseId"]
    """<p>Unique identifier of the case in UUID format.</p>"""
    case_reference_number: NotRequired[
        "capo_connect.types.case_reference_number.CaseReferenceNumber"
    ]
    """<p>A friendly number for the case. Reference numbers are not guaranteed to be unique.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseEntry) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["CaseId"] = value["case_id"]
    if "case_reference_number" in value:
        out["CaseReferenceNumber"] = value["case_reference_number"]
    return out


def deserialize_json(data: dict) -> CaseEntry:
    out: CaseEntry = {}  # type: ignore[typeddict-item]
    if data.get("CaseId") is not None:
        out["case_id"] = data["CaseId"]
    if data.get("CaseReferenceNumber") is not None:
        out["case_reference_number"] = data["CaseReferenceNumber"]
    return out
