"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashBandwidthReportingMode``."""

from typing import Literal, TypeAlias, cast

DashBandwidthReportingMode: TypeAlias = Literal[
    "AVERAGE",
    "MAX",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashBandwidthReportingMode) -> str:
    return value


def deserialize_json(data: str) -> DashBandwidthReportingMode:
    return cast(DashBandwidthReportingMode, data)
