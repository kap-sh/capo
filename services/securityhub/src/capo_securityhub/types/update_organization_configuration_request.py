"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateOrganizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.auto_enable_standards
    import capo_securityhub.types.boolean
    import capo_securityhub.types.organization_configuration


class UpdateOrganizationConfigurationRequest(TypedDict, closed=True):
    auto_enable: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.</p> <p>If set to <code>true</code>, then Security Hub CSPM is automatically enabled in new accounts. If set to <code>false</code>, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is <code>false</code>.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>false</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.</p>"""
    auto_enable_standards: NotRequired[
        "capo_securityhub.types.auto_enable_standards.AutoEnableStandards"
    ]
    """<p>Whether to automatically enable Security Hub CSPM <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html">default standards</a> in new member accounts when they join the organization.</p> <p>The default value of this parameter is equal to <code>DEFAULT</code>.</p> <p>If equal to <code>DEFAULT</code>, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to <code>NONE</code>, then default standards are not automatically enabled for new member accounts.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>NONE</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.</p>"""
    organization_configuration: NotRequired[
        "capo_securityhub.types.organization_configuration.OrganizationConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationConfigurationRequest) -> dict:
    out: dict = {}
    if "auto_enable" in value:
        out["AutoEnable"] = value["auto_enable"]
    if "auto_enable_standards" in value:
        import capo_securityhub.types.auto_enable_standards

        out["AutoEnableStandards"] = (
            capo_securityhub.types.auto_enable_standards.serialize_json(
                value["auto_enable_standards"]
            )
        )
    if "organization_configuration" in value:
        import capo_securityhub.types.organization_configuration

        out["OrganizationConfiguration"] = (
            capo_securityhub.types.organization_configuration.serialize_json(
                value["organization_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOrganizationConfigurationRequest:
    out: UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoEnable") is not None:
        out["auto_enable"] = data["AutoEnable"]
    if data.get("AutoEnableStandards") is not None:
        import capo_securityhub.types.auto_enable_standards

        out["auto_enable_standards"] = (
            capo_securityhub.types.auto_enable_standards.deserialize_json(
                data["AutoEnableStandards"]
            )
        )
    if data.get("OrganizationConfiguration") is not None:
        import capo_securityhub.types.organization_configuration

        out["organization_configuration"] = (
            capo_securityhub.types.organization_configuration.deserialize_json(
                data["OrganizationConfiguration"]
            )
        )
    return out
