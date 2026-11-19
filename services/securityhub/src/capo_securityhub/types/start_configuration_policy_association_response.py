"""Generated from Smithy shape ``com.amazonaws.securityhub#StartConfigurationPolicyAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.association_type
    import capo_securityhub.types.configuration_policy_association_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.target_type
    import capo_securityhub.types.timestamp


class StartConfigurationPolicyAssociationResponse(TypedDict, closed=True):
    configuration_policy_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The UUID of the configuration policy. </p>"""
    target_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of the target account, organizational unit, or the organization root with which the configuration is associated. </p>"""
    target_type: NotRequired["capo_securityhub.types.target_type.TargetType"]
    """<p> Indicates whether the target is an Amazon Web Services account, organizational unit, or the organization root. </p>"""
    association_type: NotRequired[
        "capo_securityhub.types.association_type.AssociationType"
    ]
    """<p> Indicates whether the association between the specified target and the configuration was directly applied by the Security Hub CSPM delegated administrator or inherited from a parent. </p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy association was last updated. </p>"""
    association_status: NotRequired[
        "capo_securityhub.types.configuration_policy_association_status.ConfigurationPolicyAssociationStatus"
    ]
    """<p> The current status of the association between the specified target and the configuration. Possible values are: </p> <ul> <li> <p> <code>PENDING</code> - The association is in progress.</p> </li> <li> <p> <code>SUCCESS</code> - The association succeeded.</p> </li> <li> <p> <code>FAILED</code> - The association failed. For details, see <code>AssociationStatusMessage</code>.</p> </li> <li> <p> <code>DISABLED</code> - Central configuration is disabled because the organization is managed by Security Hub CSPM policies in Organizations.</p> </li> </ul>"""
    association_status_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> An explanation for a <code>FAILED</code> value for <code>AssociationStatus</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationPolicyAssociationResponse) -> dict:
    out: dict = {}
    if "configuration_policy_id" in value:
        out["ConfigurationPolicyId"] = value["configuration_policy_id"]
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "target_type" in value:
        import capo_securityhub.types.target_type

        out["TargetType"] = capo_securityhub.types.target_type.serialize_json(
            value["target_type"]
        )
    if "association_type" in value:
        import capo_securityhub.types.association_type

        out["AssociationType"] = capo_securityhub.types.association_type.serialize_json(
            value["association_type"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "association_status" in value:
        import capo_securityhub.types.configuration_policy_association_status

        out["AssociationStatus"] = (
            capo_securityhub.types.configuration_policy_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "association_status_message" in value:
        out["AssociationStatusMessage"] = value["association_status_message"]
    return out


def deserialize_json(data: dict) -> StartConfigurationPolicyAssociationResponse:
    out: StartConfigurationPolicyAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationPolicyId") is not None:
        out["configuration_policy_id"] = data["ConfigurationPolicyId"]
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    if data.get("TargetType") is not None:
        import capo_securityhub.types.target_type

        out["target_type"] = capo_securityhub.types.target_type.deserialize_json(
            data["TargetType"]
        )
    if data.get("AssociationType") is not None:
        import capo_securityhub.types.association_type

        out["association_type"] = (
            capo_securityhub.types.association_type.deserialize_json(
                data["AssociationType"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("AssociationStatus") is not None:
        import capo_securityhub.types.configuration_policy_association_status

        out["association_status"] = (
            capo_securityhub.types.configuration_policy_association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    if data.get("AssociationStatusMessage") is not None:
        out["association_status_message"] = data["AssociationStatusMessage"]
    return out
