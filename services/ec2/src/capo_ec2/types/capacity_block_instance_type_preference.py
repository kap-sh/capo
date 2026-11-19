"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockInstanceTypePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CapacityBlockInstanceTypePreference(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type to consider in the Capacity Block search.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockInstanceTypePreference,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))


def deserialize_ec2_query(el: Element) -> CapacityBlockInstanceTypePreference:
    out: CapacityBlockInstanceTypePreference = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    return out
