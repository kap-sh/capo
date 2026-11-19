"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListTrafficPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.traffic_policy_list


class ListTrafficPoliciesResponse(TypedDict, closed=True):
    traffic_policies: NotRequired[
        "capo_mailmanager.types.traffic_policy_list.TrafficPolicyList"
    ]
    """<p>The list of traffic policies.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTrafficPoliciesResponse) -> dict:
    out: dict = {}
    if "traffic_policies" in value:
        import capo_mailmanager.types.traffic_policy_list

        out["TrafficPolicies"] = (
            capo_mailmanager.types.traffic_policy_list.serialize_aws_json_1_0(
                value["traffic_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTrafficPoliciesResponse:
    out: ListTrafficPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicies") is not None:
        import capo_mailmanager.types.traffic_policy_list

        out["traffic_policies"] = (
            capo_mailmanager.types.traffic_policy_list.deserialize_aws_json_1_0(
                data["TrafficPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTrafficPoliciesResponse) -> dict:
    out: dict = {}
    if "traffic_policies" in value:
        import capo_mailmanager.types.traffic_policy_list

        out["TrafficPolicies"] = (
            capo_mailmanager.types.traffic_policy_list.serialize_cbor(
                value["traffic_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTrafficPoliciesResponse:
    out: ListTrafficPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrafficPolicies") is not None:
        import capo_mailmanager.types.traffic_policy_list

        out["traffic_policies"] = (
            capo_mailmanager.types.traffic_policy_list.deserialize_cbor(
                data["TrafficPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
