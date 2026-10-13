"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInteractionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_interaction

LeadInteractionList: TypeAlias = list[
    "capo_partnercentral_selling.types.lead_interaction.LeadInteraction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInteractionList) -> list:
    import capo_partnercentral_selling.types.lead_interaction

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.lead_interaction.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LeadInteractionList:
    import capo_partnercentral_selling.types.lead_interaction

    out: LeadInteractionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.lead_interaction.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: LeadInteractionList) -> list[Any]:
    import capo_partnercentral_selling.types.lead_interaction

    return [
        capo_partnercentral_selling.types.lead_interaction.redact_sensitive(item)
        for item in value
    ]
