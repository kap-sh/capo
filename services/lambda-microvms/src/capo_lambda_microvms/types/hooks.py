"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Hooks``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_hooks
    import capo_lambda_microvms.types.microvm_image_hooks


class Hooks(TypedDict, closed=True):
    port: NotRequired["int"]
    """<p>The port number on which the hooks listener runs.</p>"""
    microvm_hooks: NotRequired["capo_lambda_microvms.types.microvm_hooks.MicrovmHooks"]
    """<p>The lifecycle hooks for MicroVM events.</p>"""
    microvm_image_hooks: NotRequired[
        "capo_lambda_microvms.types.microvm_image_hooks.MicrovmImageHooks"
    ]
    """<p>The hooks for MicroVM image build events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hooks) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    if "microvm_hooks" in value:
        import capo_lambda_microvms.types.microvm_hooks

        out["microvmHooks"] = capo_lambda_microvms.types.microvm_hooks.serialize_json(
            value["microvm_hooks"]
        )
    if "microvm_image_hooks" in value:
        import capo_lambda_microvms.types.microvm_image_hooks

        out["microvmImageHooks"] = (
            capo_lambda_microvms.types.microvm_image_hooks.serialize_json(
                value["microvm_image_hooks"]
            )
        )
    return out


def deserialize_json(data: dict) -> Hooks:
    out: Hooks = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("microvmHooks") is not None:
        import capo_lambda_microvms.types.microvm_hooks

        out["microvm_hooks"] = (
            capo_lambda_microvms.types.microvm_hooks.deserialize_json(
                data["microvmHooks"]
            )
        )
    if data.get("microvmImageHooks") is not None:
        import capo_lambda_microvms.types.microvm_image_hooks

        out["microvm_image_hooks"] = (
            capo_lambda_microvms.types.microvm_image_hooks.deserialize_json(
                data["microvmImageHooks"]
            )
        )
    return out
