"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.inference_instance_type


class InferenceResourceConfig(TypedDict, closed=True):
    instance_type: (
        "capo_cleanroomsml.types.inference_instance_type.InferenceInstanceType"
    )
    """<p>The type of instance that is used to perform model inference.</p>"""
    instance_count: "int"
    """<p>The number of instances to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceResourceConfig) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.inference_instance_type

    out["instanceType"] = (
        capo_cleanroomsml.types.inference_instance_type.serialize_json(
            value["instance_type"]
        )
    )
    out["instanceCount"] = value.get("instance_count", 1)
    return out


def deserialize_json(data: dict) -> InferenceResourceConfig:
    out: InferenceResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("instanceType") is not None:
        import capo_cleanroomsml.types.inference_instance_type

        out["instance_type"] = (
            capo_cleanroomsml.types.inference_instance_type.deserialize_json(
                data["instanceType"]
            )
        )
    else:
        import typing

        out["instance_type"] = typing.cast(
            "capo_cleanroomsml.types.inference_instance_type.InferenceInstanceType", ""
        )
    if data.get("instanceCount") is not None:
        out["instance_count"] = data["instanceCount"]
    else:
        out["instance_count"] = 1
    return out
