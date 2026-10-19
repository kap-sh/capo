"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterChunks``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.default_task_count
    import capo_deadline.types.range_constraint
    import capo_deadline.types.target_runtime_seconds


class StepParameterChunks(TypedDict, closed=True):
    default_task_count: "capo_deadline.types.default_task_count.DefaultTaskCount"
    """<p>The number of tasks to combine into a single chunk by default.</p>"""
    target_runtime_seconds: NotRequired[
        "capo_deadline.types.target_runtime_seconds.TargetRuntimeSeconds"
    ]
    """<p>The number of seconds to aim for when forming chunks.</p>"""
    range_constraint: "capo_deadline.types.range_constraint.RangeConstraint"
    """<p>Specifies whether the chunked ranges must be contiguous or can have gaps between them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepParameterChunks) -> dict:
    out: dict = {}
    out["defaultTaskCount"] = value["default_task_count"]
    if "target_runtime_seconds" in value:
        out["targetRuntimeSeconds"] = value["target_runtime_seconds"]
    import capo_deadline.types.range_constraint

    out["rangeConstraint"] = capo_deadline.types.range_constraint.serialize_json(
        value["range_constraint"]
    )
    return out


def deserialize_json(data: dict) -> StepParameterChunks:
    out: StepParameterChunks = {}  # type: ignore[typeddict-item]
    if data.get("defaultTaskCount") is not None:
        out["default_task_count"] = data["defaultTaskCount"]
    else:
        out["default_task_count"] = 0
    if data.get("targetRuntimeSeconds") is not None:
        out["target_runtime_seconds"] = data["targetRuntimeSeconds"]
    if data.get("rangeConstraint") is not None:
        import capo_deadline.types.range_constraint

        out["range_constraint"] = capo_deadline.types.range_constraint.deserialize_json(
            data["rangeConstraint"]
        )
    else:
        import typing

        out["range_constraint"] = typing.cast(
            "capo_deadline.types.range_constraint.RangeConstraint", ""
        )
    return out
