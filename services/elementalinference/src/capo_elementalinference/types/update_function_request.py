"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateFunctionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.event_bridge_delivery_mode
    import capo_elementalinference.types.function_description
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_target
    import capo_elementalinference.types.jsonata_expression
    import capo_elementalinference.types.resource_name


class UpdateFunctionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.function_id.FunctionId"
    """<p>The ID of the function.</p>"""
    name: NotRequired["capo_elementalinference.types.resource_name.ResourceName"]
    """<p>A new name for the function. You can't change the name while the function is referenced by a feed. </p>"""
    target: NotRequired["capo_elementalinference.types.function_target.FunctionTarget"]
    """<p>A new target for the function. You can't change the target while the function is referenced by a feed. </p>"""
    request_expression: NotRequired[
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    ]
    """<p>A new request expression for the function. Elemental Inference derives contextTypes again from the new expression. While a feed references the function, the new expression must reference the same media context as the current one. </p>"""
    response_expression: NotRequired[
        "capo_elementalinference.types.jsonata_expression.JsonataExpression"
    ]
    """<p>A new response expression for the function. To remove the response expression, specify an empty string. A function with a Bedrock target and eventBridgeDelivery set to ENABLED must keep a response expression. </p>"""
    description: NotRequired[
        "capo_elementalinference.types.function_description.FunctionDescription"
    ]
    """<p>A new description for the function.</p>"""
    event_bridge_delivery: NotRequired[
        "capo_elementalinference.types.event_bridge_delivery_mode.EventBridgeDeliveryMode"
    ]
    """<p>Specifies whether Elemental Inference also sends this function's marked results to Amazon EventBridge, as described for CreateFunction. If you omit this parameter, the current value is kept. While a feed references the function, you can change this value to DISABLED, but not to ENABLED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "target" in value:
        import capo_elementalinference.types.function_target

        out["target"] = capo_elementalinference.types.function_target.serialize_json(
            value["target"]
        )
    if "request_expression" in value:
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
    return out


def deserialize_json(data: dict) -> UpdateFunctionRequest:
    out: UpdateFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("target") is not None:
        import capo_elementalinference.types.function_target

        out["target"] = capo_elementalinference.types.function_target.deserialize_json(
            data["target"]
        )
    if data.get("requestExpression") is not None:
        out["request_expression"] = data["requestExpression"]
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
    return out


def redact_sensitive(value: UpdateFunctionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_expression" in value:
        out["request_expression"] = "*** Sensitive Data Redacted ***"
    if "response_expression" in value:
        out["response_expression"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
