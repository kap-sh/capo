"""Generated from Smithy shape ``com.amazonaws.sustainability#EstimatedWaterAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimensions_map
    import capo_sustainability.types.model_version
    import capo_sustainability.types.time_period
    import capo_sustainability.types.water_allocation_map


class EstimatedWaterAllocation(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p>The reporting period for water allocation values.</p>"""
    dimensions_values: "capo_sustainability.types.dimensions_map.DimensionsMap"
    """<p>The dimensions used to group water allocation values.</p>"""
    model_version: "capo_sustainability.types.model_version.ModelVersion"
    """<p>The semantic version-formatted string that indicates the methodology version used to calculate the water allocation values. </p> <note> <p> The AWS Sustainability service reflects the most recent model version for every month. You will not see two entries for the same month with different <code>ModelVersion</code> values. </p> </note>"""
    allocation_values: (
        "capo_sustainability.types.water_allocation_map.WaterAllocationMap"
    )
    """<p>The allocation values for the requested water allocation types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedWaterAllocation) -> dict:
    out: dict = {}
    import capo_sustainability.types.time_period

    out["TimePeriod"] = capo_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    import capo_sustainability.types.dimensions_map

    out["DimensionsValues"] = capo_sustainability.types.dimensions_map.serialize_json(
        value["dimensions_values"]
    )
    out["ModelVersion"] = value["model_version"]
    import capo_sustainability.types.water_allocation_map

    out["AllocationValues"] = (
        capo_sustainability.types.water_allocation_map.serialize_json(
            value["allocation_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> EstimatedWaterAllocation:
    out: EstimatedWaterAllocation = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError("EstimatedWaterAllocation.time_period required")
    if data.get("DimensionsValues") is not None:
        import capo_sustainability.types.dimensions_map

        out["dimensions_values"] = (
            capo_sustainability.types.dimensions_map.deserialize_json(
                data["DimensionsValues"]
            )
        )
    else:
        out["dimensions_values"] = {}
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    else:
        out["model_version"] = ""
    if data.get("AllocationValues") is not None:
        import capo_sustainability.types.water_allocation_map

        out["allocation_values"] = (
            capo_sustainability.types.water_allocation_map.deserialize_json(
                data["AllocationValues"]
            )
        )
    else:
        out["allocation_values"] = {}
    return out
