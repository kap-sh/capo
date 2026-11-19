"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateTrustResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.request_id
    import capo_directory_service.types.trust_id


class UpdateTrustResult(TypedDict, closed=True):
    request_id: NotRequired["capo_directory_service.types.request_id.RequestId"]
    trust_id: NotRequired["capo_directory_service.types.trust_id.TrustId"]
    """<p>Identifier of the trust relationship.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrustResult) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrustResult:
    out: UpdateTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateTrustResult) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "trust_id" in value:
        out["TrustId"] = value["trust_id"]
    return out


def deserialize_cbor(data: dict) -> UpdateTrustResult:
    out: UpdateTrustResult = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    return out
