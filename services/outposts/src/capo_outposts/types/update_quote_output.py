"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateQuoteOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.quote


class UpdateQuoteOutput(TypedDict, closed=True):
    quote: NotRequired["capo_outposts.types.quote.Quote"]
    """<p>Information about the updated quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuoteOutput) -> dict:
    out: dict = {}
    if "quote" in value:
        import capo_outposts.types.quote

        out["Quote"] = capo_outposts.types.quote.serialize_json(value["quote"])
    return out


def deserialize_json(data: dict) -> UpdateQuoteOutput:
    out: UpdateQuoteOutput = {}  # type: ignore[typeddict-item]
    if data.get("Quote") is not None:
        import capo_outposts.types.quote

        out["quote"] = capo_outposts.types.quote.deserialize_json(data["Quote"])
    return out


def redact_sensitive(value: UpdateQuoteOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quote" in value:
        import capo_outposts.types.quote

        out["quote"] = capo_outposts.types.quote.redact_sensitive(value["quote"])
    return out
