"""Generated from Smithy shape ``com.amazonaws.keyspaces#WarmThroughputSpecification``."""

from typing_extensions import NotRequired, TypedDict


class WarmThroughputSpecification(TypedDict, closed=True):
    read_units_per_second: NotRequired["int"]
    """<p>The number of read capacity units per second to pre-warm the table for read capacity throughput. The minimum value is 1.</p>"""
    write_units_per_second: NotRequired["int"]
    """<p>The number of write capacity units per second to pre-warm the table for write capacity throughput. The minimum value is 1.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WarmThroughputSpecification) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["readUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["writeUnitsPerSecond"] = value["write_units_per_second"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WarmThroughputSpecification:
    out: WarmThroughputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("readUnitsPerSecond") is not None:
        out["read_units_per_second"] = data["readUnitsPerSecond"]
    if data.get("writeUnitsPerSecond") is not None:
        out["write_units_per_second"] = data["writeUnitsPerSecond"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WarmThroughputSpecification) -> dict:
    out: dict = {}
    if "read_units_per_second" in value:
        out["readUnitsPerSecond"] = value["read_units_per_second"]
    if "write_units_per_second" in value:
        out["writeUnitsPerSecond"] = value["write_units_per_second"]
    return out


def deserialize_cbor(data: dict) -> WarmThroughputSpecification:
    out: WarmThroughputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("readUnitsPerSecond") is not None:
        out["read_units_per_second"] = data["readUnitsPerSecond"]
    if data.get("writeUnitsPerSecond") is not None:
        out["write_units_per_second"] = data["writeUnitsPerSecond"]
    return out
