"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeCustomDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.custom_domain_list
    import capo_apprunner.types.string
    import capo_apprunner.types.vpc_dns_target_list


class DescribeCustomDomainsResponse(TypedDict, closed=True):
    dns_target: "capo_apprunner.types.string.String"
    """<p>The App Runner subdomain of the App Runner service. The associated custom domain names are mapped to this target name.</p>"""
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service whose associated custom domain names you want to describe.</p>"""
    custom_domains: "capo_apprunner.types.custom_domain_list.CustomDomainList"
    """<p>A list of descriptions of custom domain names that are associated with the service. In a paginated request, the request returns up to <code>MaxResults</code> records per call.</p>"""
    vpc_dns_targets: "capo_apprunner.types.vpc_dns_target_list.VpcDNSTargetList"
    """<p>DNS Target records for the custom domains of this Amazon VPC. </p>"""
    next_token: NotRequired["capo_apprunner.types.string.String"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeCustomDomainsResponse) -> dict:
    out: dict = {}
    out["DNSTarget"] = value["dns_target"]
    out["ServiceArn"] = value["service_arn"]
    import capo_apprunner.types.custom_domain_list

    out["CustomDomains"] = (
        capo_apprunner.types.custom_domain_list.serialize_aws_json_1_0(
            value["custom_domains"]
        )
    )
    import capo_apprunner.types.vpc_dns_target_list

    out["VpcDNSTargets"] = (
        capo_apprunner.types.vpc_dns_target_list.serialize_aws_json_1_0(
            value["vpc_dns_targets"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeCustomDomainsResponse:
    out: DescribeCustomDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DNSTarget") is not None:
        out["dns_target"] = data["DNSTarget"]
    else:
        out["dns_target"] = ""
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    if data.get("CustomDomains") is not None:
        import capo_apprunner.types.custom_domain_list

        out["custom_domains"] = (
            capo_apprunner.types.custom_domain_list.deserialize_aws_json_1_0(
                data["CustomDomains"]
            )
        )
    else:
        out["custom_domains"] = []
    if data.get("VpcDNSTargets") is not None:
        import capo_apprunner.types.vpc_dns_target_list

        out["vpc_dns_targets"] = (
            capo_apprunner.types.vpc_dns_target_list.deserialize_aws_json_1_0(
                data["VpcDNSTargets"]
            )
        )
    else:
        out["vpc_dns_targets"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
