"""Generated from Smithy shape ``com.amazonaws.guardduty#Resources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.resource_v2

Resources: TypeAlias = list["capo_guardduty.types.resource_v2.ResourceV2"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import capo_guardduty.types.resource_v2

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.resource_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resources:
    import capo_guardduty.types.resource_v2

    out: Resources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.resource_v2.deserialize_json(item))
    return out


def redact_sensitive(value: Resources) -> list[Any]:
    import capo_guardduty.types.resource_v2

    return [capo_guardduty.types.resource_v2.redact_sensitive(item) for item in value]
