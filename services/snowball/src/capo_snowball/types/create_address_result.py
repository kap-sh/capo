"""Generated from Smithy shape ``com.amazonaws.snowball#CreateAddressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class CreateAddressResult(TypedDict, closed=True):
    address_id: NotRequired["capo_snowball.types.string.String"]
    """<p>The automatically generated ID for a specific address. You'll use this ID when you create a job to specify which address you want the Snow device for that job shipped to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAddressResult) -> dict:
    out: dict = {}
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAddressResult:
    out: CreateAddressResult = {}  # type: ignore[typeddict-item]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAddressResult) -> dict:
    out: dict = {}
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    return out


def deserialize_cbor(data: dict) -> CreateAddressResult:
    out: CreateAddressResult = {}  # type: ignore[typeddict-item]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    return out
