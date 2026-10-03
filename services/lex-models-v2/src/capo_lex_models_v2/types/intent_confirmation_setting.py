"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentConfirmationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.conditional_specification
    import capo_lex_models_v2.types.dialog_code_hook_invocation_setting
    import capo_lex_models_v2.types.dialog_state
    import capo_lex_models_v2.types.elicitation_code_hook_invocation_setting
    import capo_lex_models_v2.types.prompt_specification
    import capo_lex_models_v2.types.response_specification


class IntentConfirmationSetting(TypedDict, closed=True):
    prompt_specification: (
        "capo_lex_models_v2.types.prompt_specification.PromptSpecification"
    )
    """<p>Prompts the user to confirm the intent. This question should have a yes or no answer.</p> <p>Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the <code>OrderPizza</code> intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information. </p>"""
    declination_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    """<p>When the user answers "no" to the question defined in <code>promptSpecification</code>, Amazon Lex responds with this response to acknowledge that the intent was canceled. </p>"""
    active: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the intent's confirmation is sent to the user. When this field is false, confirmation and declination responses aren't sent. If the <code>active</code> field isn't specified, the default is true.</p>"""
    confirmation_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    confirmation_next_step: NotRequired[
        "capo_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot executes when the customer confirms the intent.</p>"""
    confirmation_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the intent is closed.</p>"""
    declination_next_step: NotRequired[
        "capo_lex_models_v2.types.dialog_state.DialogState"
    ]
    """<p>Specifies the next step that the bot executes when the customer declines the intent.</p>"""
    declination_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the intent is declined.</p>"""
    failure_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    failure_next_step: NotRequired["capo_lex_models_v2.types.dialog_state.DialogState"]
    """<p>The next step to take in the conversation if the confirmation step fails.</p>"""
    failure_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    code_hook: NotRequired[
        "capo_lex_models_v2.types.dialog_code_hook_invocation_setting.DialogCodeHookInvocationSetting"
    ]
    """<p>The <code>DialogCodeHookInvocationSetting</code> object associated with intent's confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is <code>InvokeDialogCodeHook</code>. </p>"""
    elicitation_code_hook: NotRequired[
        "capo_lex_models_v2.types.elicitation_code_hook_invocation_setting.ElicitationCodeHookInvocationSetting"
    ]
    """<p>The <code>DialogCodeHookInvocationSetting</code> used when the code hook is invoked during confirmation prompt retries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentConfirmationSetting) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.prompt_specification

    out["promptSpecification"] = (
        capo_lex_models_v2.types.prompt_specification.serialize_json(
            value["prompt_specification"]
        )
    )
    if "declination_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["declinationResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["declination_response"]
            )
        )
    if "active" in value:
        out["active"] = value["active"]
    if "confirmation_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["confirmationResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["confirmation_response"]
            )
        )
    if "confirmation_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["confirmationNextStep"] = (
            capo_lex_models_v2.types.dialog_state.serialize_json(
                value["confirmation_next_step"]
            )
        )
    if "confirmation_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["confirmationConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["confirmation_conditional"]
            )
        )
    if "declination_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["declinationNextStep"] = (
            capo_lex_models_v2.types.dialog_state.serialize_json(
                value["declination_next_step"]
            )
        )
    if "declination_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["declinationConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["declination_conditional"]
            )
        )
    if "failure_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["failureResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["failure_response"]
            )
        )
    if "failure_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["failureNextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
            value["failure_next_step"]
        )
    if "failure_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["failureConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["failure_conditional"]
            )
        )
    if "code_hook" in value:
        import capo_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["codeHook"] = (
            capo_lex_models_v2.types.dialog_code_hook_invocation_setting.serialize_json(
                value["code_hook"]
            )
        )
    if "elicitation_code_hook" in value:
        import capo_lex_models_v2.types.elicitation_code_hook_invocation_setting

        out["elicitationCodeHook"] = (
            capo_lex_models_v2.types.elicitation_code_hook_invocation_setting.serialize_json(
                value["elicitation_code_hook"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntentConfirmationSetting:
    out: IntentConfirmationSetting = {}  # type: ignore[typeddict-item]
    if data.get("promptSpecification") is not None:
        import capo_lex_models_v2.types.prompt_specification

        out["prompt_specification"] = (
            capo_lex_models_v2.types.prompt_specification.deserialize_json(
                data["promptSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "IntentConfirmationSetting.prompt_specification required"
        )
    if data.get("declinationResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["declination_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["declinationResponse"]
            )
        )
    if data.get("active") is not None:
        out["active"] = data["active"]
    if data.get("confirmationResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["confirmation_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["confirmationResponse"]
            )
        )
    if data.get("confirmationNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["confirmation_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["confirmationNextStep"]
            )
        )
    if data.get("confirmationConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["confirmation_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["confirmationConditional"]
            )
        )
    if data.get("declinationNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["declination_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["declinationNextStep"]
            )
        )
    if data.get("declinationConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["declination_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["declinationConditional"]
            )
        )
    if data.get("failureResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["failure_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["failureResponse"]
            )
        )
    if data.get("failureNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["failure_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["failureNextStep"]
            )
        )
    if data.get("failureConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["failure_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["failureConditional"]
            )
        )
    if data.get("codeHook") is not None:
        import capo_lex_models_v2.types.dialog_code_hook_invocation_setting

        out["code_hook"] = (
            capo_lex_models_v2.types.dialog_code_hook_invocation_setting.deserialize_json(
                data["codeHook"]
            )
        )
    if data.get("elicitationCodeHook") is not None:
        import capo_lex_models_v2.types.elicitation_code_hook_invocation_setting

        out["elicitation_code_hook"] = (
            capo_lex_models_v2.types.elicitation_code_hook_invocation_setting.deserialize_json(
                data["elicitationCodeHook"]
            )
        )
    return out
