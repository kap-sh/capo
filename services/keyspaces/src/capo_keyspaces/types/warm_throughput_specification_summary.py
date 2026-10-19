"""Generated from Smithy shape ``com.amazonaws.keyspaces#WarmThroughputSpecificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.warm_throughput_status


class WarmThroughputSpecificationSummary(TypedDict, closed=True):
    read_units_per_second: "int"
    """<p>The number of read capacity units per second currently configured for warm throughput.</p>"""
    write_units_per_second: "int"
    """<p>The number of write capacity units per second currently configured for warm throughput.</p>"""
    status: "capo_keyspaces.types.warm_throughput_status.WarmThroughputStatus"
    """<p>The current status of the warm throughput configuration. Valid values are <code>AVAILABLE</code> when the configuration is active, and <code>UPDATING</code> when changes are being applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WarmThroughputSpecificationSummary) -> dict:
    out: dict = {}
    out["readUnitsPerSecond"] = value["read_units_per_second"]
    out["writeUnitsPerSecond"] = value["write_units_per_second"]
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WarmThroughputSpecificationSummary:
    out: WarmThroughputSpecificationSummary = {}  # type: ignore[typeddict-item]
    if data.get("readUnitsPerSecond") is not None:
        out["read_units_per_second"] = data["readUnitsPerSecond"]
    else:
        out["read_units_per_second"] = 0
    if data.get("writeUnitsPerSecond") is not None:
        out["write_units_per_second"] = data["writeUnitsPerSecond"]
    else:
        out["write_units_per_second"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
