"""Generated from Smithy shape ``com.amazonaws.bedrock#CreatePromptRouterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.prompt_router_description
    import capo_bedrock.types.prompt_router_name
    import capo_bedrock.types.prompt_router_target_model
    import capo_bedrock.types.prompt_router_target_models
    import capo_bedrock.types.routing_criteria
    import capo_bedrock.types.tag_list


class CreatePromptRouterRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>"""
    prompt_router_name: "capo_bedrock.types.prompt_router_name.PromptRouterName"
    """<p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>"""
    models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels"
    """<p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>"""
    description: NotRequired[
        "capo_bedrock.types.prompt_router_description.PromptRouterDescription"
    ]
    """<p>An optional description of the prompt router to help identify its purpose.</p>"""
    routing_criteria: "capo_bedrock.types.routing_criteria.RoutingCriteria"
    """<p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>"""
    fallback_model: (
        "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
    )
    """<p>The default model to use when the routing criteria is not met.</p>"""
    tags: NotRequired["capo_bedrock.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRouterRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["promptRouterName"] = value["prompt_router_name"]
    import capo_bedrock.types.prompt_router_target_models

    out["models"] = capo_bedrock.types.prompt_router_target_models.serialize_json(
        value["models"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock.types.routing_criteria

    out["routingCriteria"] = capo_bedrock.types.routing_criteria.serialize_json(
        value["routing_criteria"]
    )
    import capo_bedrock.types.prompt_router_target_model

    out["fallbackModel"] = capo_bedrock.types.prompt_router_target_model.serialize_json(
        value["fallback_model"]
    )
    if "tags" in value:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePromptRouterRequest:
    out: CreatePromptRouterRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("promptRouterName") is not None:
        out["prompt_router_name"] = data["promptRouterName"]
    else:
        out["prompt_router_name"] = ""
    if data.get("models") is not None:
        import capo_bedrock.types.prompt_router_target_models

        out["models"] = capo_bedrock.types.prompt_router_target_models.deserialize_json(
            data["models"]
        )
    else:
        out["models"] = []
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("routingCriteria") is not None:
        import capo_bedrock.types.routing_criteria

        out["routing_criteria"] = capo_bedrock.types.routing_criteria.deserialize_json(
            data["routingCriteria"]
        )
    else:
        raise DeserializationError(
            "CreatePromptRouterRequest.routing_criteria required"
        )
    if data.get("fallbackModel") is not None:
        import capo_bedrock.types.prompt_router_target_model

        out["fallback_model"] = (
            capo_bedrock.types.prompt_router_target_model.deserialize_json(
                data["fallbackModel"]
            )
        )
    else:
        raise DeserializationError("CreatePromptRouterRequest.fallback_model required")
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreatePromptRouterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
