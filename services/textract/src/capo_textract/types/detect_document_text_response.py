"""Generated from Smithy shape ``com.amazonaws.textract#DetectDocumentTextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.block_list
    import capo_textract.types.document_metadata
    import capo_textract.types.string


class DetectDocumentTextResponse(TypedDict, closed=True):
    document_metadata: NotRequired[
        "capo_textract.types.document_metadata.DocumentMetadata"
    ]
    """<p>Metadata about the document. It contains the number of pages that are detected in the document.</p>"""
    blocks: NotRequired["capo_textract.types.block_list.BlockList"]
    """<p>An array of <code>Block</code> objects that contain the text that's detected in the document.</p>"""
    detect_document_text_model_version: NotRequired["capo_textract.types.string.String"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectDocumentTextResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = (
            capo_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    if "detect_document_text_model_version" in value:
        out["DetectDocumentTextModelVersion"] = value[
            "detect_document_text_model_version"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectDocumentTextResponse:
    out: DetectDocumentTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    if data.get("DetectDocumentTextModelVersion") is not None:
        out["detect_document_text_model_version"] = data[
            "DetectDocumentTextModelVersion"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectDocumentTextResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = capo_textract.types.document_metadata.serialize_cbor(
            value["document_metadata"]
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_cbor(value["blocks"])
    if "detect_document_text_model_version" in value:
        out["DetectDocumentTextModelVersion"] = value[
            "detect_document_text_model_version"
        ]
    return out


def deserialize_cbor(data: dict) -> DetectDocumentTextResponse:
    out: DetectDocumentTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_cbor(
                data["DocumentMetadata"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_cbor(data["Blocks"])
    if data.get("DetectDocumentTextModelVersion") is not None:
        out["detect_document_text_model_version"] = data[
            "DetectDocumentTextModelVersion"
        ]
    return out
