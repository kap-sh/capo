"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.license_asset_group_configuration_list
    import capo_license_manager.types.license_asset_group_property_list
    import capo_license_manager.types.license_asset_group_status
    import capo_license_manager.types.license_asset_resource_description
    import capo_license_manager.types.license_asset_resource_name
    import capo_license_manager.types.license_asset_ruleset_arn_list
    import capo_license_manager.types.string


class UpdateLicenseAssetGroupRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
    ]
    """<p>License asset group name.</p>"""
    description: NotRequired[
        "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
    ]
    """<p>License asset group description.</p>"""
    license_asset_group_configurations: NotRequired[
        "capo_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList"
    ]
    """<p>License asset group configurations.</p>"""
    associated_license_asset_ruleset_ar_ns: "capo_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList"
    """<p>ARNs of associated license asset rulesets.</p>"""
    properties: NotRequired[
        "capo_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
    ]
    """<p>License asset group properties.</p>"""
    license_asset_group_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license asset group.</p>"""
    status: NotRequired[
        "capo_license_manager.types.license_asset_group_status.LicenseAssetGroupStatus"
    ]
    """<p>License asset group status. The possible values are <code>ACTIVE</code> | <code>DISABLED</code>.</p>"""
    client_token: "capo_license_manager.types.string.String"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "license_asset_group_configurations" in value:
        import capo_license_manager.types.license_asset_group_configuration_list

        out["LicenseAssetGroupConfigurations"] = (
            capo_license_manager.types.license_asset_group_configuration_list.serialize_aws_json_1_1(
                value["license_asset_group_configurations"]
            )
        )
    import capo_license_manager.types.license_asset_ruleset_arn_list

    out["AssociatedLicenseAssetRulesetARNs"] = (
        capo_license_manager.types.license_asset_ruleset_arn_list.serialize_aws_json_1_1(
            value["associated_license_asset_ruleset_ar_ns"]
        )
    )
    if "properties" in value:
        import capo_license_manager.types.license_asset_group_property_list

        out["Properties"] = (
            capo_license_manager.types.license_asset_group_property_list.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    out["LicenseAssetGroupArn"] = value["license_asset_group_arn"]
    if "status" in value:
        import capo_license_manager.types.license_asset_group_status

        out["Status"] = (
            capo_license_manager.types.license_asset_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLicenseAssetGroupRequest:
    out: UpdateLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LicenseAssetGroupConfigurations") is not None:
        import capo_license_manager.types.license_asset_group_configuration_list

        out["license_asset_group_configurations"] = (
            capo_license_manager.types.license_asset_group_configuration_list.deserialize_aws_json_1_1(
                data["LicenseAssetGroupConfigurations"]
            )
        )
    if data.get("AssociatedLicenseAssetRulesetARNs") is not None:
        import capo_license_manager.types.license_asset_ruleset_arn_list

        out["associated_license_asset_ruleset_ar_ns"] = (
            capo_license_manager.types.license_asset_ruleset_arn_list.deserialize_aws_json_1_1(
                data["AssociatedLicenseAssetRulesetARNs"]
            )
        )
    else:
        out["associated_license_asset_ruleset_ar_ns"] = []
    if data.get("Properties") is not None:
        import capo_license_manager.types.license_asset_group_property_list

        out["properties"] = (
            capo_license_manager.types.license_asset_group_property_list.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if data.get("LicenseAssetGroupArn") is not None:
        out["license_asset_group_arn"] = data["LicenseAssetGroupArn"]
    else:
        out["license_asset_group_arn"] = ""
    if data.get("Status") is not None:
        import capo_license_manager.types.license_asset_group_status

        out["status"] = (
            capo_license_manager.types.license_asset_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
