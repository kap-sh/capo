"""Generated from Smithy shape ``com.amazonaws.outposts#ListQuotesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.quote_summary_list_definition
    import capo_outposts.types.token


class ListQuotesOutput(TypedDict, closed=True):
    quotes: NotRequired[
        "capo_outposts.types.quote_summary_list_definition.QuoteSummaryListDefinition"
    ]
    """<p>Information about the quotes.</p>"""
    next_token: NotRequired["capo_outposts.types.token.Token"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuotesOutput) -> dict:
    out: dict = {}
    if "quotes" in value:
        import capo_outposts.types.quote_summary_list_definition

        out["Quotes"] = (
            capo_outposts.types.quote_summary_list_definition.serialize_json(
                value["quotes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuotesOutput:
    out: ListQuotesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Quotes") is not None:
        import capo_outposts.types.quote_summary_list_definition

        out["quotes"] = (
            capo_outposts.types.quote_summary_list_definition.deserialize_json(
                data["Quotes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListQuotesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quotes" in value:
        import capo_outposts.types.quote_summary_list_definition

        out["quotes"] = (
            capo_outposts.types.quote_summary_list_definition.redact_sensitive(
                value["quotes"]
            )
        )
    return out
