"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckInLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class CheckInLicenseRequest(TypedDict, closed=True):
    license_consumption_token: "capo_license_manager.types.string.String"
    """<p>License consumption token.</p>"""
    beneficiary: NotRequired["capo_license_manager.types.string.String"]
    """<p>License beneficiary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckInLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseConsumptionToken"] = value["license_consumption_token"]
    if "beneficiary" in value:
        out["Beneficiary"] = value["beneficiary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckInLicenseRequest:
    out: CheckInLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConsumptionToken") is not None:
        out["license_consumption_token"] = data["LicenseConsumptionToken"]
    else:
        out["license_consumption_token"] = ""
    if data.get("Beneficiary") is not None:
        out["beneficiary"] = data["Beneficiary"]
    return out
