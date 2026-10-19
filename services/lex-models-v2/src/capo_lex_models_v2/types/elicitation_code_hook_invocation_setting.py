"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ElicitationCodeHookInvocationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.name


class ElicitationCodeHookInvocationSetting(TypedDict, closed=True):
    enable_code_hook_invocation: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether a Lambda function should be invoked for the dialog.</p>"""
    invocation_label: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>A label that indicates the dialog step from which the dialog code hook is happening.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElicitationCodeHookInvocationSetting) -> dict:
    out: dict = {}
    out["enableCodeHookInvocation"] = value["enable_code_hook_invocation"]
    if "invocation_label" in value:
        out["invocationLabel"] = value["invocation_label"]
    return out


def deserialize_json(data: dict) -> ElicitationCodeHookInvocationSetting:
    out: ElicitationCodeHookInvocationSetting = {}  # type: ignore[typeddict-item]
    if data.get("enableCodeHookInvocation") is not None:
        out["enable_code_hook_invocation"] = data["enableCodeHookInvocation"]
    else:
        out["enable_code_hook_invocation"] = False
    if data.get("invocationLabel") is not None:
        out["invocation_label"] = data["invocationLabel"]
    return out
