"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSummaryListDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.quote_summary

QuoteSummaryListDefinition: TypeAlias = list[
    "capo_outposts.types.quote_summary.QuoteSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSummaryListDefinition) -> list:
    import capo_outposts.types.quote_summary

    out: list = []
    for item in value:
        out.append(capo_outposts.types.quote_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteSummaryListDefinition:
    import capo_outposts.types.quote_summary

    out: QuoteSummaryListDefinition = []
    for item in data:
        if item is None:
            continue
        out.append(capo_outposts.types.quote_summary.deserialize_json(item))
    return out


def redact_sensitive(value: QuoteSummaryListDefinition) -> list[Any]:
    import capo_outposts.types.quote_summary

    return [capo_outposts.types.quote_summary.redact_sensitive(item) for item in value]
