"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_boolean
    import capo_ec2.types.boxed_long
    import capo_ec2.types.ipam_prefix_list_resolver_target_id
    import capo_ec2.types.string


class ModifyIpamPrefixListResolverTargetRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target to modify.</p>"""
    desired_version: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The desired version of the prefix list to target. This allows you to pin the target to a specific version.</p>"""
    track_latest_version: NotRequired["capo_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, the target will always synchronize with the most current version.</p> <p>Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPrefixListResolverTargetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_prefix_list_resolver_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverTargetId",
                str(value["ipam_prefix_list_resolver_target_id"]),
            )
        )
    if "desired_version" in value:
        pairs.append((f"{key_prefix}DesiredVersion", str(value["desired_version"])))
    if "track_latest_version" in value:
        pairs.append(
            (
                f"{key_prefix}TrackLatestVersion",
                "true" if value["track_latest_version"] else "false",
            )
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> ModifyIpamPrefixListResolverTargetRequest:
    out: ModifyIpamPrefixListResolverTargetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_prefix_list_resolver_target_id = el.find(
        "IpamPrefixListResolverTargetId"
    )
    if child_ipam_prefix_list_resolver_target_id is not None:
        out["ipam_prefix_list_resolver_target_id"] = str(
            child_ipam_prefix_list_resolver_target_id.text or ""
        )
    child_desired_version = el.find("DesiredVersion")
    if child_desired_version is not None:
        out["desired_version"] = int(child_desired_version.text or "")
    child_track_latest_version = el.find("TrackLatestVersion")
    if child_track_latest_version is not None:
        out["track_latest_version"] = (
            child_track_latest_version.text or ""
        ).lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
