"""Generated from Smithy shape ``com.amazonaws.kendraranking#CapacityUnitsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_capacity_unit


class CapacityUnitsConfiguration(TypedDict, closed=True):
    rescore_capacity_units: (
        "capo_kendra_ranking.types.rescore_capacity_unit.RescoreCapacityUnit"
    )
    """<p>The amount of extra capacity for your rescore execution plan.</p> <p>A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityUnitsConfiguration) -> dict:
    out: dict = {}
    out["RescoreCapacityUnits"] = value["rescore_capacity_units"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityUnitsConfiguration:
    out: CapacityUnitsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RescoreCapacityUnits") is not None:
        out["rescore_capacity_units"] = data["RescoreCapacityUnits"]
    else:
        out["rescore_capacity_units"] = 0
    return out
