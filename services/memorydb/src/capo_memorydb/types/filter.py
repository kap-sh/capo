"""Generated from Smithy shape ``com.amazonaws.memorydb#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_memorydb.types.filter_name
    import capo_memorydb.types.filter_value_list


class Filter(TypedDict, closed=True):
    name: "capo_memorydb.types.filter_name.FilterName"
    """<p>The property being filtered. For example, UserName.</p>"""
    values: "capo_memorydb.types.filter_value_list.FilterValueList"
    """<p>The property values to filter on. For example, "user-123".</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_memorydb.types.filter_value_list

    out["Values"] = capo_memorydb.types.filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Filter.name required")
    if data.get("Values") is not None:
        import capo_memorydb.types.filter_value_list

        out["values"] = capo_memorydb.types.filter_value_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("Filter.values required")
    return out
