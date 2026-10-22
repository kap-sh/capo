"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashAdaptationSetGrouping``."""

from typing import Literal, TypeAlias, cast

"""Specify additional criteria for partitioning video outputs into separate AdaptationSets. These criteria are applied on top of the grouping produced by DashManifestStyle."""
DashAdaptationSetGrouping: TypeAlias = Literal["CODEC",]


# --- restJson1 ser/de ---
def serialize_json(value: DashAdaptationSetGrouping) -> str:
    return value


def deserialize_json(data: str) -> DashAdaptationSetGrouping:
    return cast(DashAdaptationSetGrouping, data)
