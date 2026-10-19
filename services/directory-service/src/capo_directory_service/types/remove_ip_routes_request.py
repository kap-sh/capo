"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveIpRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.cidr_ips
    import capo_directory_service.types.cidr_ipv6s
    import capo_directory_service.types.directory_id


class RemoveIpRoutesRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier (ID) of the directory from which you want to remove the IP addresses.</p>"""
    cidr_ips: NotRequired["capo_directory_service.types.cidr_ips.CidrIps"]
    """<p>IP address blocks that you want to remove.</p>"""
    cidr_ipv6s: NotRequired["capo_directory_service.types.cidr_ipv6s.CidrIpv6s"]
    """<p>IPv6 address blocks that you want to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveIpRoutesRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "cidr_ips" in value:
        import capo_directory_service.types.cidr_ips

        out["CidrIps"] = capo_directory_service.types.cidr_ips.serialize_aws_json_1_1(
            value["cidr_ips"]
        )
    if "cidr_ipv6s" in value:
        import capo_directory_service.types.cidr_ipv6s

        out["CidrIpv6s"] = (
            capo_directory_service.types.cidr_ipv6s.serialize_aws_json_1_1(
                value["cidr_ipv6s"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveIpRoutesRequest:
    out: RemoveIpRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("CidrIps") is not None:
        import capo_directory_service.types.cidr_ips

        out["cidr_ips"] = (
            capo_directory_service.types.cidr_ips.deserialize_aws_json_1_1(
                data["CidrIps"]
            )
        )
    if data.get("CidrIpv6s") is not None:
        import capo_directory_service.types.cidr_ipv6s

        out["cidr_ipv6s"] = (
            capo_directory_service.types.cidr_ipv6s.deserialize_aws_json_1_1(
                data["CidrIpv6s"]
            )
        )
    return out
