"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id


class CopyProductOutput(TypedDict, closed=True):
    copy_product_token: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The token to use to track the progress of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProductOutput) -> dict:
    out: dict = {}
    if "copy_product_token" in value:
        out["CopyProductToken"] = value["copy_product_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProductOutput:
    out: CopyProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("CopyProductToken") is not None:
        out["copy_product_token"] = data["CopyProductToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopyProductOutput) -> dict:
    out: dict = {}
    if "copy_product_token" in value:
        out["CopyProductToken"] = value["copy_product_token"]
    return out


def deserialize_cbor(data: dict) -> CopyProductOutput:
    out: CopyProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("CopyProductToken") is not None:
        out["copy_product_token"] = data["CopyProductToken"]
    return out
