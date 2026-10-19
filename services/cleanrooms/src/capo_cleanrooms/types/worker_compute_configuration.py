"""Generated from Smithy shape ``com.amazonaws.cleanrooms#WorkerComputeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.worker_compute_configuration_properties
    import capo_cleanrooms.types.worker_compute_type


class WorkerComputeConfiguration(TypedDict, closed=True):
    type: NotRequired["capo_cleanrooms.types.worker_compute_type.WorkerComputeType"]
    """<p> The worker compute configuration type.</p>"""
    number: NotRequired["int"]
    """<p> The number of workers.</p> <p>SQL queries support a minimum value of 2 and a maximum value of 400. </p> <p>PySpark jobs support a minimum value of 4 and a maximum value of 128.</p>"""
    properties: NotRequired[
        "capo_cleanrooms.types.worker_compute_configuration_properties.WorkerComputeConfigurationProperties"
    ]
    """<p>The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your Clean Rooms workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_cleanrooms.types.worker_compute_type

        out["type"] = capo_cleanrooms.types.worker_compute_type.serialize_json(
            value["type"]
        )
    if "number" in value:
        out["number"] = value["number"]
    if "properties" in value:
        import capo_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanrooms.types.worker_compute_configuration_properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerComputeConfiguration:
    out: WorkerComputeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cleanrooms.types.worker_compute_type

        out["type"] = capo_cleanrooms.types.worker_compute_type.deserialize_json(
            data["type"]
        )
    if data.get("number") is not None:
        out["number"] = data["number"]
    if data.get("properties") is not None:
        import capo_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            capo_cleanrooms.types.worker_compute_configuration_properties.deserialize_json(
                data["properties"]
            )
        )
    return out
