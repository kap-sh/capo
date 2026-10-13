"""Generated from Smithy shape ``com.amazonaws.connect#UpdateViewContentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view


class UpdateViewContentResponse(TypedDict, closed=True):
    view: NotRequired["capo_connect.types.view.View"]
    """<p>A view resource object. Contains metadata and content necessary to render the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateViewContentResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import capo_connect.types.view

        out["View"] = capo_connect.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> UpdateViewContentResponse:
    out: UpdateViewContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("View") is not None:
        import capo_connect.types.view

        out["view"] = capo_connect.types.view.deserialize_json(data["View"])
    return out


def redact_sensitive(value: UpdateViewContentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_connect.types.view

        out["view"] = capo_connect.types.view.redact_sensitive(value["view"])
    return out
