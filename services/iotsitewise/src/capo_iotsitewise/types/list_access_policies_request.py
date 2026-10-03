"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAccessPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.iam_arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.identity_id
    import capo_iotsitewise.types.identity_type
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.resource_type


class ListAccessPoliciesRequest(TypedDict, closed=True):
    identity_type: NotRequired["capo_iotsitewise.types.identity_type.IdentityType"]
    """<p>The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify <code>identityId</code>.</p>"""
    identity_id: NotRequired["capo_iotsitewise.types.identity_id.IdentityId"]
    """<p>The ID of the identity. This parameter is required if you specify <code>USER</code> or <code>GROUP</code> for <code>identityType</code>.</p>"""
    resource_type: NotRequired["capo_iotsitewise.types.resource_type.ResourceType"]
    """<p>The type of resource (portal or project). This parameter is required if you specify <code>resourceId</code>.</p>"""
    resource_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the resource. This parameter is required if you specify <code>resourceType</code>.</p>"""
    iam_arn: NotRequired["capo_iotsitewise.types.iam_arn.IamArn"]
    """<p>The ARN of the IAM user. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM ARNs</a> in the <i>IAM User Guide</i>. This parameter is required if you specify <code>IAM</code> for <code>identityType</code>.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessPoliciesRequest:
    out: ListAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
