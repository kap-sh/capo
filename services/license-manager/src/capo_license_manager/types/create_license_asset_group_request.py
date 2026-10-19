"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseAssetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_asset_group_configuration_list
    import capo_license_manager.types.license_asset_group_property_list
    import capo_license_manager.types.license_asset_resource_description
    import capo_license_manager.types.license_asset_resource_name
    import capo_license_manager.types.license_asset_ruleset_arn_list
    import capo_license_manager.types.string
    import capo_license_manager.types.tag_list


class CreateLicenseAssetGroupRequest(TypedDict, closed=True):
    name: "capo_license_manager.types.license_asset_resource_name.LicenseAssetResourceName"
    """<p>License asset group name.</p>"""
    description: NotRequired[
        "capo_license_manager.types.license_asset_resource_description.LicenseAssetResourceDescription"
    ]
    """<p>License asset group description.</p>"""
    license_asset_group_configurations: "capo_license_manager.types.license_asset_group_configuration_list.LicenseAssetGroupConfigurationList"
    """<p>License asset group configurations.</p>"""
    associated_license_asset_ruleset_ar_ns: "capo_license_manager.types.license_asset_ruleset_arn_list.LicenseAssetRulesetArnList"
    """<p>ARNs of associated license asset rulesets.</p>"""
    properties: NotRequired[
        "capo_license_manager.types.license_asset_group_property_list.LicenseAssetGroupPropertyList"
    ]
    """<p>License asset group properties.</p>"""
    tags: NotRequired["capo_license_manager.types.tag_list.TagList"]
    """<p>Tags to add to the license asset group.</p>"""
    client_token: "capo_license_manager.types.string.String"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseAssetGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "tags" in value:
        import capo_license_manager.types.tag_list

        out["Tags"] = capo_license_manager.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseAssetGroupRequest:
    out: CreateLicenseAssetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LicenseAssetGroupConfigurations") is not None:
        import capo_license_manager.types.license_asset_group_configuration_list

        out["license_asset_group_configurations"] = (
            capo_license_manager.types.license_asset_group_configuration_list.deserialize_aws_json_1_1(
                data["LicenseAssetGroupConfigurations"]
            )
        )
    else:
        out["license_asset_group_configurations"] = []
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
    if data.get("Tags") is not None:
        import capo_license_manager.types.tag_list

        out["tags"] = capo_license_manager.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
