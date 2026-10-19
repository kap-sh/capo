"""Generated from Smithy shape ``com.amazonaws.ecs#MemoryMiBRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer


class MemoryMiBRequest(TypedDict, closed=True):
    min: "capo_ecs.types.boxed_integer.BoxedInteger"
    """<p>The minimum amount of memory in MiB. Instance types with less memory than this value are excluded from selection.</p>"""
    max: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum amount of memory in MiB. Instance types with more memory than this value are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemoryMiBRequest) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemoryMiBRequest:
    out: MemoryMiBRequest = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    else:
        out["min"] = 0
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
