"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StopEarthObservationJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_arn


class StopEarthObservationJobInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopEarthObservationJobInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StopEarthObservationJobInput:
    out: StopEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
