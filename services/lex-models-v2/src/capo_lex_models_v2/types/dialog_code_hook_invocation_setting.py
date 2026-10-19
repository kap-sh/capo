"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogCodeHookInvocationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification


class DialogCodeHookInvocationSetting(TypedDict, closed=True):
    enable_code_hook_invocation: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether a Lambda function should be invoked for the dialog.</p>"""
    active: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Determines whether a dialog code hook is used when the intent is activated.</p>"""
    invocation_label: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>A label that indicates the dialog step from which the dialog code hook is happening.</p>"""
    post_code_hook_specification: "capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification.PostDialogCodeHookInvocationSpecification"
    """<p>Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogCodeHookInvocationSetting) -> dict:
    out: dict = {}
    out["enableCodeHookInvocation"] = value["enable_code_hook_invocation"]
    out["active"] = value["active"]
    if "invocation_label" in value:
        out["invocationLabel"] = value["invocation_label"]
    import capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification

    out["postCodeHookSpecification"] = (
        capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification.serialize_json(
            value["post_code_hook_specification"]
        )
    )
    return out


def deserialize_json(data: dict) -> DialogCodeHookInvocationSetting:
    out: DialogCodeHookInvocationSetting = {}  # type: ignore[typeddict-item]
    if data.get("enableCodeHookInvocation") is not None:
        out["enable_code_hook_invocation"] = data["enableCodeHookInvocation"]
    else:
        out["enable_code_hook_invocation"] = False
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = False
    if data.get("invocationLabel") is not None:
        out["invocation_label"] = data["invocationLabel"]
    if data.get("postCodeHookSpecification") is not None:
        import capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification

        out["post_code_hook_specification"] = (
            capo_lex_models_v2.types.post_dialog_code_hook_invocation_specification.deserialize_json(
                data["postCodeHookSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "DialogCodeHookInvocationSetting.post_code_hook_specification required"
        )
    return out
