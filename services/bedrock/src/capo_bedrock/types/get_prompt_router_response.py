"""Generated from Smithy shape ``com.amazonaws.bedrock#GetPromptRouterResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.prompt_router_arn
    import capo_bedrock.types.prompt_router_description
    import capo_bedrock.types.prompt_router_name
    import capo_bedrock.types.prompt_router_status
    import capo_bedrock.types.prompt_router_target_model
    import capo_bedrock.types.prompt_router_target_models
    import capo_bedrock.types.prompt_router_type
    import capo_bedrock.types.routing_criteria
    import capo_bedrock.types.timestamp


class GetPromptRouterResponse(TypedDict, closed=True):
    prompt_router_name: "capo_bedrock.types.prompt_router_name.PromptRouterName"
    """<p>The router's name.</p>"""
    routing_criteria: "capo_bedrock.types.routing_criteria.RoutingCriteria"
    """<p>The router's routing criteria.</p>"""
    description: NotRequired[
        "capo_bedrock.types.prompt_router_description.PromptRouterDescription"
    ]
    """<p>The router's description.</p>"""
    created_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>When the router was created.</p>"""
    updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>When the router was updated.</p>"""
    prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn"
    """<p>The prompt router's ARN</p>"""
    models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels"
    """<p>The router's models.</p>"""
    fallback_model: (
        "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
    )
    """<p>The router's fallback model.</p>"""
    status: "capo_bedrock.types.prompt_router_status.PromptRouterStatus"
    """<p>The router's status.</p>"""
    type: "capo_bedrock.types.prompt_router_type.PromptRouterType"
    """<p>The router's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPromptRouterResponse) -> dict:
    out: dict = {}
    out["promptRouterName"] = value["prompt_router_name"]
    import capo_bedrock.types.routing_criteria

    out["routingCriteria"] = capo_bedrock.types.routing_criteria.serialize_json(
        value["routing_criteria"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_bedrock.types.timestamp

        out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_bedrock.types.timestamp

        out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    out["promptRouterArn"] = value["prompt_router_arn"]
    import capo_bedrock.types.prompt_router_target_models

    out["models"] = capo_bedrock.types.prompt_router_target_models.serialize_json(
        value["models"]
    )
    import capo_bedrock.types.prompt_router_target_model

    out["fallbackModel"] = capo_bedrock.types.prompt_router_target_model.serialize_json(
        value["fallback_model"]
    )
    import capo_bedrock.types.prompt_router_status

    out["status"] = capo_bedrock.types.prompt_router_status.serialize_json(
        value["status"]
    )
    import capo_bedrock.types.prompt_router_type

    out["type"] = capo_bedrock.types.prompt_router_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> GetPromptRouterResponse:
    out: GetPromptRouterResponse = {}  # type: ignore[typeddict-item]
    if data.get("promptRouterName") is not None:
        out["prompt_router_name"] = data["promptRouterName"]
    else:
        raise DeserializationError(
            "GetPromptRouterResponse.prompt_router_name required"
        )
    if data.get("routingCriteria") is not None:
        import capo_bedrock.types.routing_criteria

        out["routing_criteria"] = capo_bedrock.types.routing_criteria.deserialize_json(
            data["routingCriteria"]
        )
    else:
        raise DeserializationError("GetPromptRouterResponse.routing_criteria required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("promptRouterArn") is not None:
        out["prompt_router_arn"] = data["promptRouterArn"]
    else:
        raise DeserializationError("GetPromptRouterResponse.prompt_router_arn required")
    if data.get("models") is not None:
        import capo_bedrock.types.prompt_router_target_models

        out["models"] = capo_bedrock.types.prompt_router_target_models.deserialize_json(
            data["models"]
        )
    else:
        raise DeserializationError("GetPromptRouterResponse.models required")
    if data.get("fallbackModel") is not None:
        import capo_bedrock.types.prompt_router_target_model

        out["fallback_model"] = (
            capo_bedrock.types.prompt_router_target_model.deserialize_json(
                data["fallbackModel"]
            )
        )
    else:
        raise DeserializationError("GetPromptRouterResponse.fallback_model required")
    if data.get("status") is not None:
        import capo_bedrock.types.prompt_router_status

        out["status"] = capo_bedrock.types.prompt_router_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetPromptRouterResponse.status required")
    if data.get("type") is not None:
        import capo_bedrock.types.prompt_router_type

        out["type"] = capo_bedrock.types.prompt_router_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetPromptRouterResponse.type required")
    return out


def redact_sensitive(value: GetPromptRouterResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
