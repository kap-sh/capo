"""Generated from Smithy shape ``com.amazonaws.personalize#FieldsForThemeGeneration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.column_name


class FieldsForThemeGeneration(TypedDict, closed=True):
    item_name: "capo_personalize.types.column_name.ColumnName"
    """<p>The name of the Items dataset column that stores the name of each item in the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldsForThemeGeneration) -> dict:
    out: dict = {}
    out["itemName"] = value["item_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldsForThemeGeneration:
    out: FieldsForThemeGeneration = {}  # type: ignore[typeddict-item]
    if data.get("itemName") is not None:
        out["item_name"] = data["itemName"]
    else:
        out["item_name"] = ""
    return out
