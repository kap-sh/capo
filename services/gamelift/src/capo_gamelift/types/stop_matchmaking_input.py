"""Generated from Smithy shape ``com.amazonaws.gamelift#StopMatchmakingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_id_string_model


class StopMatchmakingInput(TypedDict, closed=True):
    ticket_id: NotRequired[
        "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
    ]
    """<p>A unique identifier for a matchmaking ticket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMatchmakingInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMatchmakingInput:
    out: StopMatchmakingInput = {}  # type: ignore[typeddict-item]
    if data.get("TicketId") is not None:
        out["ticket_id"] = data["TicketId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopMatchmakingInput) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    return out


def deserialize_cbor(data: dict) -> StopMatchmakingInput:
    out: StopMatchmakingInput = {}  # type: ignore[typeddict-item]
    if data.get("TicketId") is not None:
        out["ticket_id"] = data["TicketId"]
    return out
