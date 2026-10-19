"""Generated from Smithy shape ``com.amazonaws.qconnect#CaseSummarizationInputData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.case_arn


class CaseSummarizationInputData(TypedDict, closed=True):
    case_arn: "capo_qconnect.types.case_arn.CaseArn"
    """<p>The Amazon Resource Name (ARN) of the case for summarization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummarizationInputData) -> dict:
    out: dict = {}
    out["caseArn"] = value["case_arn"]
    return out


def deserialize_json(data: dict) -> CaseSummarizationInputData:
    out: CaseSummarizationInputData = {}  # type: ignore[typeddict-item]
    if data.get("caseArn") is not None:
        out["case_arn"] = data["caseArn"]
    else:
        out["case_arn"] = ""
    return out
