"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeExpenseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.document


class AnalyzeExpenseRequest(TypedDict, closed=True):
    document: "capo_textract.types.document.Document"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeExpenseRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document

    out["Document"] = capo_textract.types.document.serialize_aws_json_1_1(
        value["document"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeExpenseRequest:
    out: AnalyzeExpenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        import capo_textract.types.document

        out["document"] = capo_textract.types.document.deserialize_aws_json_1_1(
            data["Document"]
        )
    else:
        raise DeserializationError("AnalyzeExpenseRequest.document required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalyzeExpenseRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document

    out["Document"] = capo_textract.types.document.serialize_cbor(value["document"])
    return out


def deserialize_cbor(data: dict) -> AnalyzeExpenseRequest:
    out: AnalyzeExpenseRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        import capo_textract.types.document

        out["document"] = capo_textract.types.document.deserialize_cbor(
            data["Document"]
        )
    else:
        raise DeserializationError("AnalyzeExpenseRequest.document required")
    return out
