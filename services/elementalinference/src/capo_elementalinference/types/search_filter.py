"""Generated from Smithy shape ``com.amazonaws.elementalinference#SearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.filter_name
    import capo_elementalinference.types.filter_value_list


class SearchFilter(TypedDict, closed=True):
    name: "capo_elementalinference.types.filter_name.FilterName"
    """<p>The dimension of the fixture to filter on. Valid values: COMPETITOR.</p>"""
    values: "capo_elementalinference.types.filter_value_list.FilterValueList"
    """<p>An array of values to match in the dimension that you specified in name. You can specify up to 10 values. A fixture appears in the results if it matches at least one of these values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    import capo_elementalinference.types.filter_name

    out["name"] = capo_elementalinference.types.filter_name.serialize_json(
        value["name"]
    )
    import capo_elementalinference.types.filter_value_list

    out["values"] = capo_elementalinference.types.filter_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_elementalinference.types.filter_name

        out["name"] = capo_elementalinference.types.filter_name.deserialize_json(
            data["name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_elementalinference.types.filter_name.FilterName", ""
        )
    if data.get("values") is not None:
        import capo_elementalinference.types.filter_value_list

        out["values"] = (
            capo_elementalinference.types.filter_value_list.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
