"""Generated from Smithy shape ``com.amazonaws.guardduty#SharedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.shared_resource

SharedResources: TypeAlias = list["capo_guardduty.types.shared_resource.SharedResource"]


# --- restJson1 ser/de ---
def serialize_json(value: SharedResources) -> list:
    import capo_guardduty.types.shared_resource

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.shared_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> SharedResources:
    import capo_guardduty.types.shared_resource

    out: SharedResources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.shared_resource.deserialize_json(item))
    return out
