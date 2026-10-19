"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseAssetRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn


class DeleteLicenseAssetRulesetRequest(TypedDict, closed=True):
    license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseAssetRulesetRequest) -> dict:
    out: dict = {}
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseAssetRulesetRequest:
    out: DeleteLicenseAssetRulesetRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseAssetRulesetArn") is not None:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        out["license_asset_ruleset_arn"] = ""
    return out
