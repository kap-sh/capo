"""Generated from Smithy shape ``com.amazonaws.lambdaweb#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.filter_value_list


class Filter(TypedDict, closed=True):
    name: "str"
    """<p>The name of the filter field.</p>"""
    values: "capo_lambda_web.types.filter_value_list.FilterValueList"
    """<p>The values to match for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_lambda_web.types.filter_value_list

    out["values"] = capo_lambda_web.types.filter_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Filter.name required")
    if data.get("values") is not None:
        import capo_lambda_web.types.filter_value_list

        out["values"] = capo_lambda_web.types.filter_value_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("Filter.values required")
    return out
