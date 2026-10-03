"""Generated from Smithy shape ``com.amazonaws.sagemaker#TabularResolvedAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.problem_type


class TabularResolvedAttributes(TypedDict, closed=True):
    problem_type: NotRequired["capo_sagemaker.types.problem_type.ProblemType"]
    """<p>The type of supervised learning problem available for the model candidates of the AutoML job V2 (Binary Classification, Multiclass Classification, Regression). For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types"> SageMaker Autopilot problem types</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TabularResolvedAttributes) -> dict:
    out: dict = {}
    if "problem_type" in value:
        import capo_sagemaker.types.problem_type

        out["ProblemType"] = capo_sagemaker.types.problem_type.serialize_aws_json_1_1(
            value["problem_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TabularResolvedAttributes:
    out: TabularResolvedAttributes = {}  # type: ignore[typeddict-item]
    if data.get("ProblemType") is not None:
        import capo_sagemaker.types.problem_type

        out["problem_type"] = (
            capo_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    return out
