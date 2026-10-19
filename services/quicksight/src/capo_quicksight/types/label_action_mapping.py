"""Generated from Smithy shape ``com.amazonaws.quicksight#LabelActionMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dlp_action
    import capo_quicksight.types.label_id
    import capo_quicksight.types.label_name


class LabelActionMapping(TypedDict, closed=True):
    label_id: "capo_quicksight.types.label_id.LabelId"
    """<p>The identifier of the sensitivity label from the DLP provider.</p>"""
    label_name: "capo_quicksight.types.label_name.LabelName"
    """<p>The display name of the sensitivity label from the DLP provider.</p>"""
    action: "capo_quicksight.types.dlp_action.DlpAction"
    """<p>The enforcement action to apply when content with this sensitivity label is detected. Valid values are <code>ALLOW</code>, <code>BLOCK</code>, and <code>WARN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LabelActionMapping) -> dict:
    out: dict = {}
    out["LabelId"] = value["label_id"]
    out["LabelName"] = value["label_name"]
    import capo_quicksight.types.dlp_action

    out["Action"] = capo_quicksight.types.dlp_action.serialize_json(value["action"])
    return out


def deserialize_json(data: dict) -> LabelActionMapping:
    out: LabelActionMapping = {}  # type: ignore[typeddict-item]
    if data.get("LabelId") is not None:
        out["label_id"] = data["LabelId"]
    else:
        out["label_id"] = ""
    if data.get("LabelName") is not None:
        out["label_name"] = data["LabelName"]
    else:
        out["label_name"] = ""
    if data.get("Action") is not None:
        import capo_quicksight.types.dlp_action

        out["action"] = capo_quicksight.types.dlp_action.deserialize_json(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast("capo_quicksight.types.dlp_action.DlpAction", "")
    return out
