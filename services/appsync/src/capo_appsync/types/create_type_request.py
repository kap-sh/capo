"""Generated from Smithy shape ``com.amazonaws.appsync#CreateTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.string
    import capo_appsync.types.type_definition_format


class CreateTypeRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    definition: "capo_appsync.types.string.String"
    """<p>The type definition, in GraphQL Schema Definition Language (SDL) format.</p> <p>For more information, see the <a href="http://graphql.org/learn/schema/">GraphQL SDL documentation</a>.</p>"""
    format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat"
    """<p>The type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTypeRequest) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    import capo_appsync.types.type_definition_format

    out["format"] = capo_appsync.types.type_definition_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> CreateTypeRequest:
    out: CreateTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("CreateTypeRequest.definition required")
    if data.get("format") is not None:
        import capo_appsync.types.type_definition_format

        out["format"] = capo_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("CreateTypeRequest.format required")
    return out
