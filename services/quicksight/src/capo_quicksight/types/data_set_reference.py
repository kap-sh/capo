"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.non_empty_string


class DataSetReference(TypedDict, closed=True):
    data_set_placeholder: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>Dataset placeholder.</p>"""
    data_set_arn: "capo_quicksight.types.arn.Arn"
    """<p>Dataset Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetReference) -> dict:
    out: dict = {}
    out["DataSetPlaceholder"] = value["data_set_placeholder"]
    out["DataSetArn"] = value["data_set_arn"]
    return out


def deserialize_json(data: dict) -> DataSetReference:
    out: DataSetReference = {}  # type: ignore[typeddict-item]
    if data.get("DataSetPlaceholder") is not None:
        out["data_set_placeholder"] = data["DataSetPlaceholder"]
    else:
        out["data_set_placeholder"] = ""
    if data.get("DataSetArn") is not None:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        out["data_set_arn"] = ""
    return out
