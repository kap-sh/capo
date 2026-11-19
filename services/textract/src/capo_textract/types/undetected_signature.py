"""Generated from Smithy shape ``com.amazonaws.textract#UndetectedSignature``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.u_integer


class UndetectedSignature(TypedDict, closed=True):
    page: NotRequired["capo_textract.types.u_integer.UInteger"]
    """<p>The page where a signature was expected but not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndetectedSignature) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UndetectedSignature:
    out: UndetectedSignature = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UndetectedSignature) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_cbor(data: dict) -> UndetectedSignature:
    out: UndetectedSignature = {}  # type: ignore[typeddict-item]
    if data.get("Page") is not None:
        out["page"] = data["Page"]
    return out
