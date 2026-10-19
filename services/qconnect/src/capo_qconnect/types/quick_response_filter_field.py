"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseFilterField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.quick_response_filter_operator
    import capo_qconnect.types.quick_response_filter_value_list


class QuickResponseFilterField(TypedDict, closed=True):
    name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the attribute field to filter the quick responses by.</p>"""
    values: NotRequired[
        "capo_qconnect.types.quick_response_filter_value_list.QuickResponseFilterValueList"
    ]
    """<p>The values of attribute field to filter the quick response by.</p>"""
    operator: (
        "capo_qconnect.types.quick_response_filter_operator.QuickResponseFilterOperator"
    )
    """<p>The operator to use for filtering.</p>"""
    include_no_existence: NotRequired["bool"]
    """<p>Whether to treat null value as a match for the attribute field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseFilterField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "values" in value:
        import capo_qconnect.types.quick_response_filter_value_list

        out["values"] = (
            capo_qconnect.types.quick_response_filter_value_list.serialize_json(
                value["values"]
            )
        )
    out["operator"] = value["operator"]
    if "include_no_existence" in value:
        out["includeNoExistence"] = value["include_no_existence"]
    return out


def deserialize_json(data: dict) -> QuickResponseFilterField:
    out: QuickResponseFilterField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_qconnect.types.quick_response_filter_value_list

        out["values"] = (
            capo_qconnect.types.quick_response_filter_value_list.deserialize_json(
                data["values"]
            )
        )
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    else:
        out["operator"] = ""
    if data.get("includeNoExistence") is not None:
        out["include_no_existence"] = data["includeNoExistence"]
    return out
