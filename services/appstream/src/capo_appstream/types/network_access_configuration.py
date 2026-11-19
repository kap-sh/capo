"""Generated from Smithy shape ``com.amazonaws.appstream#NetworkAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.string_list


class NetworkAccessConfiguration(TypedDict, closed=True):
    eni_private_ip_address: NotRequired["capo_appstream.types.string.String"]
    """<p>The private IP address of the elastic network interface that is attached to instances in your VPC.</p>"""
    eni_ipv6_addresses: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The IPv6 addresses assigned to the elastic network interface. This field supports IPv6 connectivity for WorkSpaces Applications instances.</p>"""
    eni_id: NotRequired["capo_appstream.types.string.String"]
    """<p>The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    if "eni_private_ip_address" in value:
        out["EniPrivateIpAddress"] = value["eni_private_ip_address"]
    if "eni_ipv6_addresses" in value:
        import capo_appstream.types.string_list

        out["EniIpv6Addresses"] = (
            capo_appstream.types.string_list.serialize_aws_json_1_1(
                value["eni_ipv6_addresses"]
            )
        )
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EniPrivateIpAddress") is not None:
        out["eni_private_ip_address"] = data["EniPrivateIpAddress"]
    if data.get("EniIpv6Addresses") is not None:
        import capo_appstream.types.string_list

        out["eni_ipv6_addresses"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["EniIpv6Addresses"]
            )
        )
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    if "eni_private_ip_address" in value:
        out["EniPrivateIpAddress"] = value["eni_private_ip_address"]
    if "eni_ipv6_addresses" in value:
        import capo_appstream.types.string_list

        out["EniIpv6Addresses"] = capo_appstream.types.string_list.serialize_cbor(
            value["eni_ipv6_addresses"]
        )
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EniPrivateIpAddress") is not None:
        out["eni_private_ip_address"] = data["EniPrivateIpAddress"]
    if data.get("EniIpv6Addresses") is not None:
        import capo_appstream.types.string_list

        out["eni_ipv6_addresses"] = capo_appstream.types.string_list.deserialize_cbor(
            data["EniIpv6Addresses"]
        )
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    return out
