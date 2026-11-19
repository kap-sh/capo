"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteHsmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.hsm_id


class DeleteHsmResponse(TypedDict, closed=True):
    hsm_id: NotRequired["capo_cloudhsm_v2.types.hsm_id.HsmId"]
    """<p>The identifier (ID) of the HSM that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmResponse) -> dict:
    out: dict = {}
    if "hsm_id" in value:
        out["HsmId"] = value["hsm_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmResponse:
    out: DeleteHsmResponse = {}  # type: ignore[typeddict-item]
    if data.get("HsmId") is not None:
        out["hsm_id"] = data["HsmId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteHsmResponse) -> dict:
    out: dict = {}
    if "hsm_id" in value:
        out["HsmId"] = value["hsm_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteHsmResponse:
    out: DeleteHsmResponse = {}  # type: ignore[typeddict-item]
    if data.get("HsmId") is not None:
        out["hsm_id"] = data["HsmId"]
    return out
