"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.string


class DeleteLicenseRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""
    source_version: "capo_license_manager.types.string.String"
    """<p>Current version of the license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    out["SourceVersion"] = value["source_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseRequest:
    out: DeleteLicenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("SourceVersion") is not None:
        out["source_version"] = data["SourceVersion"]
    else:
        out["source_version"] = ""
    return out
