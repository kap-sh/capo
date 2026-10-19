"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Change``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_specification
    import capo_cleanrooms.types.change_specification_type
    import capo_cleanrooms.types.change_type_list


class Change(TypedDict, closed=True):
    specification_type: (
        "capo_cleanrooms.types.change_specification_type.ChangeSpecificationType"
    )
    """<p>The type of specification for this change.</p>"""
    specification: "capo_cleanrooms.types.change_specification.ChangeSpecification"
    """<p>The specification details for this change.</p>"""
    types: "capo_cleanrooms.types.change_type_list.ChangeTypeList"
    """<p>The list of change types that were applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Change) -> dict:
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
    import capo_cleanrooms.types.change_type_list

    out["types"] = capo_cleanrooms.types.change_type_list.serialize_json(value["types"])
    return out


def deserialize_json(data: dict) -> Change:
    out: Change = {}  # type: ignore[typeddict-item]
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
        import capo_cleanrooms.types._unknown

        out["specification"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    if data.get("types") is not None:
        import capo_cleanrooms.types.change_type_list

        out["types"] = capo_cleanrooms.types.change_type_list.deserialize_json(
            data["types"]
        )
    else:
        out["types"] = []
    return out
