"""Generated from Smithy shape ``com.amazonaws.sustainability#EstimatedCarbonEmissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimensions_map
    import capo_sustainability.types.emissions_map
    import capo_sustainability.types.model_version
    import capo_sustainability.types.time_period


class EstimatedCarbonEmissions(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p>The reporting period for emission values.</p>"""
    dimensions_values: "capo_sustainability.types.dimensions_map.DimensionsMap"
    """<p>The dimensions used to group emissions values.</p>"""
    model_version: "capo_sustainability.types.model_version.ModelVersion"
    """<p>The semantic version-formatted string that indicates the methodology version used to calculate the emission values. </p> <note> <p> The AWS Sustainability service reflects the most recent model version for every month. You will not see two entries for the same month with different <code>ModelVersion</code> values. To track the evolution of the methodology and compare emission values from previous versions, we recommend creating a <a href="https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html">Data Export</a>. </p> </note>"""
    emissions_values: "capo_sustainability.types.emissions_map.EmissionsMap"
    """<p>The emissions values for the requested emissions types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedCarbonEmissions) -> dict:
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
    import capo_sustainability.types.emissions_map

    out["EmissionsValues"] = capo_sustainability.types.emissions_map.serialize_json(
        value["emissions_values"]
    )
    return out


def deserialize_json(data: dict) -> EstimatedCarbonEmissions:
    out: EstimatedCarbonEmissions = {}  # type: ignore[typeddict-item]
    if data.get("TimePeriod") is not None:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError("EstimatedCarbonEmissions.time_period required")
    if data.get("DimensionsValues") is not None:
        import capo_sustainability.types.dimensions_map

        out["dimensions_values"] = (
            capo_sustainability.types.dimensions_map.deserialize_json(
                data["DimensionsValues"]
            )
        )
    else:
        raise DeserializationError(
            "EstimatedCarbonEmissions.dimensions_values required"
        )
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    else:
        raise DeserializationError("EstimatedCarbonEmissions.model_version required")
    if data.get("EmissionsValues") is not None:
        import capo_sustainability.types.emissions_map

        out["emissions_values"] = (
            capo_sustainability.types.emissions_map.deserialize_json(
                data["EmissionsValues"]
            )
        )
    else:
        raise DeserializationError("EstimatedCarbonEmissions.emissions_values required")
    return out
