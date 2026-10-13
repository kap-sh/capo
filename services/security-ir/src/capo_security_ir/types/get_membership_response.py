"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.aws_account_id
    import capo_security_ir.types.aws_region
    import capo_security_ir.types.customer_type
    import capo_security_ir.types.incident_response_team
    import capo_security_ir.types.membership_accounts_configurations
    import capo_security_ir.types.membership_arn
    import capo_security_ir.types.membership_id
    import capo_security_ir.types.membership_name
    import capo_security_ir.types.membership_status
    import capo_security_ir.types.opt_in_features


class GetMembershipResponse(TypedDict, closed=True):
    membership_id: "capo_security_ir.types.membership_id.MembershipId"
    """<p>Response element for GetMembership that provides the queried membership ID.</p>"""
    account_id: NotRequired["capo_security_ir.types.aws_account_id.AWSAccountId"]
    """<p>Response element for GetMembership that provides the account configured to manage the membership.</p>"""
    region: NotRequired["capo_security_ir.types.aws_region.AwsRegion"]
    """<p>Response element for GetMembership that provides the region configured to manage the membership.</p>"""
    membership_name: NotRequired[
        "capo_security_ir.types.membership_name.MembershipName"
    ]
    """<p>Response element for GetMembership that provides the configured membership name.</p>"""
    membership_arn: NotRequired["capo_security_ir.types.membership_arn.MembershipArn"]
    """<p>Response element for GetMembership that provides the membership ARN.</p>"""
    membership_status: NotRequired[
        "capo_security_ir.types.membership_status.MembershipStatus"
    ]
    """<p>Response element for GetMembership that provides the current membership status.</p>"""
    membership_activation_timestamp: NotRequired["datetime.datetime"]
    """<p>Response element for GetMembership that provides the configured membership activation timestamp.</p>"""
    membership_deactivation_timestamp: NotRequired["datetime.datetime"]
    """<p>Response element for GetMembership that provides the configured membership name deactivation timestamp. </p>"""
    customer_type: NotRequired["capo_security_ir.types.customer_type.CustomerType"]
    """<p>Response element for GetMembership that provides the configured membership type. Options include <code> Standalone | Organizations</code>. </p>"""
    number_of_accounts_covered: NotRequired["int"]
    """<p>Response element for GetMembership that provides the number of accounts in the membership.</p>"""
    incident_response_team: NotRequired[
        "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
    ]
    """<p>Response element for GetMembership that provides the configured membership incident response team members. </p>"""
    opt_in_features: NotRequired["capo_security_ir.types.opt_in_features.OptInFeatures"]
    """<p>Response element for GetMembership that provides the if opt-in features have been enabled.</p>"""
    membership_accounts_configurations: NotRequired[
        "capo_security_ir.types.membership_accounts_configurations.MembershipAccountsConfigurations"
    ]
    """<p>The <code>membershipAccountsConfigurations</code> field contains the configuration details for member accounts within the Amazon Web Services Organizations membership structure. </p> <p>This field returns a structure containing information about:</p> <ul> <li> <p>Account configurations for member accounts</p> </li> <li> <p>Membership settings and preferences</p> </li> <li> <p>Account-level permissions and roles</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipResponse) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        import capo_security_ir.types.aws_region

        out["region"] = capo_security_ir.types.aws_region.serialize_json(
            value["region"]
        )
    if "membership_name" in value:
        out["membershipName"] = value["membership_name"]
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    if "membership_status" in value:
        import capo_security_ir.types.membership_status

        out["membershipStatus"] = (
            capo_security_ir.types.membership_status.serialize_json(
                value["membership_status"]
            )
        )
    if "membership_activation_timestamp" in value:
        import capo_security_ir.types._prelude.timestamp

        out["membershipActivationTimestamp"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["membership_activation_timestamp"]
            )
        )
    if "membership_deactivation_timestamp" in value:
        import capo_security_ir.types._prelude.timestamp

        out["membershipDeactivationTimestamp"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["membership_deactivation_timestamp"]
            )
        )
    if "customer_type" in value:
        import capo_security_ir.types.customer_type

        out["customerType"] = capo_security_ir.types.customer_type.serialize_json(
            value["customer_type"]
        )
    if "number_of_accounts_covered" in value:
        out["numberOfAccountsCovered"] = value["number_of_accounts_covered"]
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
    if "membership_accounts_configurations" in value:
        import capo_security_ir.types.membership_accounts_configurations

        out["membershipAccountsConfigurations"] = (
            capo_security_ir.types.membership_accounts_configurations.serialize_json(
                value["membership_accounts_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMembershipResponse:
    out: GetMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("GetMembershipResponse.membership_id required")
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        import capo_security_ir.types.aws_region

        out["region"] = capo_security_ir.types.aws_region.deserialize_json(
            data["region"]
        )
    if data.get("membershipName") is not None:
        out["membership_name"] = data["membershipName"]
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    if data.get("membershipStatus") is not None:
        import capo_security_ir.types.membership_status

        out["membership_status"] = (
            capo_security_ir.types.membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    if data.get("membershipActivationTimestamp") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["membership_activation_timestamp"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["membershipActivationTimestamp"]
            )
        )
    if data.get("membershipDeactivationTimestamp") is not None:
        import capo_security_ir.types._prelude.timestamp

        out["membership_deactivation_timestamp"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["membershipDeactivationTimestamp"]
            )
        )
    if data.get("customerType") is not None:
        import capo_security_ir.types.customer_type

        out["customer_type"] = capo_security_ir.types.customer_type.deserialize_json(
            data["customerType"]
        )
    if data.get("numberOfAccountsCovered") is not None:
        out["number_of_accounts_covered"] = data["numberOfAccountsCovered"]
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
    if data.get("membershipAccountsConfigurations") is not None:
        import capo_security_ir.types.membership_accounts_configurations

        out["membership_accounts_configurations"] = (
            capo_security_ir.types.membership_accounts_configurations.deserialize_json(
                data["membershipAccountsConfigurations"]
            )
        )
    return out


def redact_sensitive(value: GetMembershipResponse) -> dict[str, Any]:
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
