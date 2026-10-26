"""Generated from Smithy shape ``com.amazonaws.artifact#InquiryContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_artifact.errors import DeserializationError, SerializationError
from capo_artifact.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_artifact.types.inquiry_file_content
    import capo_artifact.types.long_string_attribute


class _InquiryContent_query(TypedDict, closed=True):
    query: "capo_artifact.types.long_string_attribute.LongStringAttribute"


class _InquiryContent_fileContent(TypedDict, closed=True):
    fileContent: "capo_artifact.types.inquiry_file_content.InquiryFileContent"


InquiryContent: TypeAlias = (
    _InquiryContent_query | _InquiryContent_fileContent | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InquiryContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InquiryContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "query" in value:
        return {"query": value["query"]}
    elif "fileContent" in value:
        import capo_artifact.types.inquiry_file_content

        return {
            "fileContent": capo_artifact.types.inquiry_file_content.serialize_json(
                value["fileContent"]
            )
        }
    else:
        raise SerializationError("InquiryContent: no variant present")


def deserialize_json(data: dict) -> InquiryContent:
    if data.get("query") is not None:
        return {"query": data["query"]}
    elif data.get("fileContent") is not None:
        import capo_artifact.types.inquiry_file_content

        return {
            "fileContent": capo_artifact.types.inquiry_file_content.deserialize_json(
                data["fileContent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("InquiryContent: no recognized variant key")
