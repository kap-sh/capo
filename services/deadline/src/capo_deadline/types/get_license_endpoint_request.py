"""Generated from Smithy shape ``com.amazonaws.deadline#GetLicenseEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id


class GetLicenseEndpointRequest(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """The license endpoint ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetLicenseEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLicenseEndpointRequest:
    out: GetLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
