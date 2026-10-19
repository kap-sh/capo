"""Generated from Smithy shape ``com.amazonaws.apprunner#AssociateCustomDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.custom_domain
    import capo_apprunner.types.string
    import capo_apprunner.types.vpc_dns_target_list


class AssociateCustomDomainResponse(TypedDict, closed=True):
    dns_target: "capo_apprunner.types.string.String"
    """<p>The App Runner subdomain of the App Runner service. The custom domain name is mapped to this target name.</p>"""
    service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service with which a custom domain name is associated.</p>"""
    custom_domain: "capo_apprunner.types.custom_domain.CustomDomain"
    """<p>A description of the domain name that's being associated.</p>"""
    vpc_dns_targets: "capo_apprunner.types.vpc_dns_target_list.VpcDNSTargetList"
    """<p>DNS Target records for the custom domains of this Amazon VPC. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateCustomDomainResponse) -> dict:
    out: dict = {}
    out["DNSTarget"] = value["dns_target"]
    out["ServiceArn"] = value["service_arn"]
    import capo_apprunner.types.custom_domain

    out["CustomDomain"] = capo_apprunner.types.custom_domain.serialize_aws_json_1_0(
        value["custom_domain"]
    )
    import capo_apprunner.types.vpc_dns_target_list

    out["VpcDNSTargets"] = (
        capo_apprunner.types.vpc_dns_target_list.serialize_aws_json_1_0(
            value["vpc_dns_targets"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateCustomDomainResponse:
    out: AssociateCustomDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("DNSTarget") is not None:
        out["dns_target"] = data["DNSTarget"]
    else:
        out["dns_target"] = ""
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    else:
        out["service_arn"] = ""
    if data.get("CustomDomain") is not None:
        import capo_apprunner.types.custom_domain

        out["custom_domain"] = (
            capo_apprunner.types.custom_domain.deserialize_aws_json_1_0(
                data["CustomDomain"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateCustomDomainResponse.custom_domain required"
        )
    if data.get("VpcDNSTargets") is not None:
        import capo_apprunner.types.vpc_dns_target_list

        out["vpc_dns_targets"] = (
            capo_apprunner.types.vpc_dns_target_list.deserialize_aws_json_1_0(
                data["VpcDNSTargets"]
            )
        )
    else:
        out["vpc_dns_targets"] = []
    return out
