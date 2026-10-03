"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.featured_results_set_name
    import capo_kendra.types.featured_results_set_status
    import capo_kendra.types.long


class FeaturedResultsSetSummary(TypedDict, closed=True):
    featured_results_set_id: NotRequired[
        "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    ]
    """<p>The identifier of the set of featured results.</p>"""
    featured_results_set_name: NotRequired[
        "capo_kendra.types.featured_results_set_name.FeaturedResultsSetName"
    ]
    """<p>The name for the set of featured results.</p>"""
    status: NotRequired[
        "capo_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
    ]
    """<p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    last_updated_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was last updated.</p>"""
    creation_timestamp: NotRequired["capo_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSetSummary) -> dict:
    out: dict = {}
    if "featured_results_set_id" in value:
        out["FeaturedResultsSetId"] = value["featured_results_set_id"]
    if "featured_results_set_name" in value:
        out["FeaturedResultsSetName"] = value["featured_results_set_name"]
    if "status" in value:
        import capo_kendra.types.featured_results_set_status

        out["Status"] = (
            capo_kendra.types.featured_results_set_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsSetSummary:
    out: FeaturedResultsSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("FeaturedResultsSetId") is not None:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    if data.get("FeaturedResultsSetName") is not None:
        out["featured_results_set_name"] = data["FeaturedResultsSetName"]
    if data.get("Status") is not None:
        import capo_kendra.types.featured_results_set_status

        out["status"] = (
            capo_kendra.types.featured_results_set_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if data.get("CreationTimestamp") is not None:
        out["creation_timestamp"] = data["CreationTimestamp"]
    return out
