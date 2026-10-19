"""Generated from Smithy shape ``com.amazonaws.ecs#ThresholdConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.threshold_type


class ThresholdConfiguration(TypedDict, closed=True):
    type: "capo_ecs.types.threshold_type.ThresholdType"
    """<p>Determines how Amazon ECS uses <code>value</code> to calculate the failure threshold. For the percentage types (<code>BOUNDED_PERCENT</code> and <code>UNBOUNDED_PERCENT</code>), Amazon ECS multiplies <code>value</code> by the latest service desired count. For <code>COUNT</code>, Amazon ECS uses <code>value</code> directly as the threshold. The default is <code>BOUNDED_PERCENT</code>.</p>"""
    value: "capo_ecs.types.integer.Integer"
    """<p>Specifies the integer that Amazon ECS uses to calculate the failure threshold. When <code>type</code> is <code>COUNT</code>, this value is the failure threshold itself. When <code>type</code> is a percentage type, Amazon ECS multiplies this value by the latest service desired count to produce the failure threshold. The default is <code>50</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThresholdConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.threshold_type

    out["type"] = capo_ecs.types.threshold_type.serialize_aws_json_1_1(value["type"])
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ThresholdConfiguration:
    out: ThresholdConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.threshold_type

        out["type"] = capo_ecs.types.threshold_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_ecs.types.threshold_type.ThresholdType", "")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
