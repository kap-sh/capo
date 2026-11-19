"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeExpenseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.document_metadata
    import capo_textract.types.expense_document_list


class AnalyzeExpenseResponse(TypedDict, closed=True):
    document_metadata: NotRequired[
        "capo_textract.types.document_metadata.DocumentMetadata"
    ]
    expense_documents: NotRequired[
        "capo_textract.types.expense_document_list.ExpenseDocumentList"
    ]
    """<p>The expenses detected by Amazon Textract.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeExpenseResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = (
            capo_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "expense_documents" in value:
        import capo_textract.types.expense_document_list

        out["ExpenseDocuments"] = (
            capo_textract.types.expense_document_list.serialize_aws_json_1_1(
                value["expense_documents"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeExpenseResponse:
    out: AnalyzeExpenseResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if data.get("ExpenseDocuments") is not None:
        import capo_textract.types.expense_document_list

        out["expense_documents"] = (
            capo_textract.types.expense_document_list.deserialize_aws_json_1_1(
                data["ExpenseDocuments"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalyzeExpenseResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import capo_textract.types.document_metadata

        out["DocumentMetadata"] = capo_textract.types.document_metadata.serialize_cbor(
            value["document_metadata"]
        )
    if "expense_documents" in value:
        import capo_textract.types.expense_document_list

        out["ExpenseDocuments"] = (
            capo_textract.types.expense_document_list.serialize_cbor(
                value["expense_documents"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AnalyzeExpenseResponse:
    out: AnalyzeExpenseResponse = {}  # type: ignore[typeddict-item]
    if data.get("DocumentMetadata") is not None:
        import capo_textract.types.document_metadata

        out["document_metadata"] = (
            capo_textract.types.document_metadata.deserialize_cbor(
                data["DocumentMetadata"]
            )
        )
    if data.get("ExpenseDocuments") is not None:
        import capo_textract.types.expense_document_list

        out["expense_documents"] = (
            capo_textract.types.expense_document_list.deserialize_cbor(
                data["ExpenseDocuments"]
            )
        )
    return out
