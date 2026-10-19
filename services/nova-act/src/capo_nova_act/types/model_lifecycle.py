"""Generated from Smithy shape ``com.amazonaws.novaact#ModelLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.model_status


class ModelLifecycle(TypedDict, closed=True):
    status: "capo_nova_act.types.model_status.ModelStatus"
    """<p>The current lifecycle status of the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelLifecycle) -> dict:
    out: dict = {}
    import capo_nova_act.types.model_status

    out["status"] = capo_nova_act.types.model_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> ModelLifecycle:
    out: ModelLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_nova_act.types.model_status

        out["status"] = capo_nova_act.types.model_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_nova_act.types.model_status.ModelStatus", "")
    return out
