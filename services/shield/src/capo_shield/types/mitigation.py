"""Generated from Smithy shape ``com.amazonaws.shield#Mitigation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.string


class Mitigation(TypedDict, closed=True):
    mitigation_name: NotRequired["capo_shield.types.string.String"]
    """<p>The name of the mitigation taken for this attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mitigation) -> dict:
    out: dict = {}
    if "mitigation_name" in value:
        out["MitigationName"] = value["mitigation_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Mitigation:
    out: Mitigation = {}  # type: ignore[typeddict-item]
    if data.get("MitigationName") is not None:
        out["mitigation_name"] = data["MitigationName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Mitigation) -> dict:
    out: dict = {}
    if "mitigation_name" in value:
        out["MitigationName"] = value["mitigation_name"]
    return out


def deserialize_cbor(data: dict) -> Mitigation:
    out: Mitigation = {}  # type: ignore[typeddict-item]
    if data.get("MitigationName") is not None:
        out["mitigation_name"] = data["MitigationName"]
    return out
