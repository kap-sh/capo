"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.alpha_numeric_non_empty_string
    import capo_securityhub.types.control_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.parameters
    import capo_securityhub.types.security_controls_provider
    import capo_securityhub.types.severity_rating
    import capo_securityhub.types.update_status


class SecurityControl(TypedDict, closed=True):
    security_control_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number, such as APIGateway.3. </p>"""
    security_control_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) for a security control across standards, such as <code>arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1</code>. This parameter doesn't mention a specific standard. </p>"""
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The title of a security control. </p>"""
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
    security_control_status: NotRequired[
        "capo_securityhub.types.control_status.ControlStatus"
    ]
    """<p> The enablement status of a security control in a specific standard. </p>"""
    update_status: NotRequired["capo_securityhub.types.update_status.UpdateStatus"]
    """<p> Identifies whether customizable properties of a security control are reflected in Security Hub CSPM findings. A status of <code>READY</code> indicates that Security Hub CSPM uses the current control parameter values when running security checks of the control. A status of <code>UPDATING</code> indicates that all security checks might not use the current parameter values. </p>"""
    parameters: NotRequired["capo_securityhub.types.parameters.Parameters"]
    """<p> An object that identifies the name of a control parameter, its current value, and whether it has been customized. </p>"""
    last_update_reason: NotRequired[
        "capo_securityhub.types.alpha_numeric_non_empty_string.AlphaNumericNonEmptyString"
    ]
    """<p> The most recent reason for updating the customizable properties of a security control. This differs from the <code>UpdateReason</code> field of the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html"> <code>BatchUpdateStandardsControlAssociations</code> </a> API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores. </p>"""
    provider: NotRequired[
        "capo_securityhub.types.security_controls_provider.SecurityControlsProvider"
    ]
    """<p>The cloud provider whose resources the security control evaluates. For example, <code>AWS</code> or <code>Azure</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControl) -> dict:
    out: dict = {}
    if "security_control_id" in value:
        out["SecurityControlId"] = value["security_control_id"]
    if "security_control_arn" in value:
        out["SecurityControlArn"] = value["security_control_arn"]
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
    if "security_control_status" in value:
        import capo_securityhub.types.control_status

        out["SecurityControlStatus"] = (
            capo_securityhub.types.control_status.serialize_json(
                value["security_control_status"]
            )
        )
    if "update_status" in value:
        import capo_securityhub.types.update_status

        out["UpdateStatus"] = capo_securityhub.types.update_status.serialize_json(
            value["update_status"]
        )
    if "parameters" in value:
        import capo_securityhub.types.parameters

        out["Parameters"] = capo_securityhub.types.parameters.serialize_json(
            value["parameters"]
        )
    if "last_update_reason" in value:
        out["LastUpdateReason"] = value["last_update_reason"]
    if "provider" in value:
        import capo_securityhub.types.security_controls_provider

        out["Provider"] = (
            capo_securityhub.types.security_controls_provider.serialize_json(
                value["provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityControl:
    out: SecurityControl = {}  # type: ignore[typeddict-item]
    if data.get("SecurityControlId") is not None:
        out["security_control_id"] = data["SecurityControlId"]
    if data.get("SecurityControlArn") is not None:
        out["security_control_arn"] = data["SecurityControlArn"]
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
    if data.get("SecurityControlStatus") is not None:
        import capo_securityhub.types.control_status

        out["security_control_status"] = (
            capo_securityhub.types.control_status.deserialize_json(
                data["SecurityControlStatus"]
            )
        )
    if data.get("UpdateStatus") is not None:
        import capo_securityhub.types.update_status

        out["update_status"] = capo_securityhub.types.update_status.deserialize_json(
            data["UpdateStatus"]
        )
    if data.get("Parameters") is not None:
        import capo_securityhub.types.parameters

        out["parameters"] = capo_securityhub.types.parameters.deserialize_json(
            data["Parameters"]
        )
    if data.get("LastUpdateReason") is not None:
        out["last_update_reason"] = data["LastUpdateReason"]
    if data.get("Provider") is not None:
        import capo_securityhub.types.security_controls_provider

        out["provider"] = (
            capo_securityhub.types.security_controls_provider.deserialize_json(
                data["Provider"]
            )
        )
    return out
