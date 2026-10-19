"""Generated from Smithy shape ``com.amazonaws.qconnect#DataReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.content_reference
    import capo_qconnect.types.generative_reference
    import capo_qconnect.types.suggested_message_reference


class _DataReference_contentReference(TypedDict, closed=True):
    contentReference: "capo_qconnect.types.content_reference.ContentReference"


class _DataReference_generativeReference(TypedDict, closed=True):
    generativeReference: "capo_qconnect.types.generative_reference.GenerativeReference"


class _DataReference_suggestedMessageReference(TypedDict, closed=True):
    suggestedMessageReference: (
        "capo_qconnect.types.suggested_message_reference.SuggestedMessageReference"
    )


DataReference: TypeAlias = (
    _DataReference_contentReference
    | _DataReference_generativeReference
    | _DataReference_suggestedMessageReference
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataReference) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataReference: cannot serialize unknown variant {value.name!r}"
        )
    elif "contentReference" in value:
        import capo_qconnect.types.content_reference

        return {
            "contentReference": capo_qconnect.types.content_reference.serialize_json(
                value["contentReference"]
            )
        }
    elif "generativeReference" in value:
        import capo_qconnect.types.generative_reference

        return {
            "generativeReference": capo_qconnect.types.generative_reference.serialize_json(
                value["generativeReference"]
            )
        }
    elif "suggestedMessageReference" in value:
        import capo_qconnect.types.suggested_message_reference

        return {
            "suggestedMessageReference": capo_qconnect.types.suggested_message_reference.serialize_json(
                value["suggestedMessageReference"]
            )
        }
    else:
        raise SerializationError("DataReference: no variant present")


def deserialize_json(data: dict) -> DataReference:
    if data.get("contentReference") is not None:
        import capo_qconnect.types.content_reference

        return {
            "contentReference": capo_qconnect.types.content_reference.deserialize_json(
                data["contentReference"]
            )
        }
    elif data.get("generativeReference") is not None:
        import capo_qconnect.types.generative_reference

        return {
            "generativeReference": capo_qconnect.types.generative_reference.deserialize_json(
                data["generativeReference"]
            )
        }
    elif data.get("suggestedMessageReference") is not None:
        import capo_qconnect.types.suggested_message_reference

        return {
            "suggestedMessageReference": capo_qconnect.types.suggested_message_reference.deserialize_json(
                data["suggestedMessageReference"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DataReference: no recognized variant key")
