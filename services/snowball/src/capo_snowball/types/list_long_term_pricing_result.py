"""Generated from Smithy shape ``com.amazonaws.snowball#ListLongTermPricingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.long_term_pricing_entry_list
    import capo_snowball.types.string


class ListLongTermPricingResult(TypedDict, closed=True):
    long_term_pricing_entries: NotRequired[
        "capo_snowball.types.long_term_pricing_entry_list.LongTermPricingEntryList"
    ]
    """<p>Each <code>LongTermPricingEntry</code> object contains a status, ID, and other information about the <code>LongTermPricing</code> type. </p>"""
    next_token: NotRequired["capo_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for your next list of returned <code>ListLongTermPricing</code> list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLongTermPricingResult) -> dict:
    out: dict = {}
    if "long_term_pricing_entries" in value:
        import capo_snowball.types.long_term_pricing_entry_list

        out["LongTermPricingEntries"] = (
            capo_snowball.types.long_term_pricing_entry_list.serialize_aws_json_1_1(
                value["long_term_pricing_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLongTermPricingResult:
    out: ListLongTermPricingResult = {}  # type: ignore[typeddict-item]
    if data.get("LongTermPricingEntries") is not None:
        import capo_snowball.types.long_term_pricing_entry_list

        out["long_term_pricing_entries"] = (
            capo_snowball.types.long_term_pricing_entry_list.deserialize_aws_json_1_1(
                data["LongTermPricingEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLongTermPricingResult) -> dict:
    out: dict = {}
    if "long_term_pricing_entries" in value:
        import capo_snowball.types.long_term_pricing_entry_list

        out["LongTermPricingEntries"] = (
            capo_snowball.types.long_term_pricing_entry_list.serialize_cbor(
                value["long_term_pricing_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListLongTermPricingResult:
    out: ListLongTermPricingResult = {}  # type: ignore[typeddict-item]
    if data.get("LongTermPricingEntries") is not None:
        import capo_snowball.types.long_term_pricing_entry_list

        out["long_term_pricing_entries"] = (
            capo_snowball.types.long_term_pricing_entry_list.deserialize_cbor(
                data["LongTermPricingEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
