"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.string


class GetLicenseRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    version: NotRequired["capo_license_manager.types.string.String"]
    """<p>License version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseRequest:
    out: GetLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
