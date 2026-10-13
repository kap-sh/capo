"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityTeamMembersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_team_member

AwsOpportunityTeamMembersList: TypeAlias = list[
    "capo_partnercentral_selling.types.aws_team_member.AwsTeamMember"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityTeamMembersList) -> list:
    import capo_partnercentral_selling.types.aws_team_member

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.aws_team_member.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AwsOpportunityTeamMembersList:
    import capo_partnercentral_selling.types.aws_team_member

    out: AwsOpportunityTeamMembersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_selling.types.aws_team_member.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: AwsOpportunityTeamMembersList) -> list[Any]:
    import capo_partnercentral_selling.types.aws_team_member

    return [
        capo_partnercentral_selling.types.aws_team_member.redact_sensitive(item)
        for item in value
    ]
