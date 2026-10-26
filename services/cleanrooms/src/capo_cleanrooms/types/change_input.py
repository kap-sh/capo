"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_specification
    import capo_cleanrooms.types.change_specification_type


class ChangeInput(TypedDict, closed=True):
    specification_type: (
        "capo_cleanrooms.types.change_specification_type.ChangeSpecificationType"
    )
    """<p>The type of specification for the change. Currently supports <code>MEMBER</code> for member-related changes.</p>"""
    specification: "capo_cleanrooms.types.change_specification.ChangeSpecification"
    """<p>The specification details for the change. The structure depends on the specification type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.change_specification_type

    out["specificationType"] = (
        capo_cleanrooms.types.change_specification_type.serialize_json(
            value["specification_type"]
        )
    )
    import capo_cleanrooms.types.change_specification

    out["specification"] = capo_cleanrooms.types.change_specification.serialize_json(
        value["specification"]
    )
    return out


def deserialize_json(data: dict) -> ChangeInput:
    out: ChangeInput = {}  # type: ignore[typeddict-item]
    if data.get("specificationType") is not None:
        import capo_cleanrooms.types.change_specification_type

        out["specification_type"] = (
            capo_cleanrooms.types.change_specification_type.deserialize_json(
                data["specificationType"]
            )
        )
    else:
        import typing

        out["specification_type"] = typing.cast(
            "capo_cleanrooms.types.change_specification_type.ChangeSpecificationType",
            "",
        )
    if data.get("specification") is not None:
        import capo_cleanrooms.types.change_specification

        out["specification"] = (
            capo_cleanrooms.types.change_specification.deserialize_json(
                data["specification"]
            )
        )
    else:
        out["specification"] = {"$unknown": {"name": ""}}
    return out
