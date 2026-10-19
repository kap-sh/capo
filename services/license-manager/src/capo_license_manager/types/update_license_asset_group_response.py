"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class UpdateLicenseAssetGroupResponse(TypedDict, closed=True):
    license_asset_group_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: "capo_license_manager.types.string.String"
    """<p>License asset group status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetGroupResponse) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetGroupResponse:
    out: UpdateLicenseAssetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("LicenseAssetGroupArn") is not None:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        out["license_asset_group_arn"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    return out
