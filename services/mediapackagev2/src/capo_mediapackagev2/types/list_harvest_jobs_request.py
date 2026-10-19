"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListHarvestJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.harvest_job_status
    import capo_mediapackagev2.types.list_resource_max_results
    import capo_mediapackagev2.types.resource_name


class ListHarvestJobsRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group to filter the harvest jobs by. If specified, only harvest jobs associated with channels in this group will be returned.</p>"""
    channel_name: NotRequired["capo_mediapackagev2.types.resource_name.ResourceName"]
    """<p>The name of the channel to filter the harvest jobs by. If specified, only harvest jobs associated with this channel will be returned.</p>"""
    origin_endpoint_name: NotRequired[
        "capo_mediapackagev2.types.resource_name.ResourceName"
    ]
    """<p>The name of the origin endpoint to filter the harvest jobs by. If specified, only harvest jobs associated with this origin endpoint will be returned.</p>"""
    status: NotRequired["capo_mediapackagev2.types.harvest_job_status.HarvestJobStatus"]
    """<p>The status to filter the harvest jobs by. If specified, only harvest jobs with this status will be returned.</p>"""
    max_results: NotRequired[
        "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
    ]
    """<p>The maximum number of harvest jobs to return in a single request. If not specified, a default value will be used.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination. Provide this value in subsequent requests to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarvestJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHarvestJobsRequest:
    out: ListHarvestJobsRequest = {}  # type: ignore[typeddict-item]
    return out
