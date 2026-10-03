"""Generated from Smithy shape ``com.amazonaws.personalize#GetSolutionMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.metrics


class GetSolutionMetricsResponse(TypedDict, closed=True):
    solution_version_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The same solution version ARN as specified in the request.</p>"""
    metrics: NotRequired["capo_personalize.types.metrics.Metrics"]
    """<p>The metrics for the solution version. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html"> Evaluating a solution version with metrics </a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSolutionMetricsResponse) -> dict:
    out: dict = {}
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "metrics" in value:
        import capo_personalize.types.metrics

        out["metrics"] = capo_personalize.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSolutionMetricsResponse:
    out: GetSolutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if data.get("metrics") is not None:
        import capo_personalize.types.metrics

        out["metrics"] = capo_personalize.types.metrics.deserialize_aws_json_1_1(
            data["metrics"]
        )
    return out
