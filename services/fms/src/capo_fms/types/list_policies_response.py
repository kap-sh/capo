"""Generated from Smithy shape ``com.amazonaws.fms#ListPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_token
    import capo_fms.types.policy_summary_list


class ListPoliciesResponse(TypedDict, closed=True):
    policy_list: NotRequired["capo_fms.types.policy_summary_list.PolicySummaryList"]
    """<p>An array of <code>PolicySummary</code> objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you have more <code>PolicySummary</code> objects than the number that you specified for <code>MaxResults</code> in the request, the response includes a <code>NextToken</code> value. To list more <code>PolicySummary</code> objects, submit another <code>ListPolicies</code> request, and specify the <code>NextToken</code> value from the response in the <code>NextToken</code> value in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    if "policy_list" in value:
        import capo_fms.types.policy_summary_list

        out["PolicyList"] = capo_fms.types.policy_summary_list.serialize_aws_json_1_1(
            value["policy_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyList") is not None:
        import capo_fms.types.policy_summary_list

        out["policy_list"] = (
            capo_fms.types.policy_summary_list.deserialize_aws_json_1_1(
                data["PolicyList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    if "policy_list" in value:
        import capo_fms.types.policy_summary_list

        out["PolicyList"] = capo_fms.types.policy_summary_list.serialize_cbor(
            value["policy_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("PolicyList") is not None:
        import capo_fms.types.policy_summary_list

        out["policy_list"] = capo_fms.types.policy_summary_list.deserialize_cbor(
            data["PolicyList"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
