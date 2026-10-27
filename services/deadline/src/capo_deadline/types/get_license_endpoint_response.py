"""Generated from Smithy shape ``com.amazonaws.deadline#GetLicenseEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.dns_name
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.license_endpoint_status
    import capo_deadline.types.security_group_id_list
    import capo_deadline.types.status_message
    import capo_deadline.types.subnet_id_list
    import capo_deadline.types.vpc_id


class GetLicenseEndpointResponse(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """The license endpoint ID."""
    status: "capo_deadline.types.license_endpoint_status.LicenseEndpointStatus"
    """The status of the license endpoint."""
    status_message: "capo_deadline.types.status_message.StatusMessage"
    """The status message of the license endpoint."""
    vpc_id: NotRequired["capo_deadline.types.vpc_id.VpcId"]
    """The VPC (virtual private cloud) ID associated with the license endpoint."""
    dns_name: NotRequired["capo_deadline.types.dns_name.DnsName"]
    """The DNS name."""
    subnet_ids: NotRequired["capo_deadline.types.subnet_id_list.SubnetIdList"]
    """The subnet IDs."""
    security_group_ids: NotRequired[
        "capo_deadline.types.security_group_id_list.SecurityGroupIdList"
    ]
    """The security group IDs for the license endpoint."""


# --- restJson1 ser/de ---
def serialize_json(value: GetLicenseEndpointResponse) -> dict:
    out: dict = {}
    out["licenseEndpointId"] = value["license_endpoint_id"]
    import capo_deadline.types.license_endpoint_status

    out["status"] = capo_deadline.types.license_endpoint_status.serialize_json(
        value["status"]
    )
    out["statusMessage"] = value["status_message"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "dns_name" in value:
        out["dnsName"] = value["dns_name"]
    if "subnet_ids" in value:
        import capo_deadline.types.subnet_id_list

        out["subnetIds"] = capo_deadline.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_deadline.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_deadline.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLicenseEndpointResponse:
    out: GetLicenseEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("licenseEndpointId") is not None:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    else:
        out["license_endpoint_id"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.license_endpoint_status

        out["status"] = capo_deadline.types.license_endpoint_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.license_endpoint_status.LicenseEndpointStatus", ""
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    else:
        out["status_message"] = ""
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("dnsName") is not None:
        out["dns_name"] = data["dnsName"]
    if data.get("subnetIds") is not None:
        import capo_deadline.types.subnet_id_list

        out["subnet_ids"] = capo_deadline.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_deadline.types.security_group_id_list

        out["security_group_ids"] = (
            capo_deadline.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
