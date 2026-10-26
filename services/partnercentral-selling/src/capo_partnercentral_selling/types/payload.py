"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Payload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError
from capo_partnercentral_selling.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_invitation_payload
    import capo_partnercentral_selling.types.opportunity_invitation_payload


class _Payload_OpportunityInvitation(TypedDict, closed=True):
    OpportunityInvitation: "capo_partnercentral_selling.types.opportunity_invitation_payload.OpportunityInvitationPayload"


class _Payload_LeadInvitation(TypedDict, closed=True):
    LeadInvitation: "capo_partnercentral_selling.types.lead_invitation_payload.LeadInvitationPayload"


Payload: TypeAlias = (
    _Payload_OpportunityInvitation | _Payload_LeadInvitation | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Payload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Payload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "OpportunityInvitation" in value:
        import capo_partnercentral_selling.types.opportunity_invitation_payload

        return {
            "OpportunityInvitation": capo_partnercentral_selling.types.opportunity_invitation_payload.serialize_aws_json_1_0(
                value["OpportunityInvitation"]
            )
        }
    elif "LeadInvitation" in value:
        import capo_partnercentral_selling.types.lead_invitation_payload

        return {
            "LeadInvitation": capo_partnercentral_selling.types.lead_invitation_payload.serialize_aws_json_1_0(
                value["LeadInvitation"]
            )
        }
    else:
        raise SerializationError("Payload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Payload:
    if data.get("OpportunityInvitation") is not None:
        import capo_partnercentral_selling.types.opportunity_invitation_payload

        return {
            "OpportunityInvitation": capo_partnercentral_selling.types.opportunity_invitation_payload.deserialize_aws_json_1_0(
                data["OpportunityInvitation"]
            )
        }
    elif data.get("LeadInvitation") is not None:
        import capo_partnercentral_selling.types.lead_invitation_payload

        return {
            "LeadInvitation": capo_partnercentral_selling.types.lead_invitation_payload.deserialize_aws_json_1_0(
                data["LeadInvitation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Payload: no recognized variant key")


def redact_sensitive(value: Payload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "OpportunityInvitation" in value:
        import capo_partnercentral_selling.types.opportunity_invitation_payload

        out["OpportunityInvitation"] = (
            capo_partnercentral_selling.types.opportunity_invitation_payload.redact_sensitive(
                value["OpportunityInvitation"]
            )
        )
    if "LeadInvitation" in value:
        import capo_partnercentral_selling.types.lead_invitation_payload

        out["LeadInvitation"] = (
            capo_partnercentral_selling.types.lead_invitation_payload.redact_sensitive(
                value["LeadInvitation"]
            )
        )
    return out
