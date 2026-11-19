"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateMacSecKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.mac_sec_key_list


class AssociateMacSecKeyResponse(TypedDict, closed=True):
    connection_id: NotRequired["capo_direct_connect.types.connection_id.ConnectionId"]
    """<p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p>"""
    mac_sec_keys: NotRequired[
        "capo_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys associated with the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateMacSecKeyResponse) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            capo_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateMacSecKeyResponse:
    out: AssociateMacSecKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateMacSecKeyResponse) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "mac_sec_keys" in value:
        import capo_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = capo_direct_connect.types.mac_sec_key_list.serialize_cbor(
            value["mac_sec_keys"]
        )
    return out


def deserialize_cbor(data: dict) -> AssociateMacSecKeyResponse:
    out: AssociateMacSecKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("macSecKeys") is not None:
        import capo_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            capo_direct_connect.types.mac_sec_key_list.deserialize_cbor(
                data["macSecKeys"]
            )
        )
    return out
