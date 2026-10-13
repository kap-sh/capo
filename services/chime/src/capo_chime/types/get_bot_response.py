"""Generated from Smithy shape ``com.amazonaws.chime#GetBotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.bot


class GetBotResponse(TypedDict, closed=True):
    bot: NotRequired["capo_chime.types.bot.Bot"]
    """<p>The chat bot details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotResponse) -> dict:
    out: dict = {}
    if "bot" in value:
        import capo_chime.types.bot

        out["Bot"] = capo_chime.types.bot.serialize_json(value["bot"])
    return out


def deserialize_json(data: dict) -> GetBotResponse:
    out: GetBotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Bot") is not None:
        import capo_chime.types.bot

        out["bot"] = capo_chime.types.bot.deserialize_json(data["Bot"])
    return out


def redact_sensitive(value: GetBotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bot" in value:
        import capo_chime.types.bot

        out["bot"] = capo_chime.types.bot.redact_sensitive(value["bot"])
    return out
