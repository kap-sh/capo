"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type
    import capo_iam.types.policy_path_type
    import capo_iam.types.policy_scope_type
    import capo_iam.types.policy_usage_type


class ListPoliciesRequest(TypedDict, closed=True):
    scope: NotRequired["capo_iam.types.policy_scope_type.policyScopeType"]
    """<p>The scope to use for filtering the results.</p> <p>To list only Amazon Web Services managed policies, set <code>Scope</code> to <code>AWS</code>. To list only the customer managed policies in your Amazon Web Services account, set <code>Scope</code> to <code>Local</code>.</p> <p>This parameter is optional. If it is not included, or if it is set to <code>All</code>, all policies are returned.</p>"""
    only_attached: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag to filter the results to only the attached policies.</p> <p>When <code>OnlyAttached</code> is <code>true</code>, the returned list contains only the policies that are attached to an IAM user, group, or role. When <code>OnlyAttached</code> is <code>false</code>, or when the parameter is not included, all policies are returned.</p>"""
    path_prefix: NotRequired["capo_iam.types.policy_path_type.policyPathType"]
    r"""<p>The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    policy_usage_filter: NotRequired["capo_iam.types.policy_usage_type.PolicyUsageType"]
    """<p>The policy usage method to use for filtering the results.</p> <p>To list only permissions policies, set <code>PolicyUsageFilter</code> to <code>PermissionsPolicy</code>. To list only the policies used to set permissions boundaries, set the value to <code>PermissionsBoundary</code>.</p> <p>This parameter is optional. If it is not included, all policies are returned. </p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPoliciesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scope" in value:
        import capo_iam.types.policy_scope_type

        capo_iam.types.policy_scope_type.serialize_query(
            value["scope"], pairs, f"{key_prefix}Scope"
        )
    pairs.append(
        (
            f"{key_prefix}OnlyAttached",
            "true" if value.get("only_attached", False) else "false",
        )
    )
    if "path_prefix" in value:
        pairs.append((f"{key_prefix}PathPrefix", str(value["path_prefix"])))
    if "policy_usage_filter" in value:
        import capo_iam.types.policy_usage_type

        capo_iam.types.policy_usage_type.serialize_query(
            value["policy_usage_filter"], pairs, f"{key_prefix}PolicyUsageFilter"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListPoliciesRequest:
    out: ListPoliciesRequest = {}  # type: ignore[typeddict-item]
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_iam.types.policy_scope_type

        out["scope"] = capo_iam.types.policy_scope_type.deserialize_query(child_scope)
    child_only_attached = el.find("OnlyAttached")
    if child_only_attached is not None:
        out["only_attached"] = (child_only_attached.text or "").lower() == "true"
    else:
        out["only_attached"] = False
    child_path_prefix = el.find("PathPrefix")
    if child_path_prefix is not None:
        out["path_prefix"] = str(child_path_prefix.text or "")
    child_policy_usage_filter = el.find("PolicyUsageFilter")
    if child_policy_usage_filter is not None:
        import capo_iam.types.policy_usage_type

        out["policy_usage_filter"] = capo_iam.types.policy_usage_type.deserialize_query(
            child_policy_usage_filter
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
