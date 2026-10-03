"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DescribeBackupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backups_max_size
    import capo_cloudhsm_v2.types.boolean
    import capo_cloudhsm_v2.types.filters
    import capo_cloudhsm_v2.types.next_token


class DescribeBackupsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudhsm_v2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value that you received in the previous response. Use this value to get more backups.</p>"""
    max_results: NotRequired["capo_cloudhsm_v2.types.backups_max_size.BackupsMaxSize"]
    """<p>The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a <code>NextToken</code> value.</p>"""
    filters: NotRequired["capo_cloudhsm_v2.types.filters.Filters"]
    """<p>One or more filters to limit the items returned in the response.</p> <p>Use the <code>backupIds</code> filter to return only the specified backups. Specify backups by their backup identifier (ID).</p> <p>Use the <code>sourceBackupIds</code> filter to return only the backups created from a source backup. The <code>sourceBackupID</code> of a source backup is returned by the <a>CopyBackupToRegion</a> operation.</p> <p>Use the <code>clusterIds</code> filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).</p> <p>Use the <code>states</code> filter to return only backups that match the specified state.</p> <p>Use the <code>neverExpires</code> filter to return backups filtered by the value in the <code>neverExpires</code> parameter. <code>True</code> returns all backups exempt from the backup retention policy. <code>False</code> returns all backups with a backup retention policy defined at the cluster.</p>"""
    shared: NotRequired["capo_cloudhsm_v2.types.boolean.Boolean"]
    """<p>Describe backups that are shared with you.</p> <note> <p>By default when using this option, the command returns backups that have been shared using a standard Resource Access Manager resource share. In order for a backup that was shared using the PutResourcePolicy command to be returned, the share must be promoted to a standard resource share using the RAM <a href="https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html">PromoteResourceShareCreatedFromPolicy</a> API operation. For more information about sharing backups, see <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html"> Working with shared backups</a> in the CloudHSM User Guide.</p> </note>"""
    sort_ascending: NotRequired["capo_cloudhsm_v2.types.boolean.Boolean"]
    """<p>Designates whether or not to sort the return backups by ascending chronological order of generation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBackupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_cloudhsm_v2.types.filters

        out["Filters"] = capo_cloudhsm_v2.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "shared" in value:
        out["Shared"] = value["shared"]
    if "sort_ascending" in value:
        out["SortAscending"] = value["sort_ascending"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBackupsRequest:
    out: DescribeBackupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_cloudhsm_v2.types.filters

        out["filters"] = capo_cloudhsm_v2.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("Shared") is not None:
        out["shared"] = data["Shared"]
    if data.get("SortAscending") is not None:
        out["sort_ascending"] = data["SortAscending"]
    return out
