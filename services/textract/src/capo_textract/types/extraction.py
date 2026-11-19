"""Generated from Smithy shape ``com.amazonaws.textract#Extraction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.expense_document
    import capo_textract.types.identity_document
    import capo_textract.types.lending_document


class Extraction(TypedDict, closed=True):
    lending_document: NotRequired[
        "capo_textract.types.lending_document.LendingDocument"
    ]
    """<p>Holds the structured data returned by AnalyzeDocument for lending documents.</p>"""
    expense_document: NotRequired[
        "capo_textract.types.expense_document.ExpenseDocument"
    ]
    identity_document: NotRequired[
        "capo_textract.types.identity_document.IdentityDocument"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Extraction) -> dict:
    out: dict = {}
    if "lending_document" in value:
        import capo_textract.types.lending_document

        out["LendingDocument"] = (
            capo_textract.types.lending_document.serialize_aws_json_1_1(
                value["lending_document"]
            )
        )
    if "expense_document" in value:
        import capo_textract.types.expense_document

        out["ExpenseDocument"] = (
            capo_textract.types.expense_document.serialize_aws_json_1_1(
                value["expense_document"]
            )
        )
    if "identity_document" in value:
        import capo_textract.types.identity_document

        out["IdentityDocument"] = (
            capo_textract.types.identity_document.serialize_aws_json_1_1(
                value["identity_document"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Extraction:
    out: Extraction = {}  # type: ignore[typeddict-item]
    if data.get("LendingDocument") is not None:
        import capo_textract.types.lending_document

        out["lending_document"] = (
            capo_textract.types.lending_document.deserialize_aws_json_1_1(
                data["LendingDocument"]
            )
        )
    if data.get("ExpenseDocument") is not None:
        import capo_textract.types.expense_document

        out["expense_document"] = (
            capo_textract.types.expense_document.deserialize_aws_json_1_1(
                data["ExpenseDocument"]
            )
        )
    if data.get("IdentityDocument") is not None:
        import capo_textract.types.identity_document

        out["identity_document"] = (
            capo_textract.types.identity_document.deserialize_aws_json_1_1(
                data["IdentityDocument"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Extraction) -> dict:
    out: dict = {}
    if "lending_document" in value:
        import capo_textract.types.lending_document

        out["LendingDocument"] = capo_textract.types.lending_document.serialize_cbor(
            value["lending_document"]
        )
    if "expense_document" in value:
        import capo_textract.types.expense_document

        out["ExpenseDocument"] = capo_textract.types.expense_document.serialize_cbor(
            value["expense_document"]
        )
    if "identity_document" in value:
        import capo_textract.types.identity_document

        out["IdentityDocument"] = capo_textract.types.identity_document.serialize_cbor(
            value["identity_document"]
        )
    return out


def deserialize_cbor(data: dict) -> Extraction:
    out: Extraction = {}  # type: ignore[typeddict-item]
    if data.get("LendingDocument") is not None:
        import capo_textract.types.lending_document

        out["lending_document"] = capo_textract.types.lending_document.deserialize_cbor(
            data["LendingDocument"]
        )
    if data.get("ExpenseDocument") is not None:
        import capo_textract.types.expense_document

        out["expense_document"] = capo_textract.types.expense_document.deserialize_cbor(
            data["ExpenseDocument"]
        )
    if data.get("IdentityDocument") is not None:
        import capo_textract.types.identity_document

        out["identity_document"] = (
            capo_textract.types.identity_document.deserialize_cbor(
                data["IdentityDocument"]
            )
        )
    return out
