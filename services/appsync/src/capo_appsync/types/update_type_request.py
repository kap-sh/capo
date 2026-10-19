"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.type_definition_format


class UpdateTypeRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The new type name.</p>"""
    definition: NotRequired["capo_appsync.types.string.String"]
    """<p>The new definition.</p>"""
    format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat"
    """<p>The new type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTypeRequest) -> dict:
    out: dict = {}
    if "definition" in value:
        out["definition"] = value["definition"]
    import capo_appsync.types.type_definition_format

    out["format"] = capo_appsync.types.type_definition_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTypeRequest:
    out: UpdateTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    if data.get("format") is not None:
        import capo_appsync.types.type_definition_format

        out["format"] = capo_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_appsync.types.type_definition_format.TypeDefinitionFormat", ""
        )
    return out
