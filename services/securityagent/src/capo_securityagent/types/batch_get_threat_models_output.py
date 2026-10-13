"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_id_list
    import capo_securityagent.types.threat_model_list


class BatchGetThreatModelsOutput(TypedDict, closed=True):
    threat_models: NotRequired[
        "capo_securityagent.types.threat_model_list.ThreatModelList"
    ]
    """<p>The list of threat models that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.threat_model_id_list.ThreatModelIdList"
    ]
    """<p>The list of threat model identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelsOutput) -> dict:
    out: dict = {}
    if "threat_models" in value:
        import capo_securityagent.types.threat_model_list

        out["threatModels"] = capo_securityagent.types.threat_model_list.serialize_json(
            value["threat_models"]
        )
    if "not_found" in value:
        import capo_securityagent.types.threat_model_id_list

        out["notFound"] = capo_securityagent.types.threat_model_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelsOutput:
    out: BatchGetThreatModelsOutput = {}  # type: ignore[typeddict-item]
    if data.get("threatModels") is not None:
        import capo_securityagent.types.threat_model_list

        out["threat_models"] = (
            capo_securityagent.types.threat_model_list.deserialize_json(
                data["threatModels"]
            )
        )
    if data.get("notFound") is not None:
        import capo_securityagent.types.threat_model_id_list

        out["not_found"] = (
            capo_securityagent.types.threat_model_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out


def redact_sensitive(value: BatchGetThreatModelsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "threat_models" in value:
        import capo_securityagent.types.threat_model_list

        out["threat_models"] = (
            capo_securityagent.types.threat_model_list.redact_sensitive(
                value["threat_models"]
            )
        )
    return out
