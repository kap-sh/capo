"""Generated from Smithy shape ``com.amazonaws.directoryservice#VerifyTrustRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.trust_id


class VerifyTrustRequest(TypedDict, closed=True):
    trust_id: "capo_directory_service.types.trust_id.TrustId"
    """<p>The unique Trust ID of the trust relationship to verify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyTrustRequest) -> dict:
    out: dict = {}
    out["TrustId"] = value["trust_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyTrustRequest:
    out: VerifyTrustRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    else:
        out["trust_id"] = ""
    return out
