"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListRLSPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.rls_policy_list
    import capo_lakeformation.types.token


class ListRLSPoliciesResponse(TypedDict, closed=True):
    rls_policies: NotRequired["capo_lakeformation.types.rls_policy_list.RLSPolicyList"]
    """<p>A list of <code>RLSPolicy</code> structures.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if not all row-level security policies have been returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRLSPoliciesResponse) -> dict:
    out: dict = {}
    if "rls_policies" in value:
        import capo_lakeformation.types.rls_policy_list

        out["RLSPolicies"] = capo_lakeformation.types.rls_policy_list.serialize_json(
            value["rls_policies"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRLSPoliciesResponse:
    out: ListRLSPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("RLSPolicies") is not None:
        import capo_lakeformation.types.rls_policy_list

        out["rls_policies"] = capo_lakeformation.types.rls_policy_list.deserialize_json(
            data["RLSPolicies"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
