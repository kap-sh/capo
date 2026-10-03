"""Generated from Smithy shape ``com.amazonaws.amp#CreateAlertManagerDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.alert_manager_definition_data
    import capo_amp.types.idempotency_token
    import capo_amp.types.workspace_id


class CreateAlertManagerDefinitionRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to add the alert manager definition to.</p>"""
    data: "capo_amp.types.alert_manager_definition_data.AlertManagerDefinitionData"
    """<p>The alert manager definition to add. A base64-encoded version of the YAML alert manager definition file.</p> <p>For details about the alert manager definition, see <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html">AlertManagedDefinitionData</a>.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAlertManagerDefinitionRequest) -> dict:
    out: dict = {}
    import capo_amp.types.alert_manager_definition_data

    out["data"] = capo_amp.types.alert_manager_definition_data.serialize_json(
        value["data"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAlertManagerDefinitionRequest:
    out: CreateAlertManagerDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_amp.types.alert_manager_definition_data

        out["data"] = capo_amp.types.alert_manager_definition_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("CreateAlertManagerDefinitionRequest.data required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
