"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateViewOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.view


class CreateViewOutput(TypedDict, closed=True):
    view: NotRequired["capo_resource_explorer_2.types.view.View"]
    """<p>A structure that contains the details about the new view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewOutput) -> dict:
    out: dict = {}
    if "view" in value:
        import capo_resource_explorer_2.types.view

        out["View"] = capo_resource_explorer_2.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> CreateViewOutput:
    out: CreateViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("View") is not None:
        import capo_resource_explorer_2.types.view

        out["view"] = capo_resource_explorer_2.types.view.deserialize_json(data["View"])
    return out


def redact_sensitive(value: CreateViewOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_resource_explorer_2.types.view

        out["view"] = capo_resource_explorer_2.types.view.redact_sensitive(
            value["view"]
        )
    return out
