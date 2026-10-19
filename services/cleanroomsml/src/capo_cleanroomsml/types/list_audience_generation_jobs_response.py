"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceGenerationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_list
    import capo_cleanroomsml.types.next_token


class ListAudienceGenerationJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_generation_jobs: (
        "capo_cleanroomsml.types.audience_generation_job_list.AudienceGenerationJobList"
    )
    """<p>The audience generation jobs that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceGenerationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.audience_generation_job_list

    out["audienceGenerationJobs"] = (
        capo_cleanroomsml.types.audience_generation_job_list.serialize_json(
            value["audience_generation_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAudienceGenerationJobsResponse:
    out: ListAudienceGenerationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("audienceGenerationJobs") is not None:
        import capo_cleanroomsml.types.audience_generation_job_list

        out["audience_generation_jobs"] = (
            capo_cleanroomsml.types.audience_generation_job_list.deserialize_json(
                data["audienceGenerationJobs"]
            )
        )
    else:
        out["audience_generation_jobs"] = []
    return out
