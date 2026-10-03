"""Generated from Smithy shape ``com.amazonaws.amp#PutAlertManagerDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.alert_manager_definition_data
    import capo_amp.types.idempotency_token
    import capo_amp.types.workspace_id


class PutAlertManagerDefinitionRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update the alert manager definition in.</p>"""
    data: "capo_amp.types.alert_manager_definition_data.AlertManagerDefinitionData"
    """<p>The alert manager definition to use. A base64-encoded version of the YAML alert manager definition file.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAlertManagerDefinitionRequest) -> dict:
    out: dict = {}
    import capo_amp.types.alert_manager_definition_data

    out["data"] = capo_amp.types.alert_manager_definition_data.serialize_json(
        value["data"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutAlertManagerDefinitionRequest:
    out: PutAlertManagerDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_amp.types.alert_manager_definition_data

        out["data"] = capo_amp.types.alert_manager_definition_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("PutAlertManagerDefinitionRequest.data required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
