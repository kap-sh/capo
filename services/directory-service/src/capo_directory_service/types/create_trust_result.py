"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateTrustResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.trust_id


class CreateTrustResult(TypedDict, closed=True):
    trust_id: NotRequired["capo_directory_service.types.trust_id.TrustId"]
    """<p>A unique identifier for the trust relationship that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrustResult:
    out: CreateTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_cbor(data: dict) -> CreateTrustResult:
    out: CreateTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out
