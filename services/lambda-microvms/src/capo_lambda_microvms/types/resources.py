"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Resources``."""

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError


class Resources(TypedDict, closed=True):
    minimum_memory_in_mi_b: "int"
    """<p>The minimum amount of memory in MiB to allocate to the MicroVM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> dict:
    out: dict = {}
    out["minimumMemoryInMiB"] = value["minimum_memory_in_mi_b"]
    return out


def deserialize_json(data: dict) -> Resources:
    out: Resources = {}  # type: ignore[typeddict-item]
    if data.get("minimumMemoryInMiB") is not None:
        out["minimum_memory_in_mi_b"] = data["minimumMemoryInMiB"]
    else:
        raise DeserializationError("Resources.minimum_memory_in_mi_b required")
    return out
