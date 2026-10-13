"""Generated from Smithy shape ``com.amazonaws.georoutes#TimeThresholdList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds

TimeThresholdList: TypeAlias = list[
    "capo_geo_routes.types.duration_seconds.DurationSeconds"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeThresholdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TimeThresholdList:
    return [item for item in data if item is not None]


def redact_sensitive(value: TimeThresholdList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
