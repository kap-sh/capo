"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.organization_configuration_configuration_type
    import capo_securityhub.types.organization_configuration_status


class OrganizationConfiguration(TypedDict, closed=True):
    configuration_type: NotRequired[
        "capo_securityhub.types.organization_configuration_configuration_type.OrganizationConfigurationConfigurationType"
    ]
    """<p> Indicates whether the organization uses local or central configuration. </p> <p>If you use local configuration, the Security Hub CSPM delegated administrator can set <code>AutoEnable</code> to <code>true</code> and <code>AutoEnableStandards</code> to <code>DEFAULT</code>. This automatically enables Security Hub CSPM and default security standards in new organization accounts. These new account settings must be set separately in each Amazon Web Services Region, and settings may be different in each Region. </p> <p> If you use central configuration, the delegated administrator can create configuration policies. Configuration policies can be used to configure Security Hub CSPM, security standards, and security controls in multiple accounts and Regions. If you want new organization accounts to use a specific configuration, you can create a configuration policy and associate it with the root or specific organizational units (OUs). New accounts will inherit the policy from the root or their assigned OU. </p>"""
    status: NotRequired[
        "capo_securityhub.types.organization_configuration_status.OrganizationConfigurationStatus"
    ]
    """<p> Describes whether central configuration could be enabled as the <code>ConfigurationType</code> for the organization. If your <code>ConfigurationType</code> is local configuration, then the value of <code>Status</code> is always <code>ENABLED</code>. </p> <p> If the value of <code>Status</code> is <code>DISABLED</code>, central configuration is disabled because the organization is managed by Security Hub CSPM policies in Organizations. </p>"""
    status_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Provides an explanation if the value of <code>Status</code> is equal to <code>FAILED</code> when <code>ConfigurationType</code> is equal to <code>CENTRAL</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationConfiguration) -> dict:
    out: dict = {}
    if "configuration_type" in value:
        import capo_securityhub.types.organization_configuration_configuration_type

        out["ConfigurationType"] = (
            capo_securityhub.types.organization_configuration_configuration_type.serialize_json(
                value["configuration_type"]
            )
        )
    if "status" in value:
        import capo_securityhub.types.organization_configuration_status

        out["Status"] = (
            capo_securityhub.types.organization_configuration_status.serialize_json(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> OrganizationConfiguration:
    out: OrganizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationType") is not None:
        import capo_securityhub.types.organization_configuration_configuration_type

        out["configuration_type"] = (
            capo_securityhub.types.organization_configuration_configuration_type.deserialize_json(
                data["ConfigurationType"]
            )
        )
    if data.get("Status") is not None:
        import capo_securityhub.types.organization_configuration_status

        out["status"] = (
            capo_securityhub.types.organization_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
