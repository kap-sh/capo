"""Generated from Smithy shape ``com.amazonaws.comprehend#ListFlywheelIterationHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.flywheel_iteration_filter
    import capo_comprehend.types.max_results_integer
    import capo_comprehend.types.string


class ListFlywheelIterationHistoryRequest(TypedDict, closed=True):
    flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    """<p>The ARN of the flywheel.</p>"""
    filter: NotRequired[
        "capo_comprehend.types.flywheel_iteration_filter.FlywheelIterationFilter"
    ]
    """<p>Filter the flywheel iteration history based on creation time.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Next token</p>"""
    max_results: NotRequired[
        "capo_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>Maximum number of iteration history results to return</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlywheelIterationHistoryRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    if "filter" in value:
        import capo_comprehend.types.flywheel_iteration_filter

        out["Filter"] = (
            capo_comprehend.types.flywheel_iteration_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlywheelIterationHistoryRequest:
    out: ListFlywheelIterationHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("FlywheelArn") is not None:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        out["flywheel_arn"] = ""
    if data.get("Filter") is not None:
        import capo_comprehend.types.flywheel_iteration_filter

        out["filter"] = (
            capo_comprehend.types.flywheel_iteration_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
