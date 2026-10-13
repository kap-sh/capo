"""Generated from Smithy shape ``com.amazonaws.gamelift#StartMatchBackfillOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_ticket


class StartMatchBackfillOutput(TypedDict, closed=True):
    matchmaking_ticket: NotRequired[
        "capo_gamelift.types.matchmaking_ticket.MatchmakingTicket"
    ]
    """<p>Ticket representing the backfill matchmaking request. This object includes the information in the request, ticket status, and match results as generated during the matchmaking process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMatchBackfillOutput) -> dict:
    out: dict = {}
    if "matchmaking_ticket" in value:
        import capo_gamelift.types.matchmaking_ticket

        out["MatchmakingTicket"] = (
            capo_gamelift.types.matchmaking_ticket.serialize_aws_json_1_1(
                value["matchmaking_ticket"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMatchBackfillOutput:
    out: StartMatchBackfillOutput = {}  # type: ignore[typeddict-item]
    if data.get("MatchmakingTicket") is not None:
        import capo_gamelift.types.matchmaking_ticket

        out["matchmaking_ticket"] = (
            capo_gamelift.types.matchmaking_ticket.deserialize_aws_json_1_1(
                data["MatchmakingTicket"]
            )
        )
    return out


def redact_sensitive(value: StartMatchBackfillOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "matchmaking_ticket" in value:
        import capo_gamelift.types.matchmaking_ticket

        out["matchmaking_ticket"] = (
            capo_gamelift.types.matchmaking_ticket.redact_sensitive(
                value["matchmaking_ticket"]
            )
        )
    return out
