"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateIntentRequest``."""

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
    import capo_lex_models_v2.types.slot_priorities_list


class UpdateIntentRequest(TypedDict, closed=True):
    intent_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the intent to update.</p>"""
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The new name for the intent.</p>"""
    intent_display_name: NotRequired[
        "capo_lex_models_v2.types.display_name.DisplayName"
    ]
    """<p>The new display name for the intent.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The new description of the intent.</p>"""
    parent_intent_signature: NotRequired[
        "capo_lex_models_v2.types.intent_signature.IntentSignature"
    ]
    """<p>The signature of the new built-in intent to use as the parent of this intent.</p>"""
    sample_utterances: NotRequired[
        "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>New utterances used to invoke the intent.</p>"""
    dialog_code_hook: NotRequired[
        "capo_lex_models_v2.types.dialog_code_hook_settings.DialogCodeHookSettings"
    ]
    """<p>The new Lambda function to use between each turn of the conversation with the bot.</p>"""
    fulfillment_code_hook: NotRequired[
        "capo_lex_models_v2.types.fulfillment_code_hook_settings.FulfillmentCodeHookSettings"
    ]
    """<p>The new Lambda function to call when all of the intents required slots are provided and the intent is ready for fulfillment.</p>"""
    slot_priorities: NotRequired[
        "capo_lex_models_v2.types.slot_priorities_list.SlotPrioritiesList"
    ]
    """<p>A new list of slots and their priorities that are contained by the intent.</p>"""
    intent_confirmation_setting: NotRequired[
        "capo_lex_models_v2.types.intent_confirmation_setting.IntentConfirmationSetting"
    ]
    """<p>New prompts that Amazon Lex sends to the user to confirm the completion of an intent.</p>"""
    intent_closing_setting: NotRequired[
        "capo_lex_models_v2.types.intent_closing_setting.IntentClosingSetting"
    ]
    """<p>The new response that Amazon Lex sends the user when the intent is closed.</p>"""
    input_contexts: NotRequired[
        "capo_lex_models_v2.types.input_contexts_list.InputContextsList"
    ]
    """<p>A new list of contexts that must be active in order for Amazon Lex to consider the intent.</p>"""
    output_contexts: NotRequired[
        "capo_lex_models_v2.types.output_contexts_list.OutputContextsList"
    ]
    """<p>A new list of contexts that Amazon Lex activates when the intent is fulfilled.</p>"""
    kendra_configuration: NotRequired[
        "capo_lex_models_v2.types.kendra_configuration.KendraConfiguration"
    ]
    """<p>New configuration settings for connecting to an Amazon Kendra index.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot that contains the intent.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the intent. Must be <code>DRAFT</code>.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    initial_response_setting: NotRequired[
        "capo_lex_models_v2.types.initial_response_setting.InitialResponseSetting"
    ]
    """<p>Configuration settings for a response sent to the user before Amazon Lex starts eliciting slots.</p>"""
    qn_a_intent_configuration: NotRequired[
        "capo_lex_models_v2.types.qn_a_intent_configuration.QnAIntentConfiguration"
    ]
    """<p>Specifies the configuration of the built-in <code>Amazon.QnAIntent</code>. The <code>AMAZON.QnAIntent</code> intent is called when Amazon Lex can't determine another intent to invoke. If you specify this field, you can't specify the <code>kendraConfiguration</code> field.</p>"""
    q_in_connect_intent_configuration: NotRequired[
        "capo_lex_models_v2.types.q_in_connect_intent_configuration.QInConnectIntentConfiguration"
    ]
    """<p>Qinconnect intent configuration details for the update intent request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntentRequest) -> dict:
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
    if "slot_priorities" in value:
        import capo_lex_models_v2.types.slot_priorities_list

        out["slotPriorities"] = (
            capo_lex_models_v2.types.slot_priorities_list.serialize_json(
                value["slot_priorities"]
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


def deserialize_json(data: dict) -> UpdateIntentRequest:
    out: UpdateIntentRequest = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        raise DeserializationError("UpdateIntentRequest.intent_name required")
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
    if data.get("slotPriorities") is not None:
        import capo_lex_models_v2.types.slot_priorities_list

        out["slot_priorities"] = (
            capo_lex_models_v2.types.slot_priorities_list.deserialize_json(
                data["slotPriorities"]
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
