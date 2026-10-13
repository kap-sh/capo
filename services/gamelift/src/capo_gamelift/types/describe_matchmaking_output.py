"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_ticket_list


class DescribeMatchmakingOutput(TypedDict, closed=True):
    ticket_list: NotRequired[
        "capo_gamelift.types.matchmaking_ticket_list.MatchmakingTicketList"
    ]
    """<p>A collection of existing matchmaking ticket objects matching the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingOutput) -> dict:
    out: dict = {}
    if "ticket_list" in value:
        import capo_gamelift.types.matchmaking_ticket_list

        out["TicketList"] = (
            capo_gamelift.types.matchmaking_ticket_list.serialize_aws_json_1_1(
                value["ticket_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingOutput:
    out: DescribeMatchmakingOutput = {}  # type: ignore[typeddict-item]
    if data.get("TicketList") is not None:
        import capo_gamelift.types.matchmaking_ticket_list

        out["ticket_list"] = (
            capo_gamelift.types.matchmaking_ticket_list.deserialize_aws_json_1_1(
                data["TicketList"]
            )
        )
    return out


def redact_sensitive(value: DescribeMatchmakingOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ticket_list" in value:
        import capo_gamelift.types.matchmaking_ticket_list

        out["ticket_list"] = (
            capo_gamelift.types.matchmaking_ticket_list.redact_sensitive(
                value["ticket_list"]
            )
        )
    return out
