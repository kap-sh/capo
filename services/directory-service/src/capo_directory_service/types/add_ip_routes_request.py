"""Generated from Smithy shape ``com.amazonaws.directoryservice#AddIpRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.ip_routes
    import capo_directory_service.types.update_security_group_for_directory_controllers


class AddIpRoutesRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier (ID) of the directory to which to add the address block.</p>"""
    ip_routes: "capo_directory_service.types.ip_routes.IpRoutes"
    """<p>IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your self-managed domain.</p>"""
    update_security_group_for_directory_controllers: "capo_directory_service.types.update_security_group_for_directory_controllers.UpdateSecurityGroupForDirectoryControllers"
    """<p>If set to true, updates the inbound and outbound rules of the security group that has the description: "Amazon Web Services created security group for <i>directory ID</i> directory controllers." Following are the new rules: </p> <p>Inbound:</p> <ul> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: DNS (UDP), Protocol: UDP, Range: 53, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: DNS (TCP), Protocol: TCP, Range: 53, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: LDAP, Protocol: TCP, Range: 389, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: All ICMP, Protocol: All, Range: N/A, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> </ul> <p></p> <p>Outbound:</p> <ul> <li> <p>Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0</p> </li> </ul> <p>These security rules impact an internal network interface that is not exposed publicly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddIpRoutesRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import capo_directory_service.types.ip_routes

    out["IpRoutes"] = capo_directory_service.types.ip_routes.serialize_aws_json_1_1(
        value["ip_routes"]
    )
    out["UpdateSecurityGroupForDirectoryControllers"] = value.get(
        "update_security_group_for_directory_controllers", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddIpRoutesRequest:
    out: AddIpRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("AddIpRoutesRequest.directory_id required")
    if data.get("IpRoutes") is not None:
        import capo_directory_service.types.ip_routes

        out["ip_routes"] = (
            capo_directory_service.types.ip_routes.deserialize_aws_json_1_1(
                data["IpRoutes"]
            )
        )
    else:
        raise DeserializationError("AddIpRoutesRequest.ip_routes required")
    if data.get("UpdateSecurityGroupForDirectoryControllers") is not None:
        out["update_security_group_for_directory_controllers"] = data[
            "UpdateSecurityGroupForDirectoryControllers"
        ]
    else:
        out["update_security_group_for_directory_controllers"] = False
    return out
