"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateBGPPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.virtual_interface


class CreateBGPPeerResponse(TypedDict, closed=True):
    virtual_interface: NotRequired[
        "capo_direct_connect.types.virtual_interface.VirtualInterface"
    ]
    """<p>The virtual interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBGPPeerResponse) -> dict:
    out: dict = {}
    if "virtual_interface" in value:
        import capo_direct_connect.types.virtual_interface

        out["virtualInterface"] = (
            capo_direct_connect.types.virtual_interface.serialize_aws_json_1_1(
                value["virtual_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBGPPeerResponse:
    out: CreateBGPPeerResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterface") is not None:
        import capo_direct_connect.types.virtual_interface

        out["virtual_interface"] = (
            capo_direct_connect.types.virtual_interface.deserialize_aws_json_1_1(
                data["virtualInterface"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateBGPPeerResponse) -> dict:
    out: dict = {}
    if "virtual_interface" in value:
        import capo_direct_connect.types.virtual_interface

        out["virtualInterface"] = (
            capo_direct_connect.types.virtual_interface.serialize_cbor(
                value["virtual_interface"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateBGPPeerResponse:
    out: CreateBGPPeerResponse = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterface") is not None:
        import capo_direct_connect.types.virtual_interface

        out["virtual_interface"] = (
            capo_direct_connect.types.virtual_interface.deserialize_cbor(
                data["virtualInterface"]
            )
        )
    return out
