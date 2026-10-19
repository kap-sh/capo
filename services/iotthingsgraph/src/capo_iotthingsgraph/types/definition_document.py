"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DefinitionDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_language
    import capo_iotthingsgraph.types.definition_text


class DefinitionDocument(TypedDict, closed=True):
    language: "capo_iotthingsgraph.types.definition_language.DefinitionLanguage"
    """<p>The language used to define the entity. <code>GRAPHQL</code> is the only valid value.</p>"""
    text: "capo_iotthingsgraph.types.definition_text.DefinitionText"
    """<p>The GraphQL text that defines the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefinitionDocument) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.definition_language

    out["language"] = (
        capo_iotthingsgraph.types.definition_language.serialize_aws_json_1_1(
            value["language"]
        )
    )
    out["text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DefinitionDocument:
    out: DefinitionDocument = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        import capo_iotthingsgraph.types.definition_language

        out["language"] = (
            capo_iotthingsgraph.types.definition_language.deserialize_aws_json_1_1(
                data["language"]
            )
        )
    else:
        import typing

        out["language"] = typing.cast(
            "capo_iotthingsgraph.types.definition_language.DefinitionLanguage", ""
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
