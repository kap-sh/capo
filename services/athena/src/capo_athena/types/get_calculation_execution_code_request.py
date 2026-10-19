"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionCodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_execution_id


class GetCalculationExecutionCodeRequest(TypedDict, closed=True):
    calculation_execution_id: (
        "capo_athena.types.calculation_execution_id.CalculationExecutionId"
    )
    """<p>The calculation execution UUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionCodeRequest) -> dict:
    out: dict = {}
    out["CalculationExecutionId"] = value["calculation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionCodeRequest:
    out: GetCalculationExecutionCodeRequest = {}  # type: ignore[typeddict-item]
    if data.get("CalculationExecutionId") is not None:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    else:
        out["calculation_execution_id"] = ""
    return out
