"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GpuInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.gpus


class GpuInfo(TypedDict, closed=True):
    gpus: NotRequired["capo_compute_optimizer.types.gpus.Gpus"]
    """<p> Describes the GPU accelerators for the instance type. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GpuInfo) -> dict:
    out: dict = {}
    if "gpus" in value:
        import capo_compute_optimizer.types.gpus

        out["gpus"] = capo_compute_optimizer.types.gpus.serialize_aws_json_1_0(
            value["gpus"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GpuInfo:
    out: GpuInfo = {}  # type: ignore[typeddict-item]
    if data.get("gpus") is not None:
        import capo_compute_optimizer.types.gpus

        out["gpus"] = capo_compute_optimizer.types.gpus.deserialize_aws_json_1_0(
            data["gpus"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GpuInfo) -> dict:
    out: dict = {}
    if "gpus" in value:
        import capo_compute_optimizer.types.gpus

        out["gpus"] = capo_compute_optimizer.types.gpus.serialize_cbor(value["gpus"])
    return out


def deserialize_cbor(data: dict) -> GpuInfo:
    out: GpuInfo = {}  # type: ignore[typeddict-item]
    if data.get("gpus") is not None:
        import capo_compute_optimizer.types.gpus

        out["gpus"] = capo_compute_optimizer.types.gpus.deserialize_cbor(data["gpus"])
    return out
