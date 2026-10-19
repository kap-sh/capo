"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id


class CreateCaseResponse(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>A response element providing responses for requests to CreateCase. This element responds with the case ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    return out


def deserialize_json(data: dict) -> CreateCaseResponse:
    out: CreateCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    return out
