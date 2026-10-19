"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserActionResult``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.key_press_result
    import capo_bedrock_agentcore.types.key_shortcut_result
    import capo_bedrock_agentcore.types.key_type_result
    import capo_bedrock_agentcore.types.mouse_click_result
    import capo_bedrock_agentcore.types.mouse_drag_result
    import capo_bedrock_agentcore.types.mouse_move_result
    import capo_bedrock_agentcore.types.mouse_scroll_result
    import capo_bedrock_agentcore.types.screenshot_result


class _BrowserActionResult_mouseClick(TypedDict, closed=True):
    mouseClick: "capo_bedrock_agentcore.types.mouse_click_result.MouseClickResult"


class _BrowserActionResult_mouseMove(TypedDict, closed=True):
    mouseMove: "capo_bedrock_agentcore.types.mouse_move_result.MouseMoveResult"


class _BrowserActionResult_mouseDrag(TypedDict, closed=True):
    mouseDrag: "capo_bedrock_agentcore.types.mouse_drag_result.MouseDragResult"


class _BrowserActionResult_mouseScroll(TypedDict, closed=True):
    mouseScroll: "capo_bedrock_agentcore.types.mouse_scroll_result.MouseScrollResult"


class _BrowserActionResult_keyType(TypedDict, closed=True):
    keyType: "capo_bedrock_agentcore.types.key_type_result.KeyTypeResult"


class _BrowserActionResult_keyPress(TypedDict, closed=True):
    keyPress: "capo_bedrock_agentcore.types.key_press_result.KeyPressResult"


class _BrowserActionResult_keyShortcut(TypedDict, closed=True):
    keyShortcut: "capo_bedrock_agentcore.types.key_shortcut_result.KeyShortcutResult"


class _BrowserActionResult_screenshot(TypedDict, closed=True):
    screenshot: "capo_bedrock_agentcore.types.screenshot_result.ScreenshotResult"


BrowserActionResult: TypeAlias = (
    _BrowserActionResult_mouseClick
    | _BrowserActionResult_mouseMove
    | _BrowserActionResult_mouseDrag
    | _BrowserActionResult_mouseScroll
    | _BrowserActionResult_keyType
    | _BrowserActionResult_keyPress
    | _BrowserActionResult_keyShortcut
    | _BrowserActionResult_screenshot
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BrowserActionResult) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"BrowserActionResult: cannot serialize unknown variant {value.name!r}"
        )
    elif "mouseClick" in value:
        import capo_bedrock_agentcore.types.mouse_click_result

        return {
            "mouseClick": capo_bedrock_agentcore.types.mouse_click_result.serialize_json(
                value["mouseClick"]
            )
        }
    elif "mouseMove" in value:
        import capo_bedrock_agentcore.types.mouse_move_result

        return {
            "mouseMove": capo_bedrock_agentcore.types.mouse_move_result.serialize_json(
                value["mouseMove"]
            )
        }
    elif "mouseDrag" in value:
        import capo_bedrock_agentcore.types.mouse_drag_result

        return {
            "mouseDrag": capo_bedrock_agentcore.types.mouse_drag_result.serialize_json(
                value["mouseDrag"]
            )
        }
    elif "mouseScroll" in value:
        import capo_bedrock_agentcore.types.mouse_scroll_result

        return {
            "mouseScroll": capo_bedrock_agentcore.types.mouse_scroll_result.serialize_json(
                value["mouseScroll"]
            )
        }
    elif "keyType" in value:
        import capo_bedrock_agentcore.types.key_type_result

        return {
            "keyType": capo_bedrock_agentcore.types.key_type_result.serialize_json(
                value["keyType"]
            )
        }
    elif "keyPress" in value:
        import capo_bedrock_agentcore.types.key_press_result

        return {
            "keyPress": capo_bedrock_agentcore.types.key_press_result.serialize_json(
                value["keyPress"]
            )
        }
    elif "keyShortcut" in value:
        import capo_bedrock_agentcore.types.key_shortcut_result

        return {
            "keyShortcut": capo_bedrock_agentcore.types.key_shortcut_result.serialize_json(
                value["keyShortcut"]
            )
        }
    elif "screenshot" in value:
        import capo_bedrock_agentcore.types.screenshot_result

        return {
            "screenshot": capo_bedrock_agentcore.types.screenshot_result.serialize_json(
                value["screenshot"]
            )
        }
    else:
        raise SerializationError("BrowserActionResult: no variant present")


def deserialize_json(data: dict) -> BrowserActionResult:
    if data.get("mouseClick") is not None:
        import capo_bedrock_agentcore.types.mouse_click_result

        return {
            "mouseClick": capo_bedrock_agentcore.types.mouse_click_result.deserialize_json(
                data["mouseClick"]
            )
        }
    elif data.get("mouseMove") is not None:
        import capo_bedrock_agentcore.types.mouse_move_result

        return {
            "mouseMove": capo_bedrock_agentcore.types.mouse_move_result.deserialize_json(
                data["mouseMove"]
            )
        }
    elif data.get("mouseDrag") is not None:
        import capo_bedrock_agentcore.types.mouse_drag_result

        return {
            "mouseDrag": capo_bedrock_agentcore.types.mouse_drag_result.deserialize_json(
                data["mouseDrag"]
            )
        }
    elif data.get("mouseScroll") is not None:
        import capo_bedrock_agentcore.types.mouse_scroll_result

        return {
            "mouseScroll": capo_bedrock_agentcore.types.mouse_scroll_result.deserialize_json(
                data["mouseScroll"]
            )
        }
    elif data.get("keyType") is not None:
        import capo_bedrock_agentcore.types.key_type_result

        return {
            "keyType": capo_bedrock_agentcore.types.key_type_result.deserialize_json(
                data["keyType"]
            )
        }
    elif data.get("keyPress") is not None:
        import capo_bedrock_agentcore.types.key_press_result

        return {
            "keyPress": capo_bedrock_agentcore.types.key_press_result.deserialize_json(
                data["keyPress"]
            )
        }
    elif data.get("keyShortcut") is not None:
        import capo_bedrock_agentcore.types.key_shortcut_result

        return {
            "keyShortcut": capo_bedrock_agentcore.types.key_shortcut_result.deserialize_json(
                data["keyShortcut"]
            )
        }
    elif data.get("screenshot") is not None:
        import capo_bedrock_agentcore.types.screenshot_result

        return {
            "screenshot": capo_bedrock_agentcore.types.screenshot_result.deserialize_json(
                data["screenshot"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("BrowserActionResult: no recognized variant key")
