"""Generated from Smithy shape ``com.amazonaws.ec2#ListVolumesInRecycleBinRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.volume_id_string_list


class ListVolumesInRecycleBinRequest(TypedDict, closed=True):
    volume_ids: NotRequired["capo_ec2.types.volume_id_string_list.VolumeIdStringList"]
    """<p>The IDs of the volumes to list. Omit this parameter to list all of the volumes that are in the Recycle Bin.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p> <p>Valid range: 5 - 500</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ListVolumesInRecycleBinRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "volume_ids" in value:
        import capo_ec2.types.volume_id_string_list

        capo_ec2.types.volume_id_string_list.serialize_ec2_query(
            value["volume_ids"], pairs, f"{key_prefix}VolumeId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> ListVolumesInRecycleBinRequest:
    out: ListVolumesInRecycleBinRequest = {}  # type: ignore[typeddict-item]
    child_volume_ids = el.find("VolumeId")
    if child_volume_ids is not None:
        import capo_ec2.types.volume_id_string_list

        out["volume_ids"] = capo_ec2.types.volume_id_string_list.deserialize_ec2_query(
            child_volume_ids
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
