"""Generated from Smithy shape ``com.amazonaws.novaact#ModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.model_id
    import capo_nova_act.types.model_lifecycle


class ModelSummary(TypedDict, closed=True):
    model_id: "capo_nova_act.types.model_id.ModelId"
    """<p>The unique identifier of the model.</p>"""
    model_lifecycle: "capo_nova_act.types.model_lifecycle.ModelLifecycle"
    """<p>The lifecycle information for the model.</p>"""
    minimum_compatibility_version: "int"
    """<p>The minimum client compatibility version required to use this model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelSummary) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import capo_nova_act.types.model_lifecycle

    out["modelLifecycle"] = capo_nova_act.types.model_lifecycle.serialize_json(
        value["model_lifecycle"]
    )
    out["minimumCompatibilityVersion"] = value["minimum_compatibility_version"]
    return out


def deserialize_json(data: dict) -> ModelSummary:
    out: ModelSummary = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("modelLifecycle") is not None:
        import capo_nova_act.types.model_lifecycle

        out["model_lifecycle"] = capo_nova_act.types.model_lifecycle.deserialize_json(
            data["modelLifecycle"]
        )
    else:
        raise DeserializationError("ModelSummary.model_lifecycle required")
    if data.get("minimumCompatibilityVersion") is not None:
        out["minimum_compatibility_version"] = data["minimumCompatibilityVersion"]
    else:
        out["minimum_compatibility_version"] = 0
    return out
