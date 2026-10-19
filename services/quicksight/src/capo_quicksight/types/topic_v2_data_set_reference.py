"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.limited_string


class TopicV2DataSetReference(TypedDict, closed=True):
    data_set_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data set.</p>"""
    data_set_name: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The name of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetReference) -> dict:
    out: dict = {}
    out["DataSetArn"] = value["data_set_arn"]
    if "data_set_name" in value:
        out["DataSetName"] = value["data_set_name"]
    return out


def deserialize_json(data: dict) -> TopicV2DataSetReference:
    out: TopicV2DataSetReference = {}  # type: ignore[typeddict-item]
    if data.get("DataSetArn") is not None:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        out["data_set_arn"] = ""
    if data.get("DataSetName") is not None:
        out["data_set_name"] = data["DataSetName"]
    return out
