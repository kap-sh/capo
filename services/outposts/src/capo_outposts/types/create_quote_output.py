"""Generated from Smithy shape ``com.amazonaws.outposts#CreateQuoteOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.quote


class CreateQuoteOutput(TypedDict, closed=True):
    quote: NotRequired["capo_outposts.types.quote.Quote"]
    """<p>Information about the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuoteOutput) -> dict:
    out: dict = {}
    if "quote" in value:
        import capo_outposts.types.quote

        out["Quote"] = capo_outposts.types.quote.serialize_json(value["quote"])
    return out


def deserialize_json(data: dict) -> CreateQuoteOutput:
    out: CreateQuoteOutput = {}  # type: ignore[typeddict-item]
    if data.get("Quote") is not None:
        import capo_outposts.types.quote

        out["quote"] = capo_outposts.types.quote.deserialize_json(data["Quote"])
    return out


def redact_sensitive(value: CreateQuoteOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quote" in value:
        import capo_outposts.types.quote

        out["quote"] = capo_outposts.types.quote.redact_sensitive(value["quote"])
    return out
