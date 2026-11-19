"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.block_list
    import capo_textract.types.identity_document_field_list
    import capo_textract.types.u_integer


class IdentityDocument(TypedDict, closed=True):
    document_index: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>Denotes the placement of a document in the IdentityDocument list. The first document is marked 1, the second 2 and so on.</p>"""
    identity_document_fields: NotRequired[
        "capo_textract.types.identity_document_field_list.IdentityDocumentFieldList"
    ]
    """<p>The structure used to record information extracted from identity documents. Contains both normalized field and value of the extracted text.</p>"""
    blocks: NotRequired["capo_textract.types.block_list.BlockList"]
    """<p>Individual word recognition, as returned by document detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocument) -> dict:
    out: dict = {}
    if "document_index" in value:
        out["DocumentIndex"] = value["document_index"]
    if "identity_document_fields" in value:
        import capo_textract.types.identity_document_field_list

        out["IdentityDocumentFields"] = (
            capo_textract.types.identity_document_field_list.serialize_aws_json_1_1(
                value["identity_document_fields"]
            )
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityDocument:
    out: IdentityDocument = {}  # type: ignore[typeddict-item]
    if data.get("DocumentIndex") is not None:
        out["document_index"] = data["DocumentIndex"]
    if data.get("IdentityDocumentFields") is not None:
        import capo_textract.types.identity_document_field_list

        out["identity_document_fields"] = (
            capo_textract.types.identity_document_field_list.deserialize_aws_json_1_1(
                data["IdentityDocumentFields"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityDocument) -> dict:
    out: dict = {}
    if "document_index" in value:
        out["DocumentIndex"] = value["document_index"]
    if "identity_document_fields" in value:
        import capo_textract.types.identity_document_field_list

        out["IdentityDocumentFields"] = (
            capo_textract.types.identity_document_field_list.serialize_cbor(
                value["identity_document_fields"]
            )
        )
    if "blocks" in value:
        import capo_textract.types.block_list

        out["Blocks"] = capo_textract.types.block_list.serialize_cbor(value["blocks"])
    return out


def deserialize_cbor(data: dict) -> IdentityDocument:
    out: IdentityDocument = {}  # type: ignore[typeddict-item]
    if data.get("DocumentIndex") is not None:
        out["document_index"] = data["DocumentIndex"]
    if data.get("IdentityDocumentFields") is not None:
        import capo_textract.types.identity_document_field_list

        out["identity_document_fields"] = (
            capo_textract.types.identity_document_field_list.deserialize_cbor(
                data["IdentityDocumentFields"]
            )
        )
    if data.get("Blocks") is not None:
        import capo_textract.types.block_list

        out["blocks"] = capo_textract.types.block_list.deserialize_cbor(data["Blocks"])
    return out
