"""Generated from Smithy shape ``com.amazonaws.connect#ViewContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view_actions
    import capo_connect.types.view_input_schema
    import capo_connect.types.view_template


class ViewContent(TypedDict, closed=True):
    input_schema: NotRequired["capo_connect.types.view_input_schema.ViewInputSchema"]
    """<p>The data schema matching data that the view template must be provided to render.</p>"""
    template: NotRequired["capo_connect.types.view_template.ViewTemplate"]
    """<p>The view template representing the structure of the view.</p>"""
    actions: NotRequired["capo_connect.types.view_actions.ViewActions"]
    """<p>A list of possible actions from the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewContent) -> dict:
    out: dict = {}
    if "input_schema" in value:
        out["InputSchema"] = value["input_schema"]
    if "template" in value:
        out["Template"] = value["template"]
    if "actions" in value:
        import capo_connect.types.view_actions

        out["Actions"] = capo_connect.types.view_actions.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> ViewContent:
    out: ViewContent = {}  # type: ignore[typeddict-item]
    if data.get("InputSchema") is not None:
        out["input_schema"] = data["InputSchema"]
    if data.get("Template") is not None:
        out["template"] = data["Template"]
    if data.get("Actions") is not None:
        import capo_connect.types.view_actions

        out["actions"] = capo_connect.types.view_actions.deserialize_json(
            data["Actions"]
        )
    return out


def redact_sensitive(value: ViewContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_schema" in value:
        out["input_schema"] = "*** Sensitive Data Redacted ***"
    if "actions" in value:
        import capo_connect.types.view_actions

        out["actions"] = capo_connect.types.view_actions.redact_sensitive(
            value["actions"]
        )
    return out
