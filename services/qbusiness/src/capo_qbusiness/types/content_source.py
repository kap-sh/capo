"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.retriever_content_source


class _ContentSource_retriever(TypedDict, closed=True):
    retriever: "capo_qbusiness.types.retriever_content_source.RetrieverContentSource"


ContentSource: TypeAlias = _ContentSource_retriever | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ContentSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ContentSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "retriever" in value:
        import capo_qbusiness.types.retriever_content_source

        return {
            "retriever": capo_qbusiness.types.retriever_content_source.serialize_json(
                value["retriever"]
            )
        }
    else:
        raise SerializationError("ContentSource: no variant present")


def deserialize_json(data: dict) -> ContentSource:
    if data.get("retriever") is not None:
        import capo_qbusiness.types.retriever_content_source

        return {
            "retriever": capo_qbusiness.types.retriever_content_source.deserialize_json(
                data["retriever"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ContentSource: no recognized variant key")
