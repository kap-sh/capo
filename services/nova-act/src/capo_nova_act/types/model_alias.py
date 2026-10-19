"""Generated from Smithy shape ``com.amazonaws.novaact#ModelAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.model_id


class ModelAlias(TypedDict, closed=True):
    alias_name: "capo_nova_act.types.model_id.ModelId"
    """<p>The name of the model alias.</p>"""
    latest_model_id: "capo_nova_act.types.model_id.ModelId"
    """<p>The model ID that this alias currently points to.</p>"""
    resolved_model_id: NotRequired["capo_nova_act.types.model_id.ModelId"]
    """<p>The resolved model ID after alias resolution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelAlias) -> dict:
    out: dict = {}
    out["aliasName"] = value["alias_name"]
    out["latestModelId"] = value["latest_model_id"]
    if "resolved_model_id" in value:
        out["resolvedModelId"] = value["resolved_model_id"]
    return out


def deserialize_json(data: dict) -> ModelAlias:
    out: ModelAlias = {}  # type: ignore[typeddict-item]
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    else:
        out["alias_name"] = ""
    if data.get("latestModelId") is not None:
        out["latest_model_id"] = data["latestModelId"]
    else:
        out["latest_model_id"] = ""
    if data.get("resolvedModelId") is not None:
        out["resolved_model_id"] = data["resolvedModelId"]
    return out
