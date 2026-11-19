"""Generated from Smithy shape ``com.amazonaws.directconnect#MacSecKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.ckn
    import capo_direct_connect.types.secret_arn
    import capo_direct_connect.types.start_on_date
    import capo_direct_connect.types.state


class MacSecKey(TypedDict, closed=True):
    secret_arn: NotRequired["capo_direct_connect.types.secret_arn.SecretARN"]
    """<p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.</p>"""
    ckn: NotRequired["capo_direct_connect.types.ckn.Ckn"]
    """<p>The Connection Key Name (CKN) for the MAC Security secret key.</p>"""
    state: NotRequired["capo_direct_connect.types.state.State"]
    """<p>The state of the MAC Security (MACsec) secret key.</p> <p>The possible values are:</p> <ul> <li> <p> <code>associating</code>: The MAC Security (MACsec) secret key is being validated and not yet associated with the connection or LAG.</p> </li> <li> <p> <code>associated</code>: The MAC Security (MACsec) secret key is validated and associated with the connection or LAG.</p> </li> <li> <p> <code>disassociating</code>: The MAC Security (MACsec) secret key is being disassociated from the connection or LAG</p> </li> <li> <p> <code>disassociated</code>: The MAC Security (MACsec) secret key is no longer associated with the connection or LAG.</p> </li> </ul>"""
    start_on: NotRequired["capo_direct_connect.types.start_on_date.StartOnDate"]
    """<p>The date that the MAC Security (MACsec) secret key takes effect. The value is displayed in UTC format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacSecKey) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["secretARN"] = value["secret_arn"]
    if "ckn" in value:
        out["ckn"] = value["ckn"]
    if "state" in value:
        out["state"] = value["state"]
    if "start_on" in value:
        out["startOn"] = value["start_on"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MacSecKey:
    out: MacSecKey = {}  # type: ignore[typeddict-item]
    if data.get("secretARN") is not None:
        out["secret_arn"] = data["secretARN"]
    if data.get("ckn") is not None:
        out["ckn"] = data["ckn"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("startOn") is not None:
        out["start_on"] = data["startOn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MacSecKey) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["secretARN"] = value["secret_arn"]
    if "ckn" in value:
        out["ckn"] = value["ckn"]
    if "state" in value:
        out["state"] = value["state"]
    if "start_on" in value:
        out["startOn"] = value["start_on"]
    return out


def deserialize_cbor(data: dict) -> MacSecKey:
    out: MacSecKey = {}  # type: ignore[typeddict-item]
    if data.get("secretARN") is not None:
        out["secret_arn"] = data["secretARN"]
    if data.get("ckn") is not None:
        out["ckn"] = data["ckn"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("startOn") is not None:
        out["start_on"] = data["startOn"]
    return out
