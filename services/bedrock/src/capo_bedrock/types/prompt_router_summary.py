"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterSummary``."""

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


class PromptRouterSummary(TypedDict, closed=True):
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
    """<p>The router's ARN.</p>"""
    models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels"
    """<p>The router's models.</p>"""
    fallback_model: (
        "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
    )
    """<p>The router's fallback model.</p>"""
    status: "capo_bedrock.types.prompt_router_status.PromptRouterStatus"
    """<p>The router's status.</p>"""
    type: "capo_bedrock.types.prompt_router_type.PromptRouterType"
    """<p>The summary's type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterSummary) -> dict:
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


def deserialize_json(data: dict) -> PromptRouterSummary:
    out: PromptRouterSummary = {}  # type: ignore[typeddict-item]
    if data.get("promptRouterName") is not None:
        out["prompt_router_name"] = data["promptRouterName"]
    else:
        out["prompt_router_name"] = ""
    if data.get("routingCriteria") is not None:
        import capo_bedrock.types.routing_criteria

        out["routing_criteria"] = capo_bedrock.types.routing_criteria.deserialize_json(
            data["routingCriteria"]
        )
    else:
        raise DeserializationError("PromptRouterSummary.routing_criteria required")
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
        out["prompt_router_arn"] = ""
    if data.get("models") is not None:
        import capo_bedrock.types.prompt_router_target_models

        out["models"] = capo_bedrock.types.prompt_router_target_models.deserialize_json(
            data["models"]
        )
    else:
        out["models"] = []
    if data.get("fallbackModel") is not None:
        import capo_bedrock.types.prompt_router_target_model

        out["fallback_model"] = (
            capo_bedrock.types.prompt_router_target_model.deserialize_json(
                data["fallbackModel"]
            )
        )
    else:
        raise DeserializationError("PromptRouterSummary.fallback_model required")
    if data.get("status") is not None:
        import capo_bedrock.types.prompt_router_status

        out["status"] = capo_bedrock.types.prompt_router_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.prompt_router_status.PromptRouterStatus", ""
        )
    if data.get("type") is not None:
        import capo_bedrock.types.prompt_router_type

        out["type"] = capo_bedrock.types.prompt_router_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock.types.prompt_router_type.PromptRouterType", ""
        )
    return out


def redact_sensitive(value: PromptRouterSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
