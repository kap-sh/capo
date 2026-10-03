"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsAccessScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.access_scope_path_list_request
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateNetworkInsightsAccessScopeRequest(TypedDict, closed=True):
    match_paths: NotRequired[
        "capo_ec2.types.access_scope_path_list_request.AccessScopePathListRequest"
    ]
    """<p>The paths to match.</p>"""
    exclude_paths: NotRequired[
        "capo_ec2.types.access_scope_path_list_request.AccessScopePathListRequest"
    ]
    """<p>The paths to exclude.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInsightsAccessScopeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "match_paths" in value:
        import capo_ec2.types.access_scope_path_list_request

        capo_ec2.types.access_scope_path_list_request.serialize_ec2_query(
            value["match_paths"], pairs, f"{key_prefix}MatchPath"
        )
    if "exclude_paths" in value:
        import capo_ec2.types.access_scope_path_list_request

        capo_ec2.types.access_scope_path_list_request.serialize_ec2_query(
            value["exclude_paths"], pairs, f"{key_prefix}ExcludePath"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateNetworkInsightsAccessScopeRequest:
    out: CreateNetworkInsightsAccessScopeRequest = {}  # type: ignore[typeddict-item]
    child_match_paths = el.find("MatchPath")
    if child_match_paths is not None:
        import capo_ec2.types.access_scope_path_list_request

        out["match_paths"] = (
            capo_ec2.types.access_scope_path_list_request.deserialize_ec2_query(
                child_match_paths
            )
        )
    child_exclude_paths = el.find("ExcludePath")
    if child_exclude_paths is not None:
        import capo_ec2.types.access_scope_path_list_request

        out["exclude_paths"] = (
            capo_ec2.types.access_scope_path_list_request.deserialize_ec2_query(
                child_exclude_paths
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
