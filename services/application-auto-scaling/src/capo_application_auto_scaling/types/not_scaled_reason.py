"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#NotScaledReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.resource_capacity
    import capo_application_auto_scaling.types.xml_string


class NotScaledReason(TypedDict, closed=True):
    code: "capo_application_auto_scaling.types.xml_string.XmlString"
    """<p>A code that represents the reason for not scaling.</p> <p>Valid values:</p> <ul> <li> <p>AutoScalingAnticipatedFlapping</p> </li> <li> <p>TargetServicePutResourceAsUnscalable</p> </li> <li> <p>AlreadyAtMaxCapacity</p> </li> <li> <p>AlreadyAtMinCapacity</p> </li> <li> <p>AlreadyAtDesiredCapacity</p> </li> </ul>"""
    max_capacity: NotRequired[
        "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The maximum capacity.</p>"""
    min_capacity: NotRequired[
        "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The minimum capacity.</p>"""
    current_capacity: NotRequired[
        "capo_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The current capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotScaledReason) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "min_capacity" in value:
        out["MinCapacity"] = value["min_capacity"]
    if "current_capacity" in value:
        out["CurrentCapacity"] = value["current_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotScaledReason:
    out: NotScaledReason = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("MaxCapacity") is not None:
        out["max_capacity"] = data["MaxCapacity"]
    if data.get("MinCapacity") is not None:
        out["min_capacity"] = data["MinCapacity"]
    if data.get("CurrentCapacity") is not None:
        out["current_capacity"] = data["CurrentCapacity"]
    return out
