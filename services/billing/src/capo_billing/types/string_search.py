"""Generated from Smithy shape ``com.amazonaws.billing#StringSearch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.search_option
    import capo_billing.types.search_value


class StringSearch(TypedDict, closed=True):
    search_option: "capo_billing.types.search_option.SearchOption"
    """<p> The type of search operation to perform on the string value. Determines how the search value is matched against the target field. </p>"""
    search_value: "capo_billing.types.search_value.SearchValue"
    """<p> The string value to use in the search operation. This value is compared against the target field using the specified search option. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringSearch) -> dict:
    out: dict = {}
    import capo_billing.types.search_option

    out["searchOption"] = capo_billing.types.search_option.serialize_aws_json_1_0(
        value["search_option"]
    )
    out["searchValue"] = value["search_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StringSearch:
    out: StringSearch = {}  # type: ignore[typeddict-item]
    if data.get("searchOption") is not None:
        import capo_billing.types.search_option

        out["search_option"] = (
            capo_billing.types.search_option.deserialize_aws_json_1_0(
                data["searchOption"]
            )
        )
    else:
        import typing

        out["search_option"] = typing.cast(
            "capo_billing.types.search_option.SearchOption", ""
        )
    if data.get("searchValue") is not None:
        out["search_value"] = data["searchValue"]
    else:
        out["search_value"] = ""
    return out
