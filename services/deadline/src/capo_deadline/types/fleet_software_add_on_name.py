"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSoftwareAddOnName``."""

from typing import Literal, TypeAlias, cast

FleetSoftwareAddOnName: TypeAlias = Literal["docker",]


# --- restJson1 ser/de ---
def serialize_json(value: FleetSoftwareAddOnName) -> str:
    return value


def deserialize_json(data: str) -> FleetSoftwareAddOnName:
    return cast(FleetSoftwareAddOnName, data)
