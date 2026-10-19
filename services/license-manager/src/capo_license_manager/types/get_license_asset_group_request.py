"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn


class GetLicenseAssetGroupRequest(TypedDict, closed=True):
    license_asset_group_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseAssetGroupRequest:
    out: GetLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseAssetGroupArn") is not None:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        out["license_asset_group_arn"] = ""
    return out
