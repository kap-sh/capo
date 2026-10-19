"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListDiscoveredResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.max_results_resources
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream
    import capo_migration_hub.types.token


class ListDiscoveredResourcesRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream.</p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The name of the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""
    next_token: NotRequired["capo_migration_hub.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""
    max_results: NotRequired[
        "capo_migration_hub.types.max_results_resources.MaxResultsResources"
    ]
    """<p>The maximum number of results returned per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesRequest:
    out: ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        out["progress_update_stream"] = ""
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        out["migration_task_name"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
