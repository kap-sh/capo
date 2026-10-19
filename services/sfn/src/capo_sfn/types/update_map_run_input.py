"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateMapRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn
    import capo_sfn.types.max_concurrency
    import capo_sfn.types.tolerated_failure_count
    import capo_sfn.types.tolerated_failure_percentage


class UpdateMapRunInput(TypedDict, closed=True):
    map_run_arn: "capo_sfn.types.long_arn.LongArn"
    """<p>The Amazon Resource Name (ARN) of a Map Run.</p>"""
    max_concurrency: NotRequired["capo_sfn.types.max_concurrency.MaxConcurrency"]
    """<p>The maximum number of child workflow executions that can be specified to run in parallel for the Map Run at the same time.</p>"""
    tolerated_failure_percentage: NotRequired[
        "capo_sfn.types.tolerated_failure_percentage.ToleratedFailurePercentage"
    ]
    """<p>The maximum percentage of failed items before the Map Run fails.</p>"""
    tolerated_failure_count: NotRequired[
        "capo_sfn.types.tolerated_failure_count.ToleratedFailureCount"
    ]
    """<p>The maximum number of failed items before the Map Run fails.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateMapRunInput) -> dict:
    out: dict = {}
    out["mapRunArn"] = value["map_run_arn"]
    if "max_concurrency" in value:
        out["maxConcurrency"] = value["max_concurrency"]
    if "tolerated_failure_percentage" in value:
        out["toleratedFailurePercentage"] = (
            "NaN"
            if value["tolerated_failure_percentage"]
            != value["tolerated_failure_percentage"]
            else "Infinity"
            if value["tolerated_failure_percentage"] == float("inf")
            else "-Infinity"
            if value["tolerated_failure_percentage"] == float("-inf")
            else value["tolerated_failure_percentage"]
        )
    if "tolerated_failure_count" in value:
        out["toleratedFailureCount"] = value["tolerated_failure_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateMapRunInput:
    out: UpdateMapRunInput = {}  # type: ignore[typeddict-item]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    else:
        out["map_run_arn"] = ""
    if data.get("maxConcurrency") is not None:
        out["max_concurrency"] = data["maxConcurrency"]
    if data.get("toleratedFailurePercentage") is not None:
        out["tolerated_failure_percentage"] = float(data["toleratedFailurePercentage"])
    if data.get("toleratedFailureCount") is not None:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    return out
