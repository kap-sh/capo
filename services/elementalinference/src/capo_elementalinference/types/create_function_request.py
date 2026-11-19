"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateFunctionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.event_bridge_delivery_mode
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.jsonata_expression
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class CreateFunctionRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A name for this function.</p>"""
    target: "capo_elementalinference.types.function_target.FunctionTarget"
    """<p>The destination for the request that the function builds.</p>"""
    request_expression: (
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    )
    """<p>The JSONata expression that builds the request. Elemental Inference evaluates it against the media object of the feed, which holds the media and metadata that the function asked for. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference evaluates the expression against sample media and rejects it if the evaluation fails. For a Bedrock target, the result must be a JSON object; Elemental Inference doesn't check that the object is a valid request body for the model. The expression can reference at most one of media.transcript, media.contextual, and media.clip. For a passthrough target, it can't reference media.frames. </p>"""
    response_expression: NotRequired[
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    ]
    """<p>The JSONata expression that selects what to store. Elemental Inference evaluates it against the result as its root: the model response for a Bedrock target, or the output of the request expression for a passthrough target. If a function has no response expression, Elemental Inference stores the entire result. Maximum length: 5,120 characters. </p> <p>When you save the function, Elemental Inference checks that the expression is valid JSONata. For a passthrough target, it also evaluates the request and response expressions together against sample media, and rejects them if they produce no value. </p>"""
    description: NotRequired[
        "capo_elementalinference.types.function_description.FunctionDescription"
    ]
    """<p>The description of the function. Maximum length: 1,024 characters.</p>"""
    event_bridge_delivery: NotRequired[
        "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
    ]
    """<p>Specifies whether Elemental Inference also sends this function's results to Amazon EventBridge. Elemental Inference sends a result only when the result is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code>. It sends the result, unchanged, as a Function Metadata Generated event to the default event bus in your account, after the result is available from GetMetadata. If the result is larger than 64 KB, the event has <code>resultOmitted</code> set to <code>true</code> in place of the result. </p> <p>Valid values:</p> <ul> <li> <p>ENABLED – Elemental Inference sends each marked result as an event.</p> </li> <li> <p>DISABLED (default) – Elemental Inference doesn't send events.</p> </li> </ul> <p>For a Bedrock target, ENABLED requires a response expression, because the model response itself never has a top-level <code>eventBridge</code> field. A feed output that runs a function with ENABLED can't use a fixedInterval trigger shorter than 4 seconds. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>The tags to associate with this function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFunctionRequest) -> dict:
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
    if "event_bridge_delivery" in value:
        import capo_elementalinference.types.event_bridge_delivery_mode

        out["eventBridgeDelivery"] = (
            capo_elementalinference.types.event_bridge_delivery_mode.serialize_json(
                value["event_bridge_delivery"]
            )
        )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFunctionRequest:
    out: CreateFunctionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateFunctionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_expression" in value:
        out["request_expression"] = "*** Sensitive Data Redacted ***"
    if "response_expression" in value:
        out["response_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
