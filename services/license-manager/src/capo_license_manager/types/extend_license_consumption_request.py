"""Generated from Smithy shape ``com.amazonaws.licensemanager#ExtendLicenseConsumptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.boolean
    import capo_license_manager.types.string


class ExtendLicenseConsumptionRequest(TypedDict, closed=True):
    license_consumption_token: "capo_license_manager.types.string.String"
    """<p>License consumption token.</p>"""
    dry_run: NotRequired["capo_license_manager.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request. Provides an error response if you do not have the required permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendLicenseConsumptionRequest) -> dict:
    out: dict = {}
    out["LicenseConsumptionToken"] = value["license_consumption_token"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendLicenseConsumptionRequest:
    out: ExtendLicenseConsumptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConsumptionToken") is not None:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    else:
        raise DeserializationError(
            "ExtendLicenseConsumptionRequest.license_consumption_token required"
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
