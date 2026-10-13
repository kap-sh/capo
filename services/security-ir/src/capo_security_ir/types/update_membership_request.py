"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateMembershipRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.incident_response_team
    import capo_security_ir.types.membership_accounts_configurations_update
    import capo_security_ir.types.membership_id
    import capo_security_ir.types.membership_name
    import capo_security_ir.types.opt_in_features


class UpdateMembershipRequest(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """<p>Required element for UpdateMembership to identify the membership to update.</p>"""
    membership_name: NotRequired[
        "capo_security_ir.types.membership_name.MembershipName"
    ]
    """<p>Optional element for UpdateMembership to update the membership name.</p>"""
    incident_response_team: NotRequired[
        "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
    ]
    """<p>Optional element for UpdateMembership to update the membership name.</p>"""
    opt_in_features: NotRequired["capo_security_ir.types.opt_in_features.OptInFeatures"]
    """<p>Optional element for UpdateMembership to enable or disable opt-in features for the service.</p>"""
    membership_accounts_configurations_update: NotRequired[
        "capo_security_ir.types.membership_accounts_configurations_update.MembershipAccountsConfigurationsUpdate"
    ]
    """<p>The <code>membershipAccountsConfigurationsUpdate</code> field in the <code>UpdateMembershipRequest</code> structure allows you to update the configuration settings for accounts within a membership. </p> <p>This field is optional and contains a structure of type <code>MembershipAccountsConfigurationsUpdate </code> that specifies the updated account configurations for the membership. </p>"""
    undo_membership_cancellation: NotRequired["bool"]
    """<p>The <code>undoMembershipCancellation</code> parameter is a boolean flag that indicates whether to reverse a previously requested membership cancellation. When set to true, this will revoke the cancellation request and maintain the membership status. </p> <p>This parameter is optional and can be used in scenarios where you need to restore a membership that was marked for cancellation but hasn't been fully terminated yet. </p> <ul> <li> <p>If set to <code>true</code>, the cancellation request will be revoked </p> </li> <li> <p>If set to <code>false</code> the service will throw a ValidationException. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMembershipRequest) -> dict:
    out: dict = {}
    if "membership_name" in value:
        out["membershipName"] = value["membership_name"]
    if "incident_response_team" in value:
        import capo_security_ir.types.incident_response_team

        out["incidentResponseTeam"] = (
            capo_security_ir.types.incident_response_team.serialize_json(
                value["incident_response_team"]
            )
        )
    if "opt_in_features" in value:
        import capo_security_ir.types.opt_in_features

        out["optInFeatures"] = capo_security_ir.types.opt_in_features.serialize_json(
            value["opt_in_features"]
        )
    if "membership_accounts_configurations_update" in value:
        import capo_security_ir.types.membership_accounts_configurations_update

        out["membershipAccountsConfigurationsUpdate"] = (
            capo_security_ir.types.membership_accounts_configurations_update.serialize_json(
                value["membership_accounts_configurations_update"]
            )
        )
    if "undo_membership_cancellation" in value:
        out["undoMembershipCancellation"] = value["undo_membership_cancellation"]
    return out


def deserialize_json(data: dict) -> UpdateMembershipRequest:
    out: UpdateMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("membershipName") is not None:
        out["membership_name"] = data["membershipName"]
    if data.get("incidentResponseTeam") is not None:
        import capo_security_ir.types.incident_response_team

        out["incident_response_team"] = (
            capo_security_ir.types.incident_response_team.deserialize_json(
                data["incidentResponseTeam"]
            )
        )
    if data.get("optInFeatures") is not None:
        import capo_security_ir.types.opt_in_features

        out["opt_in_features"] = (
            capo_security_ir.types.opt_in_features.deserialize_json(
                data["optInFeatures"]
            )
        )
    if data.get("membershipAccountsConfigurationsUpdate") is not None:
        import capo_security_ir.types.membership_accounts_configurations_update

        out["membership_accounts_configurations_update"] = (
            capo_security_ir.types.membership_accounts_configurations_update.deserialize_json(
                data["membershipAccountsConfigurationsUpdate"]
            )
        )
    if data.get("undoMembershipCancellation") is not None:
        out["undo_membership_cancellation"] = data["undoMembershipCancellation"]
    return out


def redact_sensitive(value: UpdateMembershipRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "membership_name" in value:
        out["membership_name"] = "*** Sensitive Data Redacted ***"
    if "incident_response_team" in value:
        import capo_security_ir.types.incident_response_team

        out["incident_response_team"] = (
            capo_security_ir.types.incident_response_team.redact_sensitive(
                value["incident_response_team"]
            )
        )
    return out
