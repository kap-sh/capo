"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35NoRegionalBlackoutFlag``."""

from typing import Literal, TypeAlias, cast

"""Corresponds to the no_regional_blackout_flag parameter. A value of REGIONAL_BLACKOUT corresponds to 0 (false) in the SCTE-35 specification. If you include one of the "restriction" flags then you must include all four of them."""
Scte35NoRegionalBlackoutFlag: TypeAlias = Literal[
    "REGIONAL_BLACKOUT",
    "NO_REGIONAL_BLACKOUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte35NoRegionalBlackoutFlag) -> str:
    return value


def deserialize_json(data: str) -> Scte35NoRegionalBlackoutFlag:
    return cast(Scte35NoRegionalBlackoutFlag, data)
