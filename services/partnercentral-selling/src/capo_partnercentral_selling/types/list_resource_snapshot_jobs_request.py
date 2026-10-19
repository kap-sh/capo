"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.resource_snapshot_job_status
    import capo_partnercentral_selling.types.sort_object


class ListResourceSnapshotJobsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    max_results: NotRequired["capo_partnercentral_selling.types.page_size.PageSize"]
    """<p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next set of results. </p>"""
    engagement_identifier: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p> The identifier of the engagement to filter the response. </p>"""
    status: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
    ]
    """<p> The status of the jobs to filter the response. </p>"""
    sort: NotRequired["capo_partnercentral_selling.types.sort_object.SortObject"]
    """<p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotJobsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engagement_identifier" in value:
        out["EngagementIdentifier"] = value["engagement_identifier"]
    if "status" in value:
        import capo_partnercentral_selling.types.resource_snapshot_job_status

        out["Status"] = (
            capo_partnercentral_selling.types.resource_snapshot_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_selling.types.sort_object

        out["Sort"] = (
            capo_partnercentral_selling.types.sort_object.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotJobsRequest:
    out: ListResourceSnapshotJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.resource_snapshot_job_status

        out["status"] = (
            capo_partnercentral_selling.types.resource_snapshot_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.sort_object

        out["sort"] = (
            capo_partnercentral_selling.types.sort_object.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    return out
