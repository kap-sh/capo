"""Generated from Smithy shape ``com.amazonaws.securityir#CreateMembershipRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.incident_response_team
    import capo_security_ir.types.membership_name
    import capo_security_ir.types.opt_in_features
    import capo_security_ir.types.tag_map


class CreateMembershipRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""
    membership_name: "capo_security_ir.types.membership_name.MembershipName"
    """<p>Required element used in combination with CreateMembership to create a name for the membership.</p>"""
    incident_response_team: (
        "capo_security_ir.types.incident_response_team.IncidentResponseTeam"
    )
    """<p>Required element used in combination with CreateMembership to add customer incident response team members and trusted partners to the membership. </p>"""
    opt_in_features: NotRequired["capo_security_ir.types.opt_in_features.OptInFeatures"]
    """<p>Optional element to enable the monitoring and investigation opt-in features for the service.</p>"""
    tags: NotRequired["capo_security_ir.types.tag_map.TagMap"]
    """<p>Optional element for customer configured tags.</p>"""
    cover_entire_organization: "bool"
    """<p>The <code>coverEntireOrganization</code> parameter is a boolean flag that determines whether the membership should be applied to the entire Amazon Web Services Organization. When set to true, the membership will be created for all accounts within the organization. When set to false, the membership will only be created for specified accounts. </p> <p>This parameter is optional. If not specified, the default value is false.</p> <ul> <li> <p>If set to <i>true</i>: The membership will automatically include all existing and future accounts in the Amazon Web Services Organization. </p> </li> <li> <p>If set to <i>false</i>: The membership will only apply to explicitly specified accounts. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["membershipName"] = value["membership_name"]
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
    if "tags" in value:
        import capo_security_ir.types.tag_map

        out["tags"] = capo_security_ir.types.tag_map.serialize_json(value["tags"])
    out["coverEntireOrganization"] = value.get("cover_entire_organization", True)
    return out


def deserialize_json(data: dict) -> CreateMembershipRequest:
    out: CreateMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("membershipName") is not None:
        out["membership_name"] = data["membershipName"]
    else:
        raise DeserializationError("CreateMembershipRequest.membership_name required")
    if data.get("incidentResponseTeam") is not None:
        import capo_security_ir.types.incident_response_team

        out["incident_response_team"] = (
            capo_security_ir.types.incident_response_team.deserialize_json(
                data["incidentResponseTeam"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMembershipRequest.incident_response_team required"
        )
    if data.get("optInFeatures") is not None:
        import capo_security_ir.types.opt_in_features

        out["opt_in_features"] = (
            capo_security_ir.types.opt_in_features.deserialize_json(
                data["optInFeatures"]
            )
        )
    if data.get("tags") is not None:
        import capo_security_ir.types.tag_map

        out["tags"] = capo_security_ir.types.tag_map.deserialize_json(data["tags"])
    if data.get("coverEntireOrganization") is not None:
        out["cover_entire_organization"] = data["coverEntireOrganization"]
    else:
        out["cover_entire_organization"] = True
    return out


def redact_sensitive(value: CreateMembershipRequest) -> dict[str, Any]:
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
