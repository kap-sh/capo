"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FulfillmentUpdatesSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.fulfillment_start_response_specification
    import capo_lex_models_v2.types.fulfillment_timeout
    import capo_lex_models_v2.types.fulfillment_update_response_specification


class FulfillmentUpdatesSpecification(TypedDict, closed=True):
    active: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.</p> <p>If the <code>active</code> field is set to true, the <code>startResponse</code>, <code>updateResponse</code>, and <code>timeoutInSeconds</code> fields are required.</p>"""
    start_response: NotRequired[
        "capo_lex_models_v2.types.fulfillment_start_response_specification.FulfillmentStartResponseSpecification"
    ]
    """<p>Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.</p>"""
    update_response: NotRequired[
        "capo_lex_models_v2.types.fulfillment_update_response_specification.FulfillmentUpdateResponseSpecification"
    ]
    """<p>Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.</p>"""
    timeout_in_seconds: NotRequired[
        "capo_lex_models_v2.types.fulfillment_timeout.FulfillmentTimeout"
    ]
    """<p>The length of time that the fulfillment Lambda function should run before it times out.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FulfillmentUpdatesSpecification) -> dict:
    out: dict = {}
    out["active"] = value["active"]
    if "start_response" in value:
        import capo_lex_models_v2.types.fulfillment_start_response_specification

        out["startResponse"] = (
            capo_lex_models_v2.types.fulfillment_start_response_specification.serialize_json(
                value["start_response"]
            )
        )
    if "update_response" in value:
        import capo_lex_models_v2.types.fulfillment_update_response_specification

        out["updateResponse"] = (
            capo_lex_models_v2.types.fulfillment_update_response_specification.serialize_json(
                value["update_response"]
            )
        )
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    return out


def deserialize_json(data: dict) -> FulfillmentUpdatesSpecification:
    out: FulfillmentUpdatesSpecification = {}  # type: ignore[typeddict-item]
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = False
    if data.get("startResponse") is not None:
        import capo_lex_models_v2.types.fulfillment_start_response_specification

        out["start_response"] = (
            capo_lex_models_v2.types.fulfillment_start_response_specification.deserialize_json(
                data["startResponse"]
            )
        )
    if data.get("updateResponse") is not None:
        import capo_lex_models_v2.types.fulfillment_update_response_specification

        out["update_response"] = (
            capo_lex_models_v2.types.fulfillment_update_response_specification.deserialize_json(
                data["updateResponse"]
            )
        )
    if data.get("timeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    return out
