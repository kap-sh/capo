"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetRulesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class UpdateLicenseAssetRulesetResponse(TypedDict, closed=True):
    license_asset_ruleset_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetRulesetResponse) -> dict:
    out: dict = {}
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetRulesetResponse:
    out: UpdateLicenseAssetRulesetResponse = {}  # type: ignore[typeddict-item]
    if data.get("LicenseAssetRulesetArn") is not None:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        out["license_asset_ruleset_arn"] = ""
    return out
