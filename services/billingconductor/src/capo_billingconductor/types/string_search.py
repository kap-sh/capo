"""Generated from Smithy shape ``com.amazonaws.billingconductor#StringSearch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.search_option
    import capo_billingconductor.types.search_value


class StringSearch(TypedDict, closed=True):
    search_option: "capo_billingconductor.types.search_option.SearchOption"
    """<p> The search option to be applied when performing the string search. </p>"""
    search_value: "capo_billingconductor.types.search_value.SearchValue"
    """<p> The value to search for within the specified string field. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringSearch) -> dict:
    out: dict = {}
    import capo_billingconductor.types.search_option

    out["SearchOption"] = capo_billingconductor.types.search_option.serialize_json(
        value["search_option"]
    )
    out["SearchValue"] = value["search_value"]
    return out


def deserialize_json(data: dict) -> StringSearch:
    out: StringSearch = {}  # type: ignore[typeddict-item]
    if data.get("SearchOption") is not None:
        import capo_billingconductor.types.search_option

        out["search_option"] = (
            capo_billingconductor.types.search_option.deserialize_json(
                data["SearchOption"]
            )
        )
    else:
        import typing

        out["search_option"] = typing.cast(
            "capo_billingconductor.types.search_option.SearchOption", ""
        )
    if data.get("SearchValue") is not None:
        out["search_value"] = data["SearchValue"]
    else:
        out["search_value"] = ""
    return out
