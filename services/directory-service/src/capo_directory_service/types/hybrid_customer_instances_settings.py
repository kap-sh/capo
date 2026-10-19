"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridCustomerInstancesSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_instance_ids
    import capo_directory_service.types.customer_dns_ips


class HybridCustomerInstancesSettings(TypedDict, closed=True):
    customer_dns_ips: "capo_directory_service.types.customer_dns_ips.CustomerDnsIps"
    """<p>The IP addresses of the DNS servers or domain controllers in your self-managed AD environment.</p>"""
    instance_ids: (
        "capo_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    )
    """<p>The identifiers of the self-managed instances with SSM used in hybrid directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridCustomerInstancesSettings) -> dict:
    out: dict = {}
    import capo_directory_service.types.customer_dns_ips

    out["CustomerDnsIps"] = (
        capo_directory_service.types.customer_dns_ips.serialize_aws_json_1_1(
            value["customer_dns_ips"]
        )
    )
    import capo_directory_service.types.assessment_instance_ids

    out["InstanceIds"] = (
        capo_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
            value["instance_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridCustomerInstancesSettings:
    out: HybridCustomerInstancesSettings = {}  # type: ignore[typeddict-item]
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.customer_dns_ips

        out["customer_dns_ips"] = (
            capo_directory_service.types.customer_dns_ips.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    else:
        out["customer_dns_ips"] = []
    if data.get("InstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    else:
        out["instance_ids"] = []
    return out
