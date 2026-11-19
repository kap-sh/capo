"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_instance_ids
    import capo_directory_service.types.ip_addrs


class HybridSettingsDescription(TypedDict, closed=True):
    self_managed_dns_ip_addrs: NotRequired[
        "capo_directory_service.types.ip_addrs.IpAddrs"
    ]
    """<p>The IP addresses of the DNS servers in your self-managed AD environment.</p>"""
    self_managed_instance_ids: NotRequired[
        "capo_directory_service.types.assessment_instance_ids.AssessmentInstanceIds"
    ]
    """<p>The identifiers of the self-managed instances with SSM used for hybrid directory operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridSettingsDescription) -> dict:
    out: dict = {}
    if "self_managed_dns_ip_addrs" in value:
        import capo_directory_service.types.ip_addrs

        out["SelfManagedDnsIpAddrs"] = (
            capo_directory_service.types.ip_addrs.serialize_aws_json_1_1(
                value["self_managed_dns_ip_addrs"]
            )
        )
    if "self_managed_instance_ids" in value:
        import capo_directory_service.types.assessment_instance_ids

        out["SelfManagedInstanceIds"] = (
            capo_directory_service.types.assessment_instance_ids.serialize_aws_json_1_1(
                value["self_managed_instance_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridSettingsDescription:
    out: HybridSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("SelfManagedDnsIpAddrs") is not None:
        import capo_directory_service.types.ip_addrs

        out["self_managed_dns_ip_addrs"] = (
            capo_directory_service.types.ip_addrs.deserialize_aws_json_1_1(
                data["SelfManagedDnsIpAddrs"]
            )
        )
    if data.get("SelfManagedInstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["self_managed_instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_aws_json_1_1(
                data["SelfManagedInstanceIds"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HybridSettingsDescription) -> dict:
    out: dict = {}
    if "self_managed_dns_ip_addrs" in value:
        import capo_directory_service.types.ip_addrs

        out["SelfManagedDnsIpAddrs"] = (
            capo_directory_service.types.ip_addrs.serialize_cbor(
                value["self_managed_dns_ip_addrs"]
            )
        )
    if "self_managed_instance_ids" in value:
        import capo_directory_service.types.assessment_instance_ids

        out["SelfManagedInstanceIds"] = (
            capo_directory_service.types.assessment_instance_ids.serialize_cbor(
                value["self_managed_instance_ids"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> HybridSettingsDescription:
    out: HybridSettingsDescription = {}  # type: ignore[typeddict-item]
    if data.get("SelfManagedDnsIpAddrs") is not None:
        import capo_directory_service.types.ip_addrs

        out["self_managed_dns_ip_addrs"] = (
            capo_directory_service.types.ip_addrs.deserialize_cbor(
                data["SelfManagedDnsIpAddrs"]
            )
        )
    if data.get("SelfManagedInstanceIds") is not None:
        import capo_directory_service.types.assessment_instance_ids

        out["self_managed_instance_ids"] = (
            capo_directory_service.types.assessment_instance_ids.deserialize_cbor(
                data["SelfManagedInstanceIds"]
            )
        )
    return out
