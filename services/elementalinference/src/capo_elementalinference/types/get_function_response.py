"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFunctionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.context_type_list
    import capo_elementalinference.types.event_bridge_delivery_mode
    import capo_elementalinference.types.feed_references
    import capo_elementalinference.types.function_arn
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_status
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.jsonata_expression
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class GetFunctionResponse(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the function.</p>"""
    target: "capo_elementalinference.types.function_target.FunctionTarget"
    """<p>The destination for the request that the function builds.</p>"""
    request_expression: (
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    )
    """<p>The JSONata expression that builds the request. Elemental Inference evaluates it against the media object of the feed, which holds the media and metadata that the function asked for. </p>"""
    response_expression: NotRequired[
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    ]
    """<p>The JSONata expression that selects what to store. Elemental Inference evaluates it against the result as its root: the model response for a Bedrock target, or the output of the request expression for a passthrough target. If a function has no response expression, Elemental Inference stores the entire result. </p>"""
    description: NotRequired[
        "capo_elementalinference.types.function_description.FunctionDescription"
    ]
    """<p>The description of the function.</p>"""
    event_bridge_delivery: "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
    """<p>Indicates whether Elemental Inference also sends this function's results to Amazon EventBridge. With ENABLED, each result that is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code> is also sent as a Function Metadata Generated event to the default event bus in your account. </p>"""
    arn: "capo_elementalinference.types.function_arn.FunctionArn"
    """<p>The ARN of the function.</p>"""
    id: "capo_elementalinference.types.function_id.FunctionId"
    """<p>The ID of the function.</p>"""
    status: "capo_elementalinference.types.function_status.FunctionStatus"
    """<p>The status of the function.</p>"""
    references: NotRequired[
        "capo_elementalinference.types.feed_references.FeedReferences"
    ]
    """<p>The IDs of the feeds that have a function output, enabled or disabled, that references this function. While this list isn't empty, the function can't be deleted, and its name and target can't be changed. </p>"""
    context_types: NotRequired[
        "capo_elementalinference.types.context_type_list.ContextTypeList"
    ]
    """<p>The kinds of media context that this function uses. Elemental Inference derives this field from the media paths that the request expression references; you can't set it. An empty list means that the expression references no media, so Elemental Inference supplies none at run time. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>The tags associated with the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_elementalinference.types.function_target

    out["target"] = capo_elementalinference.types.function_target.serialize_json(
        value["target"]
    )
    out["requestExpression"] = value["request_expression"]
    if "response_expression" in value:
        out["responseExpression"] = value["response_expression"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_elementalinference.types.event_bridge_delivery_mode

    out["eventBridgeDelivery"] = (
        capo_elementalinference.types.event_bridge_delivery_mode.serialize_json(
            value.get("event_bridge_delivery", "DISABLED")
        )
    )
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_elementalinference.types.function_status

    out["status"] = capo_elementalinference.types.function_status.serialize_json(
        value["status"]
    )
    if "references" in value:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.serialize_json(
                value["references"]
            )
        )
    if "context_types" in value:
        import capo_elementalinference.types.context_type_list

        out["contextTypes"] = (
            capo_elementalinference.types.context_type_list.serialize_json(
                value["context_types"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetFunctionResponse:
    out: GetFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("target") is not None:
        import capo_elementalinference.types.function_target

        out["target"] = capo_elementalinference.types.function_target.deserialize_json(
            data["target"]
        )
    else:
        out["target"] = {"$unknown": {"name": ""}}
    if data.get("requestExpression") is not None:
        out["request_expression"] = data["requestExpression"]
    else:
        out["request_expression"] = ""
    if data.get("responseExpression") is not None:
        out["response_expression"] = data["responseExpression"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("eventBridgeDelivery") is not None:
        import capo_elementalinference.types.event_bridge_delivery_mode

        out["event_bridge_delivery"] = (
            capo_elementalinference.types.event_bridge_delivery_mode.deserialize_json(
                data["eventBridgeDelivery"]
            )
        )
    else:
        out["event_bridge_delivery"] = "DISABLED"
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        import capo_elementalinference.types.function_status

        out["status"] = capo_elementalinference.types.function_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.function_status.FunctionStatus", ""
        )
    if data.get("references") is not None:
        import capo_elementalinference.types.feed_references

        out["references"] = (
            capo_elementalinference.types.feed_references.deserialize_json(
                data["references"]
            )
        )
    if data.get("contextTypes") is not None:
        import capo_elementalinference.types.context_type_list

        out["context_types"] = (
            capo_elementalinference.types.context_type_list.deserialize_json(
                data["contextTypes"]
            )
        )
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: GetFunctionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_expression" in value:
        out["request_expression"] = "*** Sensitive Data Redacted ***"
    if "response_expression" in value:
        out["response_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
