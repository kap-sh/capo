"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.key_press_arguments
    import capo_bedrock_agentcore.types.key_shortcut_arguments
    import capo_bedrock_agentcore.types.key_type_arguments
    import capo_bedrock_agentcore.types.mouse_click_arguments
    import capo_bedrock_agentcore.types.mouse_drag_arguments
    import capo_bedrock_agentcore.types.mouse_move_arguments
    import capo_bedrock_agentcore.types.mouse_scroll_arguments
    import capo_bedrock_agentcore.types.screenshot_arguments


class _BrowserAction_mouseClick(TypedDict, closed=True):
    mouseClick: "capo_bedrock_agentcore.types.mouse_click_arguments.MouseClickArguments"


class _BrowserAction_mouseMove(TypedDict, closed=True):
    mouseMove: "capo_bedrock_agentcore.types.mouse_move_arguments.MouseMoveArguments"


class _BrowserAction_mouseDrag(TypedDict, closed=True):
    mouseDrag: "capo_bedrock_agentcore.types.mouse_drag_arguments.MouseDragArguments"


class _BrowserAction_mouseScroll(TypedDict, closed=True):
    mouseScroll: (
        "capo_bedrock_agentcore.types.mouse_scroll_arguments.MouseScrollArguments"
    )


class _BrowserAction_keyType(TypedDict, closed=True):
    keyType: "capo_bedrock_agentcore.types.key_type_arguments.KeyTypeArguments"


class _BrowserAction_keyPress(TypedDict, closed=True):
    keyPress: "capo_bedrock_agentcore.types.key_press_arguments.KeyPressArguments"


class _BrowserAction_keyShortcut(TypedDict, closed=True):
    keyShortcut: (
        "capo_bedrock_agentcore.types.key_shortcut_arguments.KeyShortcutArguments"
    )


class _BrowserAction_screenshot(TypedDict, closed=True):
    screenshot: "capo_bedrock_agentcore.types.screenshot_arguments.ScreenshotArguments"


BrowserAction: TypeAlias = (
    _BrowserAction_mouseClick
    | _BrowserAction_mouseMove
    | _BrowserAction_mouseDrag
    | _BrowserAction_mouseScroll
    | _BrowserAction_keyType
    | _BrowserAction_keyPress
    | _BrowserAction_keyShortcut
    | _BrowserAction_screenshot
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BrowserAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BrowserAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "mouseClick" in value:
        import capo_bedrock_agentcore.types.mouse_click_arguments

        return {
            "mouseClick": capo_bedrock_agentcore.types.mouse_click_arguments.serialize_json(
                value["mouseClick"]
            )
        }
    elif "mouseMove" in value:
        import capo_bedrock_agentcore.types.mouse_move_arguments

        return {
            "mouseMove": capo_bedrock_agentcore.types.mouse_move_arguments.serialize_json(
                value["mouseMove"]
            )
        }
    elif "mouseDrag" in value:
        import capo_bedrock_agentcore.types.mouse_drag_arguments

        return {
            "mouseDrag": capo_bedrock_agentcore.types.mouse_drag_arguments.serialize_json(
                value["mouseDrag"]
            )
        }
    elif "mouseScroll" in value:
        import capo_bedrock_agentcore.types.mouse_scroll_arguments

        return {
            "mouseScroll": capo_bedrock_agentcore.types.mouse_scroll_arguments.serialize_json(
                value["mouseScroll"]
            )
        }
    elif "keyType" in value:
        import capo_bedrock_agentcore.types.key_type_arguments

        return {
            "keyType": capo_bedrock_agentcore.types.key_type_arguments.serialize_json(
                value["keyType"]
            )
        }
    elif "keyPress" in value:
        import capo_bedrock_agentcore.types.key_press_arguments

        return {
            "keyPress": capo_bedrock_agentcore.types.key_press_arguments.serialize_json(
                value["keyPress"]
            )
        }
    elif "keyShortcut" in value:
        import capo_bedrock_agentcore.types.key_shortcut_arguments

        return {
            "keyShortcut": capo_bedrock_agentcore.types.key_shortcut_arguments.serialize_json(
                value["keyShortcut"]
            )
        }
    elif "screenshot" in value:
        import capo_bedrock_agentcore.types.screenshot_arguments

        return {
            "screenshot": capo_bedrock_agentcore.types.screenshot_arguments.serialize_json(
                value["screenshot"]
            )
        }
    else:
        raise SerializationError("BrowserAction: no variant present")


def deserialize_json(data: dict) -> BrowserAction:
    if data.get("mouseClick") is not None:
        import capo_bedrock_agentcore.types.mouse_click_arguments

        return {
            "mouseClick": capo_bedrock_agentcore.types.mouse_click_arguments.deserialize_json(
                data["mouseClick"]
            )
        }
    elif data.get("mouseMove") is not None:
        import capo_bedrock_agentcore.types.mouse_move_arguments

        return {
            "mouseMove": capo_bedrock_agentcore.types.mouse_move_arguments.deserialize_json(
                data["mouseMove"]
            )
        }
    elif data.get("mouseDrag") is not None:
        import capo_bedrock_agentcore.types.mouse_drag_arguments

        return {
            "mouseDrag": capo_bedrock_agentcore.types.mouse_drag_arguments.deserialize_json(
                data["mouseDrag"]
            )
        }
    elif data.get("mouseScroll") is not None:
        import capo_bedrock_agentcore.types.mouse_scroll_arguments

        return {
            "mouseScroll": capo_bedrock_agentcore.types.mouse_scroll_arguments.deserialize_json(
                data["mouseScroll"]
            )
        }
    elif data.get("keyType") is not None:
        import capo_bedrock_agentcore.types.key_type_arguments

        return {
            "keyType": capo_bedrock_agentcore.types.key_type_arguments.deserialize_json(
                data["keyType"]
            )
        }
    elif data.get("keyPress") is not None:
        import capo_bedrock_agentcore.types.key_press_arguments

        return {
            "keyPress": capo_bedrock_agentcore.types.key_press_arguments.deserialize_json(
                data["keyPress"]
            )
        }
    elif data.get("keyShortcut") is not None:
        import capo_bedrock_agentcore.types.key_shortcut_arguments

        return {
            "keyShortcut": capo_bedrock_agentcore.types.key_shortcut_arguments.deserialize_json(
                data["keyShortcut"]
            )
        }
    elif data.get("screenshot") is not None:
        import capo_bedrock_agentcore.types.screenshot_arguments

        return {
            "screenshot": capo_bedrock_agentcore.types.screenshot_arguments.deserialize_json(
                data["screenshot"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BrowserAction: no recognized variant key")
