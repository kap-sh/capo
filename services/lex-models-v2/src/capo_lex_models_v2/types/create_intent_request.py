"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateIntentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.dialog_code_hook_settings
    import capo_lex_models_v2.types.display_name
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.fulfillment_code_hook_settings
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.initial_response_setting
    import capo_lex_models_v2.types.input_contexts_list
    import capo_lex_models_v2.types.intent_closing_setting
    import capo_lex_models_v2.types.intent_confirmation_setting
    import capo_lex_models_v2.types.intent_signature
    import capo_lex_models_v2.types.kendra_configuration
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.output_contexts_list
    import capo_lex_models_v2.types.q_in_connect_intent_configuration
    import capo_lex_models_v2.types.qn_a_intent_configuration
    import capo_lex_models_v2.types.sample_utterances_list


class CreateIntentRequest(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent. Intent names must be unique in the locale that contains the intent and cannot match the name of any built-in intent.</p>"""
    intent_display_name: NotRequired[
        "capo_lex_models_v2.types.display_name.DisplayName"
    ]
    """<p>A display name for the intent. If configured, This name will be shown to users during Intent Disambiguation instead of the intent name. Display names should be user-friendly, descriptive and match the intent's purpose to improve user experience during disambiguation.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>A description of the intent. Use the description to help identify the intent in lists.</p>"""
    parent_intent_signature: NotRequired[
        "capo_lex_models_v2.types.intent_signature.IntentSignature"
    ]
    """<p>A unique identifier for the built-in intent to base this intent on.</p>"""
    sample_utterances: NotRequired[
        "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>An array of strings that a user might say to signal the intent. For example, "I want a pizza", or "I want a {PizzaSize} pizza". </p> <p>In an utterance, slot names are enclosed in curly braces ("{", "}") to indicate where they should be displayed in the utterance shown to the user.. </p>"""
    dialog_code_hook: NotRequired[
        "capo_lex_models_v2.types.dialog_code_hook_settings.DialogCodeHookSettings"
    ]
    """<p>Specifies that Amazon Lex invokes the alias Lambda function for each user input. You can invoke this Lambda function to personalize user interaction.</p> <p>For example, suppose that your bot determines that the user's name is John. You Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, <code>glutenIntolerant</code> to <code>true</code>. You might find John's phone number and set the corresponding session attribute.</p>"""
    fulfillment_code_hook: NotRequired[
        "capo_lex_models_v2.types.fulfillment_code_hook_settings.FulfillmentCodeHookSettings"
    ]
    """<p>Specifies that Amazon Lex invokes the alias Lambda function when the intent is ready for fulfillment. You can invoke this function to complete the bot's transaction with the user.</p> <p>For example, in a pizza ordering bot, the Lambda function can look up the closest pizza restaurant to the customer's location and then place an order on the customer's behalf.</p>"""
    intent_confirmation_setting: NotRequired[
        "capo_lex_models_v2.types.intent_confirmation_setting.IntentConfirmationSetting"
    ]
    """<p>Provides prompts that Amazon Lex sends to the user to confirm the completion of an intent. If the user answers "no," the settings contain a statement that is sent to the user to end the intent.</p>"""
    intent_closing_setting: NotRequired[
        "capo_lex_models_v2.types.intent_closing_setting.IntentClosingSetting"
    ]
    """<p>Sets the response that Amazon Lex sends to the user when the intent is closed.</p>"""
    input_contexts: NotRequired[
        "capo_lex_models_v2.types.input_contexts_list.InputContextsList"
    ]
    """<p>A list of contexts that must be active for this intent to be considered by Amazon Lex.</p> <p>When an intent has an input context list, Amazon Lex only considers using the intent in an interaction with the user when the specified contexts are included in the active context list for the session. If the contexts are not active, then Amazon Lex will not use the intent.</p> <p>A context can be automatically activated using the <code>outputContexts</code> property or it can be set at runtime.</p> <p> For example, if there are two intents with different input contexts that respond to the same utterances, only the intent with the active context will respond.</p> <p>An intent may have up to 5 input contexts. If an intent has multiple input contexts, all of the contexts must be active to consider the intent.</p>"""
    output_contexts: NotRequired[
        "capo_lex_models_v2.types.output_contexts_list.OutputContextsList"
    ]
    """<p>A lists of contexts that the intent activates when it is fulfilled.</p> <p>You can use an output context to indicate the intents that Amazon Lex should consider for the next turn of the conversation with a customer. </p> <p>When you use the <code>outputContextsList</code> property, all of the contexts specified in the list are activated when the intent is fulfilled. You can set up to 10 output contexts. You can also set the number of conversation turns that the context should be active, or the length of time that the context should be active.</p>"""
    kendra_configuration: NotRequired[
        "capo_lex_models_v2.types.kendra_configuration.KendraConfiguration"
    ]
    """<p>Configuration information required to use the <code>AMAZON.KendraSearchIntent</code> intent to connect to an Amazon Kendra index. The <code>AMAZON.KendraSearchIntent</code> intent is called when Amazon Lex can't determine another intent to invoke.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with this intent.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot associated with this intent.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    initial_response_setting: NotRequired[
        "capo_lex_models_v2.types.initial_response_setting.InitialResponseSetting"
    ]
    """<p>Configuration settings for the response that is sent to the user at the beginning of a conversation, before eliciting slot values.</p>"""
    qn_a_intent_configuration: NotRequired[
        "capo_lex_models_v2.types.qn_a_intent_configuration.QnAIntentConfiguration"
    ]
    """<p>Specifies the configuration of the built-in <code>Amazon.QnAIntent</code>. The <code>AMAZON.QnAIntent</code> intent is called when Amazon Lex can't determine another intent to invoke. If you specify this field, you can't specify the <code>kendraConfiguration</code> field.</p>"""
    q_in_connect_intent_configuration: NotRequired[
        "capo_lex_models_v2.types.q_in_connect_intent_configuration.QInConnectIntentConfiguration"
    ]
    """<p>Qinconnect intent configuration details for the create intent request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntentRequest) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    if "intent_display_name" in value:
        out["intentDisplayName"] = value["intent_display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_intent_signature" in value:
        out["parentIntentSignature"] = value["parent_intent_signature"]
    if "sample_utterances" in value:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sampleUtterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.serialize_json(
                value["sample_utterances"]
            )
        )
    if "dialog_code_hook" in value:
        import capo_lex_models_v2.types.dialog_code_hook_settings

        out["dialogCodeHook"] = (
            capo_lex_models_v2.types.dialog_code_hook_settings.serialize_json(
                value["dialog_code_hook"]
            )
        )
    if "fulfillment_code_hook" in value:
        import capo_lex_models_v2.types.fulfillment_code_hook_settings

        out["fulfillmentCodeHook"] = (
            capo_lex_models_v2.types.fulfillment_code_hook_settings.serialize_json(
                value["fulfillment_code_hook"]
            )
        )
    if "intent_confirmation_setting" in value:
        import capo_lex_models_v2.types.intent_confirmation_setting

        out["intentConfirmationSetting"] = (
            capo_lex_models_v2.types.intent_confirmation_setting.serialize_json(
                value["intent_confirmation_setting"]
            )
        )
    if "intent_closing_setting" in value:
        import capo_lex_models_v2.types.intent_closing_setting

        out["intentClosingSetting"] = (
            capo_lex_models_v2.types.intent_closing_setting.serialize_json(
                value["intent_closing_setting"]
            )
        )
    if "input_contexts" in value:
        import capo_lex_models_v2.types.input_contexts_list

        out["inputContexts"] = (
            capo_lex_models_v2.types.input_contexts_list.serialize_json(
                value["input_contexts"]
            )
        )
    if "output_contexts" in value:
        import capo_lex_models_v2.types.output_contexts_list

        out["outputContexts"] = (
            capo_lex_models_v2.types.output_contexts_list.serialize_json(
                value["output_contexts"]
            )
        )
    if "kendra_configuration" in value:
        import capo_lex_models_v2.types.kendra_configuration

        out["kendraConfiguration"] = (
            capo_lex_models_v2.types.kendra_configuration.serialize_json(
                value["kendra_configuration"]
            )
        )
    if "initial_response_setting" in value:
        import capo_lex_models_v2.types.initial_response_setting

        out["initialResponseSetting"] = (
            capo_lex_models_v2.types.initial_response_setting.serialize_json(
                value["initial_response_setting"]
            )
        )
    if "qn_a_intent_configuration" in value:
        import capo_lex_models_v2.types.qn_a_intent_configuration

        out["qnAIntentConfiguration"] = (
            capo_lex_models_v2.types.qn_a_intent_configuration.serialize_json(
                value["qn_a_intent_configuration"]
            )
        )
    if "q_in_connect_intent_configuration" in value:
        import capo_lex_models_v2.types.q_in_connect_intent_configuration

        out["qInConnectIntentConfiguration"] = (
            capo_lex_models_v2.types.q_in_connect_intent_configuration.serialize_json(
                value["q_in_connect_intent_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateIntentRequest:
    out: CreateIntentRequest = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError("CreateIntentRequest.intent_name required")
    if data.get("intentDisplayName") is not None:
        out["intent_display_name"] = data["intentDisplayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parentIntentSignature") is not None:
        out["parent_intent_signature"] = data["parentIntentSignature"]
    if data.get("sampleUtterances") is not None:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sample_utterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    if data.get("dialogCodeHook") is not None:
        import capo_lex_models_v2.types.dialog_code_hook_settings

        out["dialog_code_hook"] = (
            capo_lex_models_v2.types.dialog_code_hook_settings.deserialize_json(
                data["dialogCodeHook"]
            )
        )
    if data.get("fulfillmentCodeHook") is not None:
        import capo_lex_models_v2.types.fulfillment_code_hook_settings

        out["fulfillment_code_hook"] = (
            capo_lex_models_v2.types.fulfillment_code_hook_settings.deserialize_json(
                data["fulfillmentCodeHook"]
            )
        )
    if data.get("intentConfirmationSetting") is not None:
        import capo_lex_models_v2.types.intent_confirmation_setting

        out["intent_confirmation_setting"] = (
            capo_lex_models_v2.types.intent_confirmation_setting.deserialize_json(
                data["intentConfirmationSetting"]
            )
        )
    if data.get("intentClosingSetting") is not None:
        import capo_lex_models_v2.types.intent_closing_setting

        out["intent_closing_setting"] = (
            capo_lex_models_v2.types.intent_closing_setting.deserialize_json(
                data["intentClosingSetting"]
            )
        )
    if data.get("inputContexts") is not None:
        import capo_lex_models_v2.types.input_contexts_list

        out["input_contexts"] = (
            capo_lex_models_v2.types.input_contexts_list.deserialize_json(
                data["inputContexts"]
            )
        )
    if data.get("outputContexts") is not None:
        import capo_lex_models_v2.types.output_contexts_list

        out["output_contexts"] = (
            capo_lex_models_v2.types.output_contexts_list.deserialize_json(
                data["outputContexts"]
            )
        )
    if data.get("kendraConfiguration") is not None:
        import capo_lex_models_v2.types.kendra_configuration

        out["kendra_configuration"] = (
            capo_lex_models_v2.types.kendra_configuration.deserialize_json(
                data["kendraConfiguration"]
            )
        )
    if data.get("initialResponseSetting") is not None:
        import capo_lex_models_v2.types.initial_response_setting

        out["initial_response_setting"] = (
            capo_lex_models_v2.types.initial_response_setting.deserialize_json(
                data["initialResponseSetting"]
            )
        )
    if data.get("qnAIntentConfiguration") is not None:
        import capo_lex_models_v2.types.qn_a_intent_configuration

        out["qn_a_intent_configuration"] = (
            capo_lex_models_v2.types.qn_a_intent_configuration.deserialize_json(
                data["qnAIntentConfiguration"]
            )
        )
    if data.get("qInConnectIntentConfiguration") is not None:
        import capo_lex_models_v2.types.q_in_connect_intent_configuration

        out["q_in_connect_intent_configuration"] = (
            capo_lex_models_v2.types.q_in_connect_intent_configuration.deserialize_json(
                data["qInConnectIntentConfiguration"]
            )
        )
    return out
