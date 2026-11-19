"""Generated from Smithy shape ``com.amazonaws.snowball#CreateAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import capo_snowball.types.address


class CreateAddressRequest(TypedDict, closed=True):
    address: "capo_snowball.types.address.Address"
    """<p>The address that you want the Snow device shipped to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAddressRequest) -> dict:
    out: dict = {}
    import capo_snowball.types.address

    out["Address"] = capo_snowball.types.address.serialize_aws_json_1_1(
        value["address"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAddressRequest:
    out: CreateAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        import capo_snowball.types.address

        out["address"] = capo_snowball.types.address.deserialize_aws_json_1_1(
            data["Address"]
        )
    else:
        raise DeserializationError("CreateAddressRequest.address required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAddressRequest) -> dict:
    out: dict = {}
    import capo_snowball.types.address

    out["Address"] = capo_snowball.types.address.serialize_cbor(value["address"])
    return out


def deserialize_cbor(data: dict) -> CreateAddressRequest:
    out: CreateAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        import capo_snowball.types.address

        out["address"] = capo_snowball.types.address.deserialize_cbor(data["Address"])
    else:
        raise DeserializationError("CreateAddressRequest.address required")
    return out
