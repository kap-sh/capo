"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.snap_start_apply_on
    import capo_lambda.types.snap_start_optimization_status


class SnapStartResponse(TypedDict, closed=True):
    apply_on: NotRequired["capo_lambda.types.snap_start_apply_on.SnapStartApplyOn"]
    """<p>When set to <code>PublishedVersions</code>, Lambda creates a snapshot of the execution environment when you publish a function version.</p>"""
    optimization_status: NotRequired[
        "capo_lambda.types.snap_start_optimization_status.SnapStartOptimizationStatus"
    ]
    """<p>When you provide a <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using">qualified Amazon Resource Name (ARN)</a>, this response element indicates whether SnapStart is activated for the specified function version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapStartResponse) -> dict:
    out: dict = {}
    if "apply_on" in value:
        import capo_lambda.types.snap_start_apply_on

        out["ApplyOn"] = capo_lambda.types.snap_start_apply_on.serialize_json(
            value["apply_on"]
        )
    if "optimization_status" in value:
        import capo_lambda.types.snap_start_optimization_status

        out["OptimizationStatus"] = (
            capo_lambda.types.snap_start_optimization_status.serialize_json(
                value["optimization_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapStartResponse:
    out: SnapStartResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplyOn") is not None:
        import capo_lambda.types.snap_start_apply_on

        out["apply_on"] = capo_lambda.types.snap_start_apply_on.deserialize_json(
            data["ApplyOn"]
        )
    if data.get("OptimizationStatus") is not None:
        import capo_lambda.types.snap_start_optimization_status

        out["optimization_status"] = (
            capo_lambda.types.snap_start_optimization_status.deserialize_json(
                data["OptimizationStatus"]
            )
        )
    return out
