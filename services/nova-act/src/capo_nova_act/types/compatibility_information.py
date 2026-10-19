"""Generated from Smithy shape ``com.amazonaws.novaact#CompatibilityInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.model_id_list
    import capo_nova_act.types.non_blank_string


class CompatibilityInformation(TypedDict, closed=True):
    client_compatibility_version: "int"
    """<p>The client compatibility version that was requested.</p>"""
    supported_model_ids: "capo_nova_act.types.model_id_list.ModelIdList"
    """<p>A list of model IDs that are supported for the client compatibility version.</p>"""
    message: NotRequired["capo_nova_act.types.non_blank_string.NonBlankString"]
    """<p>Additional information about compatibility requirements or recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompatibilityInformation) -> dict:
    out: dict = {}
    out["clientCompatibilityVersion"] = value["client_compatibility_version"]
    import capo_nova_act.types.model_id_list

    out["supportedModelIds"] = capo_nova_act.types.model_id_list.serialize_json(
        value["supported_model_ids"]
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CompatibilityInformation:
    out: CompatibilityInformation = {}  # type: ignore[typeddict-item]
    if data.get("clientCompatibilityVersion") is not None:
        out["client_compatibility_version"] = data["clientCompatibilityVersion"]
    else:
        out["client_compatibility_version"] = 0
    if data.get("supportedModelIds") is not None:
        import capo_nova_act.types.model_id_list

        out["supported_model_ids"] = capo_nova_act.types.model_id_list.deserialize_json(
            data["supportedModelIds"]
        )
    else:
        out["supported_model_ids"] = []
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
