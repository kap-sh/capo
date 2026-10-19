"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLicenseEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.license_endpoint_id


class CreateLicenseEndpointResponse(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseEndpointResponse) -> dict:
    out: dict = {}
    out["licenseEndpointId"] = value["license_endpoint_id"]
    return out


def deserialize_json(data: dict) -> CreateLicenseEndpointResponse:
    out: CreateLicenseEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("licenseEndpointId") is not None:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    else:
        out["license_endpoint_id"] = ""
    return out
