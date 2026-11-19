"""Generated from Smithy shape ``com.amazonaws.snowball#TaxDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.ind_tax_documents


class TaxDocuments(TypedDict, closed=True):
    ind: NotRequired["capo_snowball.types.ind_tax_documents.INDTaxDocuments"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaxDocuments) -> dict:
    out: dict = {}
    if "ind" in value:
        import capo_snowball.types.ind_tax_documents

        out["IND"] = capo_snowball.types.ind_tax_documents.serialize_aws_json_1_1(
            value["ind"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaxDocuments:
    out: TaxDocuments = {}  # type: ignore[typeddict-item]
    if data.get("IND") is not None:
        import capo_snowball.types.ind_tax_documents

        out["ind"] = capo_snowball.types.ind_tax_documents.deserialize_aws_json_1_1(
            data["IND"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaxDocuments) -> dict:
    out: dict = {}
    if "ind" in value:
        import capo_snowball.types.ind_tax_documents

        out["IND"] = capo_snowball.types.ind_tax_documents.serialize_cbor(value["ind"])
    return out


def deserialize_cbor(data: dict) -> TaxDocuments:
    out: TaxDocuments = {}  # type: ignore[typeddict-item]
    if data.get("IND") is not None:
        import capo_snowball.types.ind_tax_documents

        out["ind"] = capo_snowball.types.ind_tax_documents.deserialize_cbor(data["IND"])
    return out
