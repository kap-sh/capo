"""Generated from Smithy shape ``com.amazonaws.deadline#ListMembershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.max_results
    import capo_deadline.types.membership_resource_types
    import capo_deadline.types.next_token
    import capo_deadline.types.region


class ListMembershipsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """The ID of the IAM Identity Center principal whose Deadline Cloud resource memberships you want to list."""
    identity_store_id: NotRequired[
        "capo_deadline.types.identity_store_id.IdentityStoreId"
    ]
    """The identity store ID that contains the principal. This parameter is required for callers that do not use a monitor session."""
    identity_center_region: NotRequired["capo_deadline.types.region.Region"]
    """The Region of the IAM Identity Center instance. If not provided, the service defaults to the Amazon Web Services Region in which you make the request."""
    resource_types: NotRequired[
        "capo_deadline.types.membership_resource_types.MembershipResourceTypes"
    ]
    """The resource types to include when listing the principal's memberships. If not specified, memberships for all supported resource types are returned."""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMembershipsRequest:
    out: ListMembershipsRequest = {}  # type: ignore[typeddict-item]
    return out
