"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.volume_id_string_list


class DescribeVolumesModificationsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    volume_ids: NotRequired["capo_ec2.types.volume_id_string_list.VolumeIdStringList"]
    """<p>The IDs of the volumes.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>modification-state</code> - The current modification state (modifying | optimizing | completed | failed).</p> </li> <li> <p> <code>original-iops</code> - The original IOPS rate of the volume.</p> </li> <li> <p> <code>original-size</code> - The original size of the volume, in GiB.</p> </li> <li> <p> <code>original-volume-type</code> - The original volume type of the volume (standard | io1 | io2 | gp2 | sc1 | st1).</p> </li> <li> <p> <code>originalMultiAttachEnabled</code> - Indicates whether Multi-Attach support was enabled (true | false).</p> </li> <li> <p> <code>start-time</code> - The modification start time.</p> </li> <li> <p> <code>target-iops</code> - The target IOPS rate of the volume.</p> </li> <li> <p> <code>target-size</code> - The target size of the volume, in GiB.</p> </li> <li> <p> <code>target-volume-type</code> - The target volume type of the volume (standard | io1 | io2 | gp2 | sc1 | st1).</p> </li> <li> <p> <code>targetMultiAttachEnabled</code> - Indicates whether Multi-Attach support is to be enabled (true | false).</p> </li> <li> <p> <code>volume-id</code> - The ID of the volume.</p> </li> </ul>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of results (up to a limit of 500) to be returned in a paginated request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    include_managed_resources: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumesModificationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "volume_ids" in value:
        import capo_ec2.types.volume_id_string_list

        capo_ec2.types.volume_id_string_list.serialize_ec2_query(
            value["volume_ids"], pairs, f"{key_prefix}VolumeId"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeVolumesModificationsRequest:
    out: DescribeVolumesModificationsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_volume_ids = el.find("VolumeId")
    if child_volume_ids is not None:
        import capo_ec2.types.volume_id_string_list

        out["volume_ids"] = capo_ec2.types.volume_id_string_list.deserialize_ec2_query(
            child_volume_ids
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    return out
