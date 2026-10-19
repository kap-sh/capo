"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargetForm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.form_name


class SubscriptionTargetForm(TypedDict, closed=True):
    form_name: "capo_datazone.types.form_name.FormName"
    """<p>The form name included in the subscription target configuration.</p>"""
    content: "str"
    """<p>The content of the subscription target configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargetForm) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> SubscriptionTargetForm:
    out: SubscriptionTargetForm = {}  # type: ignore[typeddict-item]
    if data.get("formName") is not None:
        out["form_name"] = data["formName"]
    else:
        out["form_name"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    return out
