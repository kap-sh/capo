"""Generated from Smithy shape ``com.amazonaws.eks#ListAccessPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.access_policies_list
    import capo_eks.types.string


class ListAccessPoliciesResponse(TypedDict, closed=True):
    access_policies: NotRequired[
        "capo_eks.types.access_policies_list.AccessPoliciesList"
    ]
    """<p>The list of available access policies. You can't view the contents of an access policy using the API. To view the contents, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html#access-policy-permissions">Access policy permissions</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessPoliciesResponse) -> dict:
    out: dict = {}
    if "access_policies" in value:
        import capo_eks.types.access_policies_list

        out["accessPolicies"] = capo_eks.types.access_policies_list.serialize_json(
            value["access_policies"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessPoliciesResponse:
    out: ListAccessPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPolicies") is not None:
        import capo_eks.types.access_policies_list

        out["access_policies"] = capo_eks.types.access_policies_list.deserialize_json(
            data["accessPolicies"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
