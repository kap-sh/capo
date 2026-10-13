"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormSectionLayoutConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.free_from_layout_element_list


class FreeFormSectionLayoutConfiguration(TypedDict, closed=True):
    elements: (
        "capo_quicksight.types.free_from_layout_element_list.FreeFromLayoutElementList"
    )
    """<p>The elements that are included in the free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormSectionLayoutConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.free_from_layout_element_list

    out["Elements"] = (
        capo_quicksight.types.free_from_layout_element_list.serialize_json(
            value["elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> FreeFormSectionLayoutConfiguration:
    out: FreeFormSectionLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Elements") is not None:
        import capo_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            capo_quicksight.types.free_from_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        raise DeserializationError(
            "FreeFormSectionLayoutConfiguration.elements required"
        )
    return out


def redact_sensitive(value: FreeFormSectionLayoutConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "elements" in value:
        import capo_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            capo_quicksight.types.free_from_layout_element_list.redact_sensitive(
                value["elements"]
            )
        )
    return out
