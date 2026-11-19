"""Generated from Smithy shape ``com.amazonaws.textract#DocumentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.u_integer


class DocumentMetadata(TypedDict, closed=True):
    pages: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The number of pages that are detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Pages") is not None:
        out["pages"] = data["Pages"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "pages" in value:
        out["Pages"] = value["pages"]
    return out


def deserialize_cbor(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Pages") is not None:
        out["pages"] = data["Pages"]
    return out
