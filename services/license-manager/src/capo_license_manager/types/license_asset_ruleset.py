"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRuleset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.license_asset_rule_list
    import capo_license_manager.types.string


class LicenseAssetRuleset(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>License asset ruleset name.</p>"""
    description: NotRequired["capo_license_manager.types.string.String"]
    """<p>License asset ruleset description.</p>"""
    rules: "capo_license_manager.types.license_asset_rule_list.LicenseAssetRuleList"
    """<p>License asset rules.</p>"""
    license_asset_ruleset_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset ruleset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRuleset) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_license_manager.types.license_asset_rule_list

    out["Rules"] = (
        capo_license_manager.types.license_asset_rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    out["LicenseAssetRulesetArn"] = value["license_asset_ruleset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetRuleset:
    out: LicenseAssetRuleset = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rules") is not None:
        import capo_license_manager.types.license_asset_rule_list

        out["rules"] = (
            capo_license_manager.types.license_asset_rule_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    if data.get("LicenseAssetRulesetArn") is not None:
        out["license_asset_ruleset_arn"] = data["LicenseAssetRulesetArn"]
    else:
        out["license_asset_ruleset_arn"] = ""
    return out
