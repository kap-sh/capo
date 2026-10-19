"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_payload
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.target_resource


class ExecuteActionRequest(TypedDict, closed=True):
    target_resource: "capo_iotsitewise.types.target_resource.TargetResource"
    """<p>The resource the action will be taken on.</p>"""
    action_definition_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_payload: "capo_iotsitewise.types.action_payload.ActionPayload"
    """<p>The JSON payload of the action.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this action resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteActionRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.target_resource

    out["targetResource"] = capo_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["actionDefinitionId"] = value["action_definition_id"]
    import capo_iotsitewise.types.action_payload

    out["actionPayload"] = capo_iotsitewise.types.action_payload.serialize_json(
        value["action_payload"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> ExecuteActionRequest:
    out: ExecuteActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetResource") is not None:
        import capo_iotsitewise.types.target_resource

        out["target_resource"] = (
            capo_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("ExecuteActionRequest.target_resource required")
    if data.get("actionDefinitionId") is not None:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        out["action_definition_id"] = ""
    if data.get("actionPayload") is not None:
        import capo_iotsitewise.types.action_payload

        out["action_payload"] = capo_iotsitewise.types.action_payload.deserialize_json(
            data["actionPayload"]
        )
    else:
        raise DeserializationError("ExecuteActionRequest.action_payload required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("resolveTo") is not None:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out
