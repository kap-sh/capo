"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_extracted_characters


class DocumentMetadata(TypedDict, closed=True):
    pages: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>Number of pages in the document.</p>"""
    extracted_characters: NotRequired[
        "capo_comprehend.types.list_of_extracted_characters.ListOfExtractedCharacters"
    ]
    """<p>List of pages in the document, with the number of characters extracted from each page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    if "extracted_characters" in value:
        import capo_comprehend.types.list_of_extracted_characters

        out["ExtractedCharacters"] = (
            capo_comprehend.types.list_of_extracted_characters.serialize_aws_json_1_1(
                value["extracted_characters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Pages") is not None:
        out["pages"] = data["Pages"]
    if data.get("ExtractedCharacters") is not None:
        import capo_comprehend.types.list_of_extracted_characters

        out["extracted_characters"] = (
            capo_comprehend.types.list_of_extracted_characters.deserialize_aws_json_1_1(
                data["ExtractedCharacters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    if "extracted_characters" in value:
        import capo_comprehend.types.list_of_extracted_characters

        out["ExtractedCharacters"] = (
            capo_comprehend.types.list_of_extracted_characters.serialize_cbor(
                value["extracted_characters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Pages") is not None:
        out["pages"] = data["Pages"]
    if data.get("ExtractedCharacters") is not None:
        import capo_comprehend.types.list_of_extracted_characters

        out["extracted_characters"] = (
            capo_comprehend.types.list_of_extracted_characters.deserialize_cbor(
                data["ExtractedCharacters"]
            )
        )
    return out
