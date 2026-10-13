"""Generated from Smithy shape ``com.amazonaws.connect#CreateViewVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view


class CreateViewVersionResponse(TypedDict, closed=True):
    view: NotRequired["capo_connect.types.view.View"]
    """<p>All view data is contained within the View object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewVersionResponse) -> dict:
    out: dict = {}
    if "view" in value:
        import capo_connect.types.view

        out["View"] = capo_connect.types.view.serialize_json(value["view"])
    return out


def deserialize_json(data: dict) -> CreateViewVersionResponse:
    out: CreateViewVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("View") is not None:
        import capo_connect.types.view

        out["view"] = capo_connect.types.view.deserialize_json(data["View"])
    return out


def redact_sensitive(value: CreateViewVersionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "view" in value:
        import capo_connect.types.view

        out["view"] = capo_connect.types.view.redact_sensitive(value["view"])
    return out
