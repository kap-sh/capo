"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.resource_snapshot_job_summary_list


class ListResourceSnapshotJobsResponse(TypedDict, closed=True):
    resource_snapshot_job_summaries: "capo_partnercentral_selling.types.resource_snapshot_job_summary_list.ResourceSnapshotJobSummaryList"
    """<p> An array of resource snapshot job summary objects. </p>"""
    next_token: NotRequired["str"]
    """<p> The token to retrieve the next set of results. If there are no additional results, this value is null. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotJobsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.resource_snapshot_job_summary_list

    out["ResourceSnapshotJobSummaries"] = (
        capo_partnercentral_selling.types.resource_snapshot_job_summary_list.serialize_aws_json_1_0(
            value["resource_snapshot_job_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotJobsResponse:
    out: ListResourceSnapshotJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceSnapshotJobSummaries") is not None:
        import capo_partnercentral_selling.types.resource_snapshot_job_summary_list

        out["resource_snapshot_job_summaries"] = (
            capo_partnercentral_selling.types.resource_snapshot_job_summary_list.deserialize_aws_json_1_0(
                data["ResourceSnapshotJobSummaries"]
            )
        )
    else:
        out["resource_snapshot_job_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
