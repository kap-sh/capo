"""Generated from Smithy shape ``com.amazonaws.inspector2#OnDemandScanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.on_demand_scan

OnDemandScanList: TypeAlias = list["capo_inspector2.types.on_demand_scan.OnDemandScan"]


# --- restJson1 ser/de ---
def serialize_json(value: OnDemandScanList) -> list:
    import capo_inspector2.types.on_demand_scan

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.on_demand_scan.serialize_json(item))
    return out


def deserialize_json(data: list) -> OnDemandScanList:
    import capo_inspector2.types.on_demand_scan

    out: OnDemandScanList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_inspector2.types.on_demand_scan.deserialize_json(item))
    return out
