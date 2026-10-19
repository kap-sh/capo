"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobWorkerComputeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_worker_compute_type
    import capo_cleanrooms.types.worker_compute_configuration_properties


class ProtectedJobWorkerComputeConfiguration(TypedDict, closed=True):
    type: "capo_cleanrooms.types.protected_job_worker_compute_type.ProtectedJobWorkerComputeType"
    """<p>The worker compute configuration type.</p>"""
    number: "int"
    """<p>The number of workers for a PySpark job.</p>"""
    properties: NotRequired[
        "capo_cleanrooms.types.worker_compute_configuration_properties.WorkerComputeConfigurationProperties"
    ]
    """<p>The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your Clean Rooms workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobWorkerComputeConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_worker_compute_type

    out["type"] = (
        capo_cleanrooms.types.protected_job_worker_compute_type.serialize_json(
            value["type"]
        )
    )
    out["number"] = value["number"]
    if "properties" in value:
        import capo_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanrooms.types.worker_compute_configuration_properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobWorkerComputeConfiguration:
    out: ProtectedJobWorkerComputeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cleanrooms.types.protected_job_worker_compute_type

        out["type"] = (
            capo_cleanrooms.types.protected_job_worker_compute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.protected_job_worker_compute_type.ProtectedJobWorkerComputeType",
            "",
        )
    if data.get("number") is not None:
        out["number"] = data["number"]
    else:
        out["number"] = 0
    if data.get("properties") is not None:
        import capo_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanrooms.types.worker_compute_configuration_properties.deserialize_json(
                data["properties"]
            )
        )
    return out
