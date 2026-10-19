"""Generated from Smithy shape ``com.amazonaws.personalize#StopSolutionVersionCreationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class StopSolutionVersionCreationRequest(TypedDict, closed=True):
    solution_version_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution version you want to stop creating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSolutionVersionCreationRequest) -> dict:
    out: dict = {}
    out["solutionVersionArn"] = value["solution_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSolutionVersionCreationRequest:
    out: StopSolutionVersionCreationRequest = {}  # type: ignore[typeddict-item]
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        out["solution_version_arn"] = ""
    return out
