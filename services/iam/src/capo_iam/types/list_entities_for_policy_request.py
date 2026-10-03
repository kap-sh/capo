"""Generated from Smithy shape ``com.amazonaws.iam#ListEntitiesForPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.entity_type
    import capo_iam.types.marker_type
    import capo_iam.types.max_items_type
    import capo_iam.types.path_type
    import capo_iam.types.policy_usage_type


class ListEntitiesForPolicyRequest(TypedDict, closed=True):
    policy_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    entity_filter: NotRequired["capo_iam.types.entity_type.EntityType"]
    """<p>The entity type to use for filtering the results.</p> <p>For example, when <code>EntityFilter</code> is <code>Role</code>, only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.</p>"""
    path_prefix: NotRequired["capo_iam.types.path_type.pathType"]
    r"""<p>The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p>"""
    policy_usage_filter: NotRequired["capo_iam.types.policy_usage_type.PolicyUsageType"]
    """<p>The policy usage method to use for filtering the results.</p> <p>To list only permissions policies, set <code>PolicyUsageFilter</code> to <code>PermissionsPolicy</code>. To list only the policies used to set permissions boundaries, set the value to <code>PermissionsBoundary</code>.</p> <p>This parameter is optional. If it is not included, all policies are returned. </p>"""
    marker: NotRequired["capo_iam.types.marker_type.markerType"]
    """<p>Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the <code>Marker</code> element in the response that you received to indicate where the next call should start.</p>"""
    max_items: NotRequired["capo_iam.types.max_items_type.maxItemsType"]
    """<p>Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the <code>IsTruncated</code> response element is <code>true</code>.</p> <p>If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the <code>IsTruncated</code> response element returns <code>true</code>, and <code>Marker</code> contains a value to include in the subsequent call that tells the service where to continue from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListEntitiesForPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyArn", str(value["policy_arn"])))
    if "entity_filter" in value:
        import capo_iam.types.entity_type

        capo_iam.types.entity_type.serialize_query(
            value["entity_filter"], pairs, f"{key_prefix}EntityFilter"
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


def deserialize_query(el: Element) -> ListEntitiesForPolicyRequest:
    out: ListEntitiesForPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_arn = el.find("PolicyArn")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    else:
        raise DeserializationError("ListEntitiesForPolicyRequest.policy_arn required")
    child_entity_filter = el.find("EntityFilter")
    if child_entity_filter is not None:
        import capo_iam.types.entity_type

        out["entity_filter"] = capo_iam.types.entity_type.deserialize_query(
            child_entity_filter
        )
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
