"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CreateHsmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.hsm


class CreateHsmResponse(TypedDict, closed=True):
    hsm: NotRequired["capo_cloudhsm_v2.types.hsm.Hsm"]
    """<p>Information about the HSM that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmResponse) -> dict:
    out: dict = {}
    if "hsm" in value:
        import capo_cloudhsm_v2.types.hsm

        out["Hsm"] = capo_cloudhsm_v2.types.hsm.serialize_aws_json_1_1(value["hsm"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmResponse:
    out: CreateHsmResponse = {}  # type: ignore[typeddict-item]
    if data.get("Hsm") is not None:
        import capo_cloudhsm_v2.types.hsm

        out["hsm"] = capo_cloudhsm_v2.types.hsm.deserialize_aws_json_1_1(data["Hsm"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateHsmResponse) -> dict:
    out: dict = {}
    if "hsm" in value:
        import capo_cloudhsm_v2.types.hsm

        out["Hsm"] = capo_cloudhsm_v2.types.hsm.serialize_cbor(value["hsm"])
    return out


def deserialize_cbor(data: dict) -> CreateHsmResponse:
    out: CreateHsmResponse = {}  # type: ignore[typeddict-item]
    if data.get("Hsm") is not None:
        import capo_cloudhsm_v2.types.hsm

        out["hsm"] = capo_cloudhsm_v2.types.hsm.deserialize_cbor(data["Hsm"])
    return out
