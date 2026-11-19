"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MemorySizeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.nullable_memory
    import capo_compute_optimizer.types.nullable_memory_reservation


class MemorySizeConfiguration(TypedDict, closed=True):
    memory: NotRequired["capo_compute_optimizer.types.nullable_memory.NullableMemory"]
    """<p> The amount of memory in the container. </p>"""
    memory_reservation: NotRequired[
        "capo_compute_optimizer.types.nullable_memory_reservation.NullableMemoryReservation"
    ]
    """<p> The limit of memory reserve for the container. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MemorySizeConfiguration) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MemorySizeConfiguration:
    out: MemorySizeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MemorySizeConfiguration) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    return out


def deserialize_cbor(data: dict) -> MemorySizeConfiguration:
    out: MemorySizeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    return out
