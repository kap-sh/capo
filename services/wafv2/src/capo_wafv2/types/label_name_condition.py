"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelNameCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.label_name


class LabelNameCondition(TypedDict, closed=True):
    label_name: "capo_wafv2.types.label_name.LabelName"
    """<p>The label name that a log record must contain in order to meet the condition. This must be a fully qualified label name. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelNameCondition) -> dict:
    out: dict = {}
    out["LabelName"] = value["label_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelNameCondition:
    out: LabelNameCondition = {}  # type: ignore[typeddict-item]
    if data.get("LabelName") is not None:
        out["label_name"] = data["LabelName"]
    else:
        out["label_name"] = ""
    return out
