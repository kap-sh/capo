"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListRuleGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.resource_managed_status
    import capo_network_firewall.types.resource_managed_type
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.subscription_status


class ListRuleGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    scope: NotRequired[
        "capo_network_firewall.types.resource_managed_status.ResourceManagedStatus"
    ]
    """<p>The scope of the request. The default setting of <code>ACCOUNT</code> or a setting of <code>NULL</code> returns all of the rule groups in your account. A setting of <code>MANAGED</code> returns all available managed rule groups.</p>"""
    managed_type: NotRequired[
        "capo_network_firewall.types.resource_managed_type.ResourceManagedType"
    ]
    """<p>Indicates the general category of the Amazon Web Services managed rule group.</p>"""
    subscription_status: NotRequired[
        "capo_network_firewall.types.subscription_status.SubscriptionStatus"
    ]
    """<p>Filters the results to show only rule groups with the specified subscription status. Use this to find subscribed or unsubscribed rule groups.</p>"""
    type: NotRequired["capo_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "scope" in value:
        import capo_network_firewall.types.resource_managed_status

        out["Scope"] = (
            capo_network_firewall.types.resource_managed_status.serialize_aws_json_1_0(
                value["scope"]
            )
        )
    if "managed_type" in value:
        import capo_network_firewall.types.resource_managed_type

        out["ManagedType"] = (
            capo_network_firewall.types.resource_managed_type.serialize_aws_json_1_0(
                value["managed_type"]
            )
        )
    if "subscription_status" in value:
        import capo_network_firewall.types.subscription_status

        out["SubscriptionStatus"] = (
            capo_network_firewall.types.subscription_status.serialize_aws_json_1_0(
                value["subscription_status"]
            )
        )
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = (
            capo_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleGroupsRequest:
    out: ListRuleGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Scope") is not None:
        import capo_network_firewall.types.resource_managed_status

        out["scope"] = (
            capo_network_firewall.types.resource_managed_status.deserialize_aws_json_1_0(
                data["Scope"]
            )
        )
    if data.get("ManagedType") is not None:
        import capo_network_firewall.types.resource_managed_type

        out["managed_type"] = (
            capo_network_firewall.types.resource_managed_type.deserialize_aws_json_1_0(
                data["ManagedType"]
            )
        )
    if data.get("SubscriptionStatus") is not None:
        import capo_network_firewall.types.subscription_status

        out["subscription_status"] = (
            capo_network_firewall.types.subscription_status.deserialize_aws_json_1_0(
                data["SubscriptionStatus"]
            )
        )
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = (
            capo_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRuleGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "scope" in value:
        import capo_network_firewall.types.resource_managed_status

        out["Scope"] = (
            capo_network_firewall.types.resource_managed_status.serialize_cbor(
                value["scope"]
            )
        )
    if "managed_type" in value:
        import capo_network_firewall.types.resource_managed_type

        out["ManagedType"] = (
            capo_network_firewall.types.resource_managed_type.serialize_cbor(
                value["managed_type"]
            )
        )
    if "subscription_status" in value:
        import capo_network_firewall.types.subscription_status

        out["SubscriptionStatus"] = (
            capo_network_firewall.types.subscription_status.serialize_cbor(
                value["subscription_status"]
            )
        )
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = capo_network_firewall.types.rule_group_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> ListRuleGroupsRequest:
    out: ListRuleGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Scope") is not None:
        import capo_network_firewall.types.resource_managed_status

        out["scope"] = (
            capo_network_firewall.types.resource_managed_status.deserialize_cbor(
                data["Scope"]
            )
        )
    if data.get("ManagedType") is not None:
        import capo_network_firewall.types.resource_managed_type

        out["managed_type"] = (
            capo_network_firewall.types.resource_managed_type.deserialize_cbor(
                data["ManagedType"]
            )
        )
    if data.get("SubscriptionStatus") is not None:
        import capo_network_firewall.types.subscription_status

        out["subscription_status"] = (
            capo_network_firewall.types.subscription_status.deserialize_cbor(
                data["SubscriptionStatus"]
            )
        )
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = capo_network_firewall.types.rule_group_type.deserialize_cbor(
            data["Type"]
        )
    return out
