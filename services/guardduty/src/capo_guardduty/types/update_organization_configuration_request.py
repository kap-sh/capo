"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.auto_enable_members
    import capo_guardduty.types.boolean
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.organization_data_source_configurations
    import capo_guardduty.types.organization_features_configurations


class UpdateOrganizationConfigurationRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The ID of the detector that configures the delegated administrator.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    auto_enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Represents whether to automatically enable member accounts in the organization. This applies to only new member accounts, not the existing member accounts. When a new account joins the organization, the chosen features will be enabled for them by default.</p> <p>Even though this is still supported, we recommend using <code>AutoEnableOrganizationMembers</code> to achieve the similar results. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>.</p>"""
    data_sources: NotRequired[
        "capo_guardduty.types.organization_data_source_configurations.OrganizationDataSourceConfigurations"
    ]
    """<p>Describes which data sources will be updated.</p>"""
    features: NotRequired[
        "capo_guardduty.types.organization_features_configurations.OrganizationFeaturesConfigurations"
    ]
    """<p>A list of features that will be configured for the organization.</p>"""
    auto_enable_organization_members: NotRequired[
        "capo_guardduty.types.auto_enable_members.AutoEnableMembers"
    ]
    """<p>Indicates the auto-enablement configuration of GuardDuty for the member accounts in the organization. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>. </p> <p>Use one of the following configuration values for <code>autoEnableOrganizationMembers</code>:</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have GuardDuty enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have GuardDuty enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> <p>It may take up to 24 hours to update the configuration for all the member accounts.</p> </li> <li> <p> <code>NONE</code>: Indicates that GuardDuty will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.</p> <p>When you update the auto-enable setting from <code>ALL</code> or <code>NEW</code> to <code>NONE</code>, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["autoEnable"] = value["auto_enable"]
    if "data_sources" in value:
        import capo_guardduty.types.organization_data_source_configurations

        out["dataSources"] = (
            capo_guardduty.types.organization_data_source_configurations.serialize_json(
                value["data_sources"]
            )
        )
    if "features" in value:
        import capo_guardduty.types.organization_features_configurations

        out["features"] = (
            capo_guardduty.types.organization_features_configurations.serialize_json(
                value["features"]
            )
        )
    if "auto_enable_organization_members" in value:
        import capo_guardduty.types.auto_enable_members

        out["autoEnableOrganizationMembers"] = (
            capo_guardduty.types.auto_enable_members.serialize_json(
                value["auto_enable_organization_members"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("autoEnable") is not None:
        out["auto_enable"] = data["autoEnable"]
    if data.get("dataSources") is not None:
        import capo_guardduty.types.organization_data_source_configurations

        out["data_sources"] = (
            capo_guardduty.types.organization_data_source_configurations.deserialize_json(
                data["dataSources"]
            )
        )
    if data.get("features") is not None:
        import capo_guardduty.types.organization_features_configurations

        out["features"] = (
            capo_guardduty.types.organization_features_configurations.deserialize_json(
                data["features"]
            )
        )
    if data.get("autoEnableOrganizationMembers") is not None:
        import capo_guardduty.types.auto_enable_members

        out["auto_enable_organization_members"] = (
            capo_guardduty.types.auto_enable_members.deserialize_json(
                data["autoEnableOrganizationMembers"]
            )
        )
    return out
