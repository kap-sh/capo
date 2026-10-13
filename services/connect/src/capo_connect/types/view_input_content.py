"""Generated from Smithy shape ``com.amazonaws.connect#ViewInputContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view_actions
    import capo_connect.types.view_template


class ViewInputContent(TypedDict, closed=True):
    template: NotRequired["capo_connect.types.view_template.ViewTemplate"]
    """<p>The view template representing the structure of the view.</p>"""
    actions: NotRequired["capo_connect.types.view_actions.ViewActions"]
    """<p>A list of possible actions from the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewInputContent) -> dict:
    out: dict = {}
    if "template" in value:
        out["Template"] = value["template"]
    if "actions" in value:
        import capo_connect.types.view_actions

        out["Actions"] = capo_connect.types.view_actions.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> ViewInputContent:
    out: ViewInputContent = {}  # type: ignore[typeddict-item]
    if data.get("Template") is not None:
        out["template"] = data["Template"]
    if data.get("Actions") is not None:
        import capo_connect.types.view_actions

        out["actions"] = capo_connect.types.view_actions.deserialize_json(
            data["Actions"]
        )
    return out


def redact_sensitive(value: ViewInputContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_connect.types.view_actions

        out["actions"] = capo_connect.types.view_actions.redact_sensitive(
            value["actions"]
        )
    return out
