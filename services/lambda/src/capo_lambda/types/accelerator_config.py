"""Generated from Smithy shape ``com.amazonaws.lambda#AcceleratorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.accelerator_memory_gb


class AcceleratorConfig(TypedDict, closed=True):
    accelerator_memory_size: (
        "capo_lambda.types.accelerator_memory_gb.AcceleratorMemoryGB"
    )
    """<p>The minimum amount of memory (in GB) of each accelerator device exposed to the execution environment. Lambda might allocate more, depending on the accelerator instance types available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorConfig) -> dict:
    out: dict = {}
    import capo_lambda.types.accelerator_memory_gb

    out["AcceleratorMemorySize"] = (
        capo_lambda.types.accelerator_memory_gb.serialize_json(
            value["accelerator_memory_size"]
        )
    )
    return out


def deserialize_json(data: dict) -> AcceleratorConfig:
    out: AcceleratorConfig = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorMemorySize") is not None:
        import capo_lambda.types.accelerator_memory_gb

        out["accelerator_memory_size"] = (
            capo_lambda.types.accelerator_memory_gb.deserialize_json(
                data["AcceleratorMemorySize"]
            )
        )
    else:
        import typing

        out["accelerator_memory_size"] = typing.cast(
            "capo_lambda.types.accelerator_memory_gb.AcceleratorMemoryGB", 0
        )
    return out
