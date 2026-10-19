"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.pivoted_label_list


class PivotConfiguration(TypedDict, closed=True):
    label_column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column that contains the labels to be pivoted into separate columns.</p>"""
    pivoted_labels: "capo_quicksight.types.pivoted_label_list.PivotedLabelList"
    """<p>The list of specific label values to pivot into separate columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotConfiguration) -> dict:
    out: dict = {}
    if "label_column_name" in value:
        out["LabelColumnName"] = value["label_column_name"]
    import capo_quicksight.types.pivoted_label_list

    out["PivotedLabels"] = capo_quicksight.types.pivoted_label_list.serialize_json(
        value["pivoted_labels"]
    )
    return out


def deserialize_json(data: dict) -> PivotConfiguration:
    out: PivotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LabelColumnName") is not None:
        out["label_column_name"] = data["LabelColumnName"]
    if data.get("PivotedLabels") is not None:
        import capo_quicksight.types.pivoted_label_list

        out["pivoted_labels"] = (
            capo_quicksight.types.pivoted_label_list.deserialize_json(
                data["PivotedLabels"]
            )
        )
    else:
        out["pivoted_labels"] = []
    return out
