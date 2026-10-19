"""Generated from Smithy shape ``com.amazonaws.lakeformation#PartitionValueList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.value_string_list


class PartitionValueList(TypedDict, closed=True):
    values: "capo_lakeformation.types.value_string_list.ValueStringList"
    """<p>The list of partition values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionValueList) -> dict:
    out: dict = {}
    import capo_lakeformation.types.value_string_list

    out["Values"] = capo_lakeformation.types.value_string_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> PartitionValueList:
    out: PartitionValueList = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_lakeformation.types.value_string_list

        out["values"] = capo_lakeformation.types.value_string_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
