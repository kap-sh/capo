"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.ip_address_details
    import capo_global_accelerator.types.ip_address_family
    import capo_global_accelerator.types.ip_addresses


class IpSet(TypedDict, closed=True):
    ip_family: NotRequired["capo_global_accelerator.types.generic_string.GenericString"]
    """<p>IpFamily is deprecated and has been replaced by IpAddressFamily.</p>"""
    ip_addresses: NotRequired["capo_global_accelerator.types.ip_addresses.IpAddresses"]
    """<p>The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.</p>"""
    ip_address_family: NotRequired[
        "capo_global_accelerator.types.ip_address_family.IpAddressFamily"
    ]
    """<p>The types of IP addresses included in this IP set. </p>"""
    ip_address_details: NotRequired[
        "capo_global_accelerator.types.ip_address_details.IpAddressDetails"
    ]
    """<p>The array of IP addresses in the IP address set, with detailed information about the IP addresses. An IP address set can have a maximum of two IP addresses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpSet) -> dict:
    out: dict = {}
    if "ip_family" in value:
        out["IpFamily"] = value["ip_family"]
    if "ip_addresses" in value:
        import capo_global_accelerator.types.ip_addresses

        out["IpAddresses"] = (
            capo_global_accelerator.types.ip_addresses.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    if "ip_address_family" in value:
        import capo_global_accelerator.types.ip_address_family

        out["IpAddressFamily"] = (
            capo_global_accelerator.types.ip_address_family.serialize_aws_json_1_1(
                value["ip_address_family"]
            )
        )
    if "ip_address_details" in value:
        import capo_global_accelerator.types.ip_address_details

        out["IpAddressDetails"] = (
            capo_global_accelerator.types.ip_address_details.serialize_aws_json_1_1(
                value["ip_address_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IpSet:
    out: IpSet = {}  # type: ignore[typeddict-item]
    if data.get("IpFamily") is not None:
        out["ip_family"] = data["IpFamily"]
    if data.get("IpAddresses") is not None:
        import capo_global_accelerator.types.ip_addresses

        out["ip_addresses"] = (
            capo_global_accelerator.types.ip_addresses.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    if data.get("IpAddressFamily") is not None:
        import capo_global_accelerator.types.ip_address_family

        out["ip_address_family"] = (
            capo_global_accelerator.types.ip_address_family.deserialize_aws_json_1_1(
                data["IpAddressFamily"]
            )
        )
    if data.get("IpAddressDetails") is not None:
        import capo_global_accelerator.types.ip_address_details

        out["ip_address_details"] = (
            capo_global_accelerator.types.ip_address_details.deserialize_aws_json_1_1(
                data["IpAddressDetails"]
            )
        )
    return out
