"""Generated from Smithy shape ``com.amazonaws.snowball#INDTaxDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.gstin


class INDTaxDocuments(TypedDict, closed=True):
    gstin: NotRequired["capo_snowball.types.gstin.GSTIN"]
    """<p>The Goods and Services Tax (GST) documents required in Amazon Web Services Region in India.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: INDTaxDocuments) -> dict:
    out: dict = {}
    if "gstin" in value:
        out["GSTIN"] = value["gstin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> INDTaxDocuments:
    out: INDTaxDocuments = {}  # type: ignore[typeddict-item]
    if data.get("GSTIN") is not None:
        out["gstin"] = data["GSTIN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: INDTaxDocuments) -> dict:
    out: dict = {}
    if "gstin" in value:
        out["GSTIN"] = value["gstin"]
    return out


def deserialize_cbor(data: dict) -> INDTaxDocuments:
    out: INDTaxDocuments = {}  # type: ignore[typeddict-item]
    if data.get("GSTIN") is not None:
        out["gstin"] = data["GSTIN"]
    return out
