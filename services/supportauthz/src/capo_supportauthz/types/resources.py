"""Generated from Smithy shape ``com.amazonaws.supportauthz#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.resource

Resources: TypeAlias = list["capo_supportauthz.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    return list(value)


def deserialize_json(data: list) -> Resources:
    return [item for item in data if item is not None]
