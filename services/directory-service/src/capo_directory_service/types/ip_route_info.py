"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRouteInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.added_date_time
    import capo_directory_service.types.cidr_ip
    import capo_directory_service.types.cidr_ipv6
    import capo_directory_service.types.description
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.ip_route_status_msg
    import capo_directory_service.types.ip_route_status_reason


class IpRouteInfo(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>Identifier (ID) of the directory associated with the IP addresses.</p>"""
    cidr_ip: NotRequired["capo_directory_service.types.cidr_ip.CidrIp"]
    """<p>IP address block in the <a>IpRoute</a>.</p>"""
    cidr_ipv6: NotRequired["capo_directory_service.types.cidr_ipv6.CidrIpv6"]
    """<p>IPv6 address block in the <a>IpRoute</a>.</p>"""
    ip_route_status_msg: NotRequired[
        "capo_directory_service.types.ip_route_status_msg.IpRouteStatusMsg"
    ]
    """<p>The status of the IP address block.</p>"""
    added_date_time: NotRequired[
        "capo_directory_service.types.added_date_time.AddedDateTime"
    ]
    """<p>The date and time the address block was added to the directory.</p>"""
    ip_route_status_reason: NotRequired[
        "capo_directory_service.types.ip_route_status_reason.IpRouteStatusReason"
    ]
    """<p>The reason for the IpRouteStatusMsg.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>Description of the <a>IpRouteInfo</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRouteInfo) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    if "cidr_ipv6" in value:
        out["CidrIpv6"] = value["cidr_ipv6"]
    if "ip_route_status_msg" in value:
        import capo_directory_service.types.ip_route_status_msg

        out["IpRouteStatusMsg"] = (
            capo_directory_service.types.ip_route_status_msg.serialize_aws_json_1_1(
                value["ip_route_status_msg"]
            )
        )
    if "added_date_time" in value:
        import capo_directory_service.types.added_date_time

        out["AddedDateTime"] = (
            capo_directory_service.types.added_date_time.serialize_aws_json_1_1(
                value["added_date_time"]
            )
        )
    if "ip_route_status_reason" in value:
        out["IpRouteStatusReason"] = value["ip_route_status_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpRouteInfo:
    out: IpRouteInfo = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("CidrIp") is not None:
        out["cidr_ip"] = data["CidrIp"]
    if data.get("CidrIpv6") is not None:
        out["cidr_ipv6"] = data["CidrIpv6"]
    if data.get("IpRouteStatusMsg") is not None:
        import capo_directory_service.types.ip_route_status_msg

        out["ip_route_status_msg"] = (
            capo_directory_service.types.ip_route_status_msg.deserialize_aws_json_1_1(
                data["IpRouteStatusMsg"]
            )
        )
    if data.get("AddedDateTime") is not None:
        import capo_directory_service.types.added_date_time

        out["added_date_time"] = (
            capo_directory_service.types.added_date_time.deserialize_aws_json_1_1(
                data["AddedDateTime"]
            )
        )
    if data.get("IpRouteStatusReason") is not None:
        out["ip_route_status_reason"] = data["IpRouteStatusReason"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRouteInfo) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    if "cidr_ipv6" in value:
        out["CidrIpv6"] = value["cidr_ipv6"]
    if "ip_route_status_msg" in value:
        import capo_directory_service.types.ip_route_status_msg

        out["IpRouteStatusMsg"] = (
            capo_directory_service.types.ip_route_status_msg.serialize_cbor(
                value["ip_route_status_msg"]
            )
        )
    if "added_date_time" in value:
        import capo_directory_service.types.added_date_time

        out["AddedDateTime"] = (
            capo_directory_service.types.added_date_time.serialize_cbor(
                value["added_date_time"]
            )
        )
    if "ip_route_status_reason" in value:
        out["IpRouteStatusReason"] = value["ip_route_status_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> IpRouteInfo:
    out: IpRouteInfo = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("CidrIp") is not None:
        out["cidr_ip"] = data["CidrIp"]
    if data.get("CidrIpv6") is not None:
        out["cidr_ipv6"] = data["CidrIpv6"]
    if data.get("IpRouteStatusMsg") is not None:
        import capo_directory_service.types.ip_route_status_msg

        out["ip_route_status_msg"] = (
            capo_directory_service.types.ip_route_status_msg.deserialize_cbor(
                data["IpRouteStatusMsg"]
            )
        )
    if data.get("AddedDateTime") is not None:
        import capo_directory_service.types.added_date_time

        out["added_date_time"] = (
            capo_directory_service.types.added_date_time.deserialize_cbor(
                data["AddedDateTime"]
            )
        )
    if data.get("IpRouteStatusReason") is not None:
        out["ip_route_status_reason"] = data["IpRouteStatusReason"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
