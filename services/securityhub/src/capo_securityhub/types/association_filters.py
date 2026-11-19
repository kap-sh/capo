"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.association_type
    import capo_securityhub.types.configuration_policy_association_status
    import capo_securityhub.types.non_empty_string


class AssociationFilters(TypedDict, closed=True):
    configuration_policy_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ARN or UUID of the configuration policy. </p>"""
    association_type: NotRequired[
        "capo_securityhub.types.association_type.AssociationType"
    ]
    """<p> Indicates whether the association between a target and a configuration was directly applied by the Security Hub CSPM delegated administrator or inherited from a parent. </p>"""
    association_status: NotRequired[
        "capo_securityhub.types.configuration_policy_association_status.ConfigurationPolicyAssociationStatus"
    ]
    """<p> The current status of the association between a target and a configuration policy. Possible values are <code>PENDING</code>, <code>SUCCESS</code>, <code>FAILED</code>, and <code>DISABLED</code>. The value is <code>DISABLED</code> when central configuration is disabled because the organization is managed by Security Hub CSPM policies in Organizations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociationFilters) -> dict:
    out: dict = {}
    if "configuration_policy_id" in value:
        out["ConfigurationPolicyId"] = value["configuration_policy_id"]
    if "association_type" in value:
        import capo_securityhub.types.association_type

        out["AssociationType"] = capo_securityhub.types.association_type.serialize_json(
            value["association_type"]
        )
    if "association_status" in value:
        import capo_securityhub.types.configuration_policy_association_status

        out["AssociationStatus"] = (
            capo_securityhub.types.configuration_policy_association_status.serialize_json(
                value["association_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociationFilters:
    out: AssociationFilters = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationPolicyId") is not None:
        out["configuration_policy_id"] = data["ConfigurationPolicyId"]
    if data.get("AssociationType") is not None:
        import capo_securityhub.types.association_type

        out["association_type"] = (
            capo_securityhub.types.association_type.deserialize_json(
                data["AssociationType"]
            )
        )
    if data.get("AssociationStatus") is not None:
        import capo_securityhub.types.configuration_policy_association_status

        out["association_status"] = (
            capo_securityhub.types.configuration_policy_association_status.deserialize_json(
                data["AssociationStatus"]
            )
        )
    return out
