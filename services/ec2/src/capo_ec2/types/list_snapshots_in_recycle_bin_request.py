"""Generated from Smithy shape ``com.amazonaws.ec2#ListSnapshotsInRecycleBinRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.list_snapshots_in_recycle_bin_max_results
    import capo_ec2.types.snapshot_id_string_list
    import capo_ec2.types.string


class ListSnapshotsInRecycleBinRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_ec2.types.list_snapshots_in_recycle_bin_max_results.ListSnapshotsInRecycleBinMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    snapshot_ids: NotRequired[
        "capo_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The IDs of the snapshots to list. Omit this parameter to list all of the snapshots that are in the Recycle Bin.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ListSnapshotsInRecycleBinRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "snapshot_ids" in value:
        import capo_ec2.types.snapshot_id_string_list

        capo_ec2.types.snapshot_id_string_list.serialize_ec2_query(
            value["snapshot_ids"], pairs, f"{key_prefix}SnapshotId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ListSnapshotsInRecycleBinRequest:
    out: ListSnapshotsInRecycleBinRequest = {}  # type: ignore[typeddict-item]
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_snapshot_ids = el.find("SnapshotId")
    if child_snapshot_ids is not None:
        import capo_ec2.types.snapshot_id_string_list

        out["snapshot_ids"] = (
            capo_ec2.types.snapshot_id_string_list.deserialize_ec2_query(
                child_snapshot_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
