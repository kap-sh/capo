"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverDnssecConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.resolver_dnssec_config_list


class ListResolverDnssecConfigsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If a response includes the last of the DNSSEC configurations that are associated with the current Amazon Web Services account, <code>NextToken</code> doesn't appear in the response.</p> <p>If a response doesn't include the last of the configurations, you can get more configurations by submitting another <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResolverDnssecConfigs.html">ListResolverDnssecConfigs</a> request. Get the value of <code>NextToken</code> that Amazon Route 53 returned in the previous response and include it in <code>NextToken</code> in the next request.</p>"""
    resolver_dnssec_configs: NotRequired[
        "capo_route53resolver.types.resolver_dnssec_config_list.ResolverDnssecConfigList"
    ]
    """<p>An array that contains one <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResolverDnssecConfig.html">ResolverDnssecConfig</a> element for each configuration for DNSSEC validation that is associated with the current Amazon Web Services account. It doesn't contain disabled DNSSEC configurations for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverDnssecConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resolver_dnssec_configs" in value:
        import capo_route53resolver.types.resolver_dnssec_config_list

        out["ResolverDnssecConfigs"] = (
            capo_route53resolver.types.resolver_dnssec_config_list.serialize_aws_json_1_1(
                value["resolver_dnssec_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverDnssecConfigsResponse:
    out: ListResolverDnssecConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResolverDnssecConfigs") is not None:
        import capo_route53resolver.types.resolver_dnssec_config_list

        out["resolver_dnssec_configs"] = (
            capo_route53resolver.types.resolver_dnssec_config_list.deserialize_aws_json_1_1(
                data["ResolverDnssecConfigs"]
            )
        )
    return out
