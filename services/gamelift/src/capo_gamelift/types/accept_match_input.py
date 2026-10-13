"""Generated from Smithy shape ``com.amazonaws.gamelift#AcceptMatchInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.acceptance_type
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.player_ids_for_accept_match


class AcceptMatchInput(TypedDict, closed=True):
    ticket_id: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket. The ticket must be in status <code>REQUIRES_ACCEPTANCE</code>; otherwise this request will fail.</p>"""
    player_ids: NotRequired[
        "capo_gamelift.types.player_ids_for_accept_match.PlayerIdsForAcceptMatch"
    ]
    """<p>A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.</p>"""
    acceptance_type: NotRequired["capo_gamelift.types.acceptance_type.AcceptanceType"]
    """<p>Player response to the proposed match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptMatchInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "player_ids" in value:
        import capo_gamelift.types.player_ids_for_accept_match

        out["PlayerIds"] = (
            capo_gamelift.types.player_ids_for_accept_match.serialize_aws_json_1_1(
                value["player_ids"]
            )
        )
    if "acceptance_type" in value:
        import capo_gamelift.types.acceptance_type

        out["AcceptanceType"] = (
            capo_gamelift.types.acceptance_type.serialize_aws_json_1_1(
                value["acceptance_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptMatchInput:
    out: AcceptMatchInput = {}  # type: ignore[typeddict-item]
    if data.get("TicketId") is not None:
        out["ticket_id"] = data["TicketId"]
    if data.get("PlayerIds") is not None:
        import capo_gamelift.types.player_ids_for_accept_match

        out["player_ids"] = (
            capo_gamelift.types.player_ids_for_accept_match.deserialize_aws_json_1_1(
                data["PlayerIds"]
            )
        )
    if data.get("AcceptanceType") is not None:
        import capo_gamelift.types.acceptance_type

        out["acceptance_type"] = (
            capo_gamelift.types.acceptance_type.deserialize_aws_json_1_1(
                data["AcceptanceType"]
            )
        )
    return out


def redact_sensitive(value: AcceptMatchInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "player_ids" in value:
        out["player_ids"] = "*** Sensitive Data Redacted ***"
    return out
