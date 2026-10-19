"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_arn
    import capo_connectcases.types.case_id


class CreateCaseResponse(TypedDict, closed=True):
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    case_arn: "capo_connectcases.types.case_arn.CaseArn"
    """<p>The Amazon Resource Name (ARN) of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    out["caseArn"] = value["case_arn"]
    return out


def deserialize_json(data: dict) -> CreateCaseResponse:
    out: CreateCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    if data.get("caseArn") is not None:
        out["case_arn"] = data["caseArn"]
    else:
        out["case_arn"] = ""
    return out
