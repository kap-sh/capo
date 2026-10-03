"""Generated from Smithy shape ``com.amazonaws.kendra#CapacityUnitsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.query_capacity_unit
    import capo_kendra.types.storage_capacity_unit


class CapacityUnitsConfiguration(TypedDict, closed=True):
    storage_capacity_units: (
        "capo_kendra.types.storage_capacity_unit.StorageCapacityUnit"
    )
    """<p>The amount of extra storage capacity for an index. A single capacity unit provides 30 GB of storage space or 100,000 documents, whichever is reached first. You can add up to 100 extra capacity units.</p>"""
    query_capacity_units: "capo_kendra.types.query_capacity_unit.QueryCapacityUnit"
    """<p>The amount of extra query capacity for an index and <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html">GetQuerySuggestions</a> capacity.</p> <p>A single extra capacity unit for an index provides 0.1 queries per second or approximately 8,000 queries per day. You can add up to 100 extra capacity units.</p> <p> <code>GetQuerySuggestions</code> capacity is five times the provisioned query capacity for an index, or the base capacity of 2.5 calls per second, whichever is higher. For example, the base capacity for an index is 0.1 queries per second, and <code>GetQuerySuggestions</code> capacity has a base of 2.5 calls per second. If you add another 0.1 queries per second to total 0.2 queries per second for an index, the <code>GetQuerySuggestions</code> capacity is 2.5 calls per second (higher than five times 0.2 queries per second).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityUnitsConfiguration) -> dict:
    out: dict = {}
    out["StorageCapacityUnits"] = value["storage_capacity_units"]
    out["QueryCapacityUnits"] = value["query_capacity_units"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityUnitsConfiguration:
    out: CapacityUnitsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StorageCapacityUnits") is not None:
        out["storage_capacity_units"] = data["StorageCapacityUnits"]
    else:
        raise DeserializationError(
            "CapacityUnitsConfiguration.storage_capacity_units required"
        )
    if data.get("QueryCapacityUnits") is not None:
        out["query_capacity_units"] = data["QueryCapacityUnits"]
    else:
        raise DeserializationError(
            "CapacityUnitsConfiguration.query_capacity_units required"
        )
    return out
