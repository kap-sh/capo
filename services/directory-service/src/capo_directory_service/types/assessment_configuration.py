"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_instance_ids
    import capo_directory_service.types.customer_dns_ips
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.security_group_ids


class AssessmentConfiguration(TypedDict, closed=True):
    customer_dns_ips: "capo_directory_service.types.customer_dns_ips.CustomerDnsIps"
    """<p>A list of IP addresses for the DNS servers or domain controllers in your self-managed AD that are tested during the assessment.</p>"""
    dns_name: "capo_directory_service.types.directory_name.DirectoryName"
    """<p>The fully qualified domain name (FQDN) of the self-managed AD domain to assess.</p>"""
    vpc_settings: (
        "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
    )
    instance_ids: (
        "capo_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    )
    """<p>The identifiers of the self-managed instances with SSM that are used to perform connectivity and validation tests.</p>"""
    security_group_ids: NotRequired[
        "capo_directory_service.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>By default, the service attaches a security group to allow network access to the self-managed nodes in your Amazon VPC. You can optionally supply your own security group that allows network traffic to and from your self-managed domain controllers outside of your Amazon VPC. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentConfiguration) -> dict:
    out: dict = {}
    import capo_directory_service.types.customer_dns_ips

    out["CustomerDnsIps"] = (
        capo_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
            value["customer_dns_ips"]
        )
    )
    out["DnsName"] = value["dns_name"]
    import capo_directory_service.types.directory_vpc_settings

    out["VpcSettings"] = (
        capo_directory_service.types.directory_vpc_settings.serialize_aws_json_1_1(
            value["vpc_settings"]
        )
    )
    import capo_directory_service.types.assessment_instance_ids

    out["InstanceIds"] = (
        capo_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    )
    if "security_group_ids" in value:
        import capo_directory_service.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_directory_service.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentConfiguration:
    out: AssessmentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    else:
        out["customer_dns_ips"] = []
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    else:
        out["dns_name"] = ""
    if data.get("VpcSettings") is not None:
        import capo_directory_service.types.directory_vpc_settings

        out["vpc_settings"] = (
            capo_directory_service.types.directory_vpc_settings.deserialize_aws_json_1_1(
                data["VpcSettings"]
            )
        )
    else:
        raise DeserializationError("AssessmentConfiguration.vpc_settings required")
    if data.get("InstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    else:
        out["instance_ids"] = []
    if data.get("SecurityGroupIds") is not None:
        import capo_directory_service.types.security_group_ids

        out["security_group_ids"] = (
            capo_directory_service.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    return out
