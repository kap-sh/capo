"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AutoScalingGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.capacity_wait_timeout_seconds
    import capo_imagebuilder.types.non_empty_string


class AutoScalingGroupConfiguration(TypedDict, closed=True):
    name: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the Auto Scaling group, in the same account and Amazon Web Services Region as the infrastructure configuration. To specify a group, you must have permissions to describe it.</p>"""
    capacity_wait_timeout_seconds: NotRequired[
        "capo_imagebuilder.types.capacity_wait_timeout_seconds.CapacityWaitTimeoutSeconds"
    ]
    """<p>The number of seconds that Image Builder waits for an instance to become available in the group before the build fails. If you set this value to 0 or omit it, the build fails as soon as the group has no instance available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "capacity_wait_timeout_seconds" in value:
        out["capacityWaitTimeoutSeconds"] = value["capacity_wait_timeout_seconds"]
    return out


def deserialize_json(data: dict) -> AutoScalingGroupConfiguration:
    out: AutoScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("capacityWaitTimeoutSeconds") is not None:
        out["capacity_wait_timeout_seconds"] = data["capacityWaitTimeoutSeconds"]
    return out
