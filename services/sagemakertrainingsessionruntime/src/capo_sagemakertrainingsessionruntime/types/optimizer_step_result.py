"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#OptimizerStepResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.metrics_map


class OptimizerStepResult(TypedDict, closed=True):
    metrics: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.metrics_map.MetricsMap"
    ]
    """<p>The training metrics emitted by the engine after the optimizer step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizerStepResult) -> dict:
    out: dict = {}
    if "metrics" in value:
        import capo_sagemakertrainingsessionruntime.types.metrics_map

        out["metrics"] = (
            capo_sagemakertrainingsessionruntime.types.metrics_map.serialize_json(
                value["metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> OptimizerStepResult:
    out: OptimizerStepResult = {}  # type: ignore[typeddict-item]
    if data.get("metrics") is not None:
        import capo_sagemakertrainingsessionruntime.types.metrics_map

        out["metrics"] = (
            capo_sagemakertrainingsessionruntime.types.metrics_map.deserialize_json(
                data["metrics"]
            )
        )
    return out
