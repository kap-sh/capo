"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfDashAdaptationSetGrouping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.dash_adaptation_set_grouping

__listOfDashAdaptationSetGrouping: TypeAlias = list[
    "capo_mediaconvert.types.dash_adaptation_set_grouping.DashAdaptationSetGrouping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashAdaptationSetGrouping) -> list:
    import capo_mediaconvert.types.dash_adaptation_set_grouping

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.dash_adaptation_set_grouping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDashAdaptationSetGrouping:
    import capo_mediaconvert.types.dash_adaptation_set_grouping

    out: __listOfDashAdaptationSetGrouping = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconvert.types.dash_adaptation_set_grouping.deserialize_json(item)
        )
    return out
