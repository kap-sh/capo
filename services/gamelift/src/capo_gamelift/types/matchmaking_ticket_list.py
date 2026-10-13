"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingTicketList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_ticket

MatchmakingTicketList: TypeAlias = list[
    "capo_gamelift.types.matchmaking_ticket.MatchmakingTicket"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchmakingTicketList) -> list:
    import capo_gamelift.types.matchmaking_ticket

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.matchmaking_ticket.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MatchmakingTicketList:
    import capo_gamelift.types.matchmaking_ticket

    out: MatchmakingTicketList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.matchmaking_ticket.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MatchmakingTicketList) -> list[Any]:
    import capo_gamelift.types.matchmaking_ticket

    return [
        capo_gamelift.types.matchmaking_ticket.redact_sensitive(item) for item in value
    ]
