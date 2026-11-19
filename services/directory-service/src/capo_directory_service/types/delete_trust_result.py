"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteTrustResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.trust_id


class DeleteTrustResult(TypedDict, closed=True):
    trust_id: NotRequired["capo_directory_service.types.trust_id.TrustId"]
    """<p>The Trust ID of the trust relationship that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrustResult:
    out: DeleteTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteTrustResult) -> dict:
    out: dict = {}
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteTrustResult:
    out: DeleteTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out
