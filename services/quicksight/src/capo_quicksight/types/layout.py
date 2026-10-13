"""Generated from Smithy shape ``com.amazonaws.quicksight#Layout``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.layout_configuration


class Layout(TypedDict, closed=True):
    configuration: "capo_quicksight.types.layout_configuration.LayoutConfiguration"
    """<p>The configuration that determines what the type of layout for a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Layout) -> dict:
    out: dict = {}
    import capo_quicksight.types.layout_configuration

    out["Configuration"] = capo_quicksight.types.layout_configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> Layout:
    out: Layout = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_quicksight.types.layout_configuration

        out["configuration"] = (
            capo_quicksight.types.layout_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("Layout.configuration required")
    return out


def redact_sensitive(value: Layout) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_quicksight.types.layout_configuration

        out["configuration"] = (
            capo_quicksight.types.layout_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
