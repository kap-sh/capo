"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListEarthObservationJobOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_list
    import capo_sagemaker_geospatial.types.next_token


class ListEarthObservationJobOutput(TypedDict, closed=True):
    earth_observation_job_summaries: "capo_sagemaker_geospatial.types.earth_observation_job_list.EarthObservationJobList"
    """<p>Contains summary information about the Earth Observation jobs.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEarthObservationJobOutput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.earth_observation_job_list

    out["EarthObservationJobSummaries"] = (
        capo_sagemaker_geospatial.types.earth_observation_job_list.serialize_json(
            value["earth_observation_job_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEarthObservationJobOutput:
    out: ListEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("EarthObservationJobSummaries") is not None:
        import capo_sagemaker_geospatial.types.earth_observation_job_list

        out["earth_observation_job_summaries"] = (
            capo_sagemaker_geospatial.types.earth_observation_job_list.deserialize_json(
                data["EarthObservationJobSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutput.earth_observation_job_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListEarthObservationJobOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
