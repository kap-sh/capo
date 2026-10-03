"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetIntentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_intent_signature
    import capo_lex_model_building_service.types.code_hook
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.follow_up_prompt
    import capo_lex_model_building_service.types.fulfillment_activity
    import capo_lex_model_building_service.types.input_context_list
    import capo_lex_model_building_service.types.intent_name
    import capo_lex_model_building_service.types.intent_utterance_list
    import capo_lex_model_building_service.types.kendra_configuration
    import capo_lex_model_building_service.types.output_context_list
    import capo_lex_model_building_service.types.prompt
    import capo_lex_model_building_service.types.slot_list
    import capo_lex_model_building_service.types.statement
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.timestamp
    import capo_lex_model_building_service.types.version


class GetIntentResponse(TypedDict, closed=True):
    name: NotRequired["capo_lex_model_building_service.types.intent_name.IntentName"]
    """<p>The name of the intent.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the intent.</p>"""
    slots: NotRequired["capo_lex_model_building_service.types.slot_list.SlotList"]
    """<p>An array of intent slots configured for the intent.</p>"""
    sample_utterances: NotRequired[
        "capo_lex_model_building_service.types.intent_utterance_list.IntentUtteranceList"
    ]
    """<p>An array of sample utterances configured for the intent.</p>"""
    confirmation_prompt: NotRequired[
        "capo_lex_model_building_service.types.prompt.Prompt"
    ]
    """<p>If defined in the bot, Amazon Lex uses prompt to confirm the intent before fulfilling the user's request. For more information, see <a>PutIntent</a>. </p>"""
    rejection_statement: NotRequired[
        "capo_lex_model_building_service.types.statement.Statement"
    ]
    """<p>If the user answers "no" to the question defined in <code>confirmationPrompt</code>, Amazon Lex responds with this statement to acknowledge that the intent was canceled. </p>"""
    follow_up_prompt: NotRequired[
        "capo_lex_model_building_service.types.follow_up_prompt.FollowUpPrompt"
    ]
    """<p>If defined in the bot, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled. For more information, see <a>PutIntent</a>.</p>"""
    conclusion_statement: NotRequired[
        "capo_lex_model_building_service.types.statement.Statement"
    ]
    """<p>After the Lambda function specified in the <code>fulfillmentActivity</code> element fulfills the intent, Amazon Lex conveys this statement to the user.</p>"""
    dialog_code_hook: NotRequired[
        "capo_lex_model_building_service.types.code_hook.CodeHook"
    ]
    """<p>If defined in the bot, Amazon Amazon Lex invokes this Lambda function for each user input. For more information, see <a>PutIntent</a>. </p>"""
    fulfillment_activity: NotRequired[
        "capo_lex_model_building_service.types.fulfillment_activity.FulfillmentActivity"
    ]
    """<p>Describes how the intent is fulfilled. For more information, see <a>PutIntent</a>. </p>"""
    parent_intent_signature: NotRequired[
        "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    """<p>A unique identifier for a built-in intent.</p>"""
    last_updated_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was updated. When you create a resource, the creation date and the last updated date are the same. </p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the intent was created.</p>"""
    version: NotRequired["capo_lex_model_building_service.types.version.Version"]
    """<p>The version of the intent.</p>"""
    checksum: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>Checksum of the intent.</p>"""
    kendra_configuration: NotRequired[
        "capo_lex_model_building_service.types.kendra_configuration.KendraConfiguration"
    ]
    """<p>Configuration information, if any, to connect to an Amazon Kendra index with the <code>AMAZON.KendraSearchIntent</code> intent.</p>"""
    input_contexts: NotRequired[
        "capo_lex_model_building_service.types.input_context_list.InputContextList"
    ]
    """<p>An array of <code>InputContext</code> objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.</p>"""
    output_contexts: NotRequired[
        "capo_lex_model_building_service.types.output_context_list.OutputContextList"
    ]
    """<p>An array of <code>OutputContext</code> objects that lists the contexts that the intent activates when the intent is fulfilled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "slots" in value:
        import capo_lex_model_building_service.types.slot_list

        out["slots"] = capo_lex_model_building_service.types.slot_list.serialize_json(
            value["slots"]
        )
    if "sample_utterances" in value:
        import capo_lex_model_building_service.types.intent_utterance_list

        out["sampleUtterances"] = (
            capo_lex_model_building_service.types.intent_utterance_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "confirmation_prompt" in value:
        import capo_lex_model_building_service.types.prompt

        out["confirmationPrompt"] = (
            capo_lex_model_building_service.types.prompt.serialize_json(
                value["confirmation_prompt"]
            )
        )
    if "rejection_statement" in value:
        import capo_lex_model_building_service.types.statement

        out["rejectionStatement"] = (
            capo_lex_model_building_service.types.statement.serialize_json(
                value["rejection_statement"]
            )
        )
    if "follow_up_prompt" in value:
        import capo_lex_model_building_service.types.follow_up_prompt

        out["followUpPrompt"] = (
            capo_lex_model_building_service.types.follow_up_prompt.serialize_json(
                value["follow_up_prompt"]
            )
        )
    if "conclusion_statement" in value:
        import capo_lex_model_building_service.types.statement

        out["conclusionStatement"] = (
            capo_lex_model_building_service.types.statement.serialize_json(
                value["conclusion_statement"]
            )
        )
    if "dialog_code_hook" in value:
        import capo_lex_model_building_service.types.code_hook

        out["dialogCodeHook"] = (
            capo_lex_model_building_service.types.code_hook.serialize_json(
                value["dialog_code_hook"]
            )
        )
    if "fulfillment_activity" in value:
        import capo_lex_model_building_service.types.fulfillment_activity

        out["fulfillmentActivity"] = (
            capo_lex_model_building_service.types.fulfillment_activity.serialize_json(
                value["fulfillment_activity"]
            )
        )
    if "parent_intent_signature" in value:
        out["parentIntentSignature"] = value["parent_intent_signature"]
    if "last_updated_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "kendra_configuration" in value:
        import capo_lex_model_building_service.types.kendra_configuration

        out["kendraConfiguration"] = (
            capo_lex_model_building_service.types.kendra_configuration.serialize_json(
                value["kendra_configuration"]
            )
        )
    if "input_contexts" in value:
        import capo_lex_model_building_service.types.input_context_list

        out["inputContexts"] = (
            capo_lex_model_building_service.types.input_context_list.serialize_json(
                value["input_contexts"]
            )
        )
    if "output_contexts" in value:
        import capo_lex_model_building_service.types.output_context_list

        out["outputContexts"] = (
            capo_lex_model_building_service.types.output_context_list.serialize_json(
                value["output_contexts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIntentResponse:
    out: GetIntentResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("slots") is not None:
        import capo_lex_model_building_service.types.slot_list

        out["slots"] = capo_lex_model_building_service.types.slot_list.deserialize_json(
            data["slots"]
        )
    if data.get("sampleUtterances") is not None:
        import capo_lex_model_building_service.types.intent_utterance_list

        out["sample_utterances"] = (
            capo_lex_model_building_service.types.intent_utterance_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if data.get("confirmationPrompt") is not None:
        import capo_lex_model_building_service.types.prompt

        out["confirmation_prompt"] = (
            capo_lex_model_building_service.types.prompt.deserialize_json(
                data["confirmationPrompt"]
            )
        )
    if data.get("rejectionStatement") is not None:
        import capo_lex_model_building_service.types.statement

        out["rejection_statement"] = (
            capo_lex_model_building_service.types.statement.deserialize_json(
                data["rejectionStatement"]
            )
        )
    if data.get("followUpPrompt") is not None:
        import capo_lex_model_building_service.types.follow_up_prompt

        out["follow_up_prompt"] = (
            capo_lex_model_building_service.types.follow_up_prompt.deserialize_json(
                data["followUpPrompt"]
            )
        )
    if data.get("conclusionStatement") is not None:
        import capo_lex_model_building_service.types.statement

        out["conclusion_statement"] = (
            capo_lex_model_building_service.types.statement.deserialize_json(
                data["conclusionStatement"]
            )
        )
    if data.get("dialogCodeHook") is not None:
        import capo_lex_model_building_service.types.code_hook

        out["dialog_code_hook"] = (
            capo_lex_model_building_service.types.code_hook.deserialize_json(
                data["dialogCodeHook"]
            )
        )
    if data.get("fulfillmentActivity") is not None:
        import capo_lex_model_building_service.types.fulfillment_activity

        out["fulfillment_activity"] = (
            capo_lex_model_building_service.types.fulfillment_activity.deserialize_json(
                data["fulfillmentActivity"]
            )
        )
    if data.get("parentIntentSignature") is not None:
        out["parent_intent_signature"] = data["parentIntentSignature"]
    if data.get("lastUpdatedDate") is not None:
        import capo_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if data.get("createdDate") is not None:
        import capo_lex_model_building_service.types.timestamp

        out["created_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    if data.get("kendraConfiguration") is not None:
        import capo_lex_model_building_service.types.kendra_configuration

        out["kendra_configuration"] = (
            capo_lex_model_building_service.types.kendra_configuration.deserialize_json(
                data["kendraConfiguration"]
            )
        )
    if data.get("inputContexts") is not None:
        import capo_lex_model_building_service.types.input_context_list

        out["input_contexts"] = (
            capo_lex_model_building_service.types.input_context_list.deserialize_json(
                data["inputContexts"]
            )
        )
    if data.get("outputContexts") is not None:
        import capo_lex_model_building_service.types.output_context_list

        out["output_contexts"] = (
            capo_lex_model_building_service.types.output_context_list.deserialize_json(
                data["outputContexts"]
            )
        )
    return out
