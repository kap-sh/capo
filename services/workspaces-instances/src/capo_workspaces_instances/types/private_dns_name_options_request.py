"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PrivateDnsNameOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.hostname_type_enum


class PrivateDnsNameOptionsRequest(TypedDict, closed=True):
    hostname_type: NotRequired[
        "capo_workspaces_instances.types.hostname_type_enum.HostnameTypeEnum"
    ]
    """<p>Specifies the type of hostname configuration.</p>"""
    enable_resource_name_dns_a_record: NotRequired["bool"]
    """<p>Enables DNS A record for resource name resolution.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired["bool"]
    """<p>Enables DNS AAAA record for resource name resolution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateDnsNameOptionsRequest) -> dict:
    out: dict = {}
    if "hostname_type" in value:
        import capo_workspaces_instances.types.hostname_type_enum

        out["HostnameType"] = (
            capo_workspaces_instances.types.hostname_type_enum.serialize_aws_json_1_0(
                value["hostname_type"]
            )
        )
    if "enable_resource_name_dns_a_record" in value:
        out["EnableResourceNameDnsARecord"] = value["enable_resource_name_dns_a_record"]
    if "enable_resource_name_dns_aaaa_record" in value:
        out["EnableResourceNameDnsAAAARecord"] = value[
            "enable_resource_name_dns_aaaa_record"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> PrivateDnsNameOptionsRequest:
    out: PrivateDnsNameOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("HostnameType") is not None:
        import capo_workspaces_instances.types.hostname_type_enum

        out["hostname_type"] = (
            capo_workspaces_instances.types.hostname_type_enum.deserialize_aws_json_1_0(
                data["HostnameType"]
            )
        )
    if data.get("EnableResourceNameDnsARecord") is not None:
        out["enable_resource_name_dns_a_record"] = data["EnableResourceNameDnsARecord"]
    if data.get("EnableResourceNameDnsAAAARecord") is not None:
        out["enable_resource_name_dns_aaaa_record"] = data[
            "EnableResourceNameDnsAAAARecord"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrivateDnsNameOptionsRequest) -> dict:
    out: dict = {}
    if "hostname_type" in value:
        import capo_workspaces_instances.types.hostname_type_enum

        out["HostnameType"] = (
            capo_workspaces_instances.types.hostname_type_enum.serialize_cbor(
                value["hostname_type"]
            )
        )
    if "enable_resource_name_dns_a_record" in value:
        out["EnableResourceNameDnsARecord"] = value["enable_resource_name_dns_a_record"]
    if "enable_resource_name_dns_aaaa_record" in value:
        out["EnableResourceNameDnsAAAARecord"] = value[
            "enable_resource_name_dns_aaaa_record"
        ]
    return out


def deserialize_cbor(data: dict) -> PrivateDnsNameOptionsRequest:
    out: PrivateDnsNameOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("HostnameType") is not None:
        import capo_workspaces_instances.types.hostname_type_enum

        out["hostname_type"] = (
            capo_workspaces_instances.types.hostname_type_enum.deserialize_cbor(
                data["HostnameType"]
            )
        )
    if data.get("EnableResourceNameDnsARecord") is not None:
        out["enable_resource_name_dns_a_record"] = data["EnableResourceNameDnsARecord"]
    if data.get("EnableResourceNameDnsAAAARecord") is not None:
        out["enable_resource_name_dns_aaaa_record"] = data[
            "EnableResourceNameDnsAAAARecord"
        ]
    return out
