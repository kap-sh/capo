"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSolutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeSolutionRequest(TypedDict, closed=True):
    solution_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSolutionRequest) -> dict:
    out: dict = {}
    out["solutionArn"] = value["solution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSolutionRequest:
    out: DescribeSolutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    else:
        out["solution_arn"] = ""
    return out
