"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.customizable_properties
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.parameter_definitions
    import capo_securityhub.types.region_availability_status
    import capo_securityhub.types.security_controls_provider
    import capo_securityhub.types.severity_rating


class SecurityControlDefinition(TypedDict, closed=True):
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number (for example, APIGateway.3). This parameter differs from <code>SecurityControlArn</code>, which is a unique Amazon Resource Name (ARN) assigned to a control. The ARN references the security control ID (for example, arn:aws:securityhub:eu-central-1:123456789012:security-control/APIGateway.3). </p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The title of a security control. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of a security control across standards. This typically summarizes how Security Hub CSPM evaluates the control and the conditions under which it produces a failed finding. This parameter doesn't reference a specific standard. </p>"""
    remediation_url: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A link to Security Hub CSPM documentation that explains how to remediate a failed finding for a security control. </p>"""
    severity_rating: NotRequired[
        "capo_securityhub.types.severity_rating.SeverityRating"
    ]
    """<p> The severity of a security control. For more information about how Security Hub CSPM determines control severity, see <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity">Assigning severity to control findings</a> in the <i>Security Hub CSPM User Guide</i>. </p>"""
    current_region_availability: NotRequired[
        "capo_securityhub.types.region_availability_status.RegionAvailabilityStatus"
    ]
    """<p> Specifies whether a security control is available in the current Amazon Web Services Region. </p>"""
    customizable_properties: NotRequired[
        "capo_securityhub.types.customizable_properties.CustomizableProperties"
    ]
    """<p> Security control properties that you can customize. Currently, only parameter customization is supported for select controls. An empty array is returned for controls that don’t support custom properties. </p>"""
    parameter_definitions: NotRequired[
        "capo_securityhub.types.parameter_definitions.ParameterDefinitions"
    ]
    """<p> An object that provides a security control parameter name, description, and the options for customizing it. This object is excluded for a control that doesn't support custom parameters. </p>"""
    provider: NotRequired[
        "capo_securityhub.types.security_controls_provider.SecurityControlsProvider"
    ]
    """<p>The cloud provider whose resources the security control evaluates. For example, <code>AWS</code> or <code>Azure</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlDefinition) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "remediation_url" in value:
        out["RemediationUrl"] = value["remediation_url"]
    if "severity_rating" in value:
        import capo_securityhub.types.severity_rating

        out["SeverityRating"] = capo_securityhub.types.severity_rating.serialize_json(
            value["severity_rating"]
        )
    if "current_region_availability" in value:
        import capo_securityhub.types.region_availability_status

        out["CurrentRegionAvailability"] = (
            capo_securityhub.types.region_availability_status.serialize_json(
                value["current_region_availability"]
            )
        )
    if "customizable_properties" in value:
        import capo_securityhub.types.customizable_properties

        out["CustomizableProperties"] = (
            capo_securityhub.types.customizable_properties.serialize_json(
                value["customizable_properties"]
            )
        )
    if "parameter_definitions" in value:
        import capo_securityhub.types.parameter_definitions

        out["ParameterDefinitions"] = (
            capo_securityhub.types.parameter_definitions.serialize_json(
                value["parameter_definitions"]
            )
        )
    if "provider" in value:
        import capo_securityhub.types.security_controls_provider

        out["Provider"] = (
            capo_securityhub.types.security_controls_provider.serialize_json(
                value["provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityControlDefinition:
    out: SecurityControlDefinition = {}  # type: ignore[typeddict-item]
    if data.get("SecurityControlId") is not None:
        out["security_control_id"] = data["SecurityControlId"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RemediationUrl") is not None:
        out["remediation_url"] = data["RemediationUrl"]
    if data.get("SeverityRating") is not None:
        import capo_securityhub.types.severity_rating

        out["severity_rating"] = (
            capo_securityhub.types.severity_rating.deserialize_json(
                data["SeverityRating"]
            )
        )
    if data.get("CurrentRegionAvailability") is not None:
        import capo_securityhub.types.region_availability_status

        out["current_region_availability"] = (
            capo_securityhub.types.region_availability_status.deserialize_json(
                data["CurrentRegionAvailability"]
            )
        )
    if data.get("CustomizableProperties") is not None:
        import capo_securityhub.types.customizable_properties

        out["customizable_properties"] = (
            capo_securityhub.types.customizable_properties.deserialize_json(
                data["CustomizableProperties"]
            )
        )
    if data.get("ParameterDefinitions") is not None:
        import capo_securityhub.types.parameter_definitions

        out["parameter_definitions"] = (
            capo_securityhub.types.parameter_definitions.deserialize_json(
                data["ParameterDefinitions"]
            )
        )
    if data.get("Provider") is not None:
        import capo_securityhub.types.security_controls_provider

        out["provider"] = (
            capo_securityhub.types.security_controls_provider.deserialize_json(
                data["Provider"]
            )
        )
    return out
