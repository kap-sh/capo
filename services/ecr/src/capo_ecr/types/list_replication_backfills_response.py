"""Generated from Smithy shape ``com.amazonaws.ecr#ListReplicationBackfillsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.replication_backfill_summary_list


class ListReplicationBackfillsResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    backfills: NotRequired[
        "capo_ecr.types.replication_backfill_summary_list.ReplicationBackfillSummaryList"
    ]
    """<p>A list of the replication backfills for the registry.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListReplicationBackfills</code> request. When the results of a <code>ListReplicationBackfills</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReplicationBackfillsResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "backfills" in value:
        import capo_ecr.types.replication_backfill_summary_list

        out["backfills"] = (
            capo_ecr.types.replication_backfill_summary_list.serialize_aws_json_1_1(
                value["backfills"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReplicationBackfillsResponse:
    out: ListReplicationBackfillsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("backfills") is not None:
        import capo_ecr.types.replication_backfill_summary_list

        out["backfills"] = (
            capo_ecr.types.replication_backfill_summary_list.deserialize_aws_json_1_1(
                data["backfills"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
