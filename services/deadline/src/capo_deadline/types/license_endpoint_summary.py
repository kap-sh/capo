"""Generated from Smithy shape ``com.amazonaws.deadline#LicenseEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.license_endpoint_status
    import capo_deadline.types.status_message
    import capo_deadline.types.vpc_id


class LicenseEndpointSummary(TypedDict, closed=True):
    license_endpoint_id: NotRequired[
        "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    ]
    """The license endpoint ID."""
    status: NotRequired[
        "capo_deadline.types.license_endpoint_status.LicenseEndpointStatus"
    ]
    """The status of the license endpoint."""
    status_message: NotRequired["capo_deadline.types.status_message.StatusMessage"]
    """The status message of the license endpoint."""
    vpc_id: NotRequired["capo_deadline.types.vpc_id.VpcId"]
    """The VPC (virtual private cloud) ID associated with the license endpoint."""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseEndpointSummary) -> dict:
    out: dict = {}
    if "license_endpoint_id" in value:
        out["licenseEndpointId"] = value["license_endpoint_id"]
    if "status" in value:
        import capo_deadline.types.license_endpoint_status

        out["status"] = capo_deadline.types.license_endpoint_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> LicenseEndpointSummary:
    out: LicenseEndpointSummary = {}  # type: ignore[typeddict-item]
    if data.get("licenseEndpointId") is not None:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    if data.get("status") is not None:
        import capo_deadline.types.license_endpoint_status

        out["status"] = capo_deadline.types.license_endpoint_status.deserialize_json(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    return out
