"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceBotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_bot


class DescribeAppInstanceBotResponse(TypedDict, closed=True):
    app_instance_bot: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_bot.AppInstanceBot"
    ]
    """<p>The detials of the <code>AppInstanceBot</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceBotResponse) -> dict:
    out: dict = {}
    if "app_instance_bot" in value:
        import capo_chime_sdk_identity.types.app_instance_bot

        out["AppInstanceBot"] = (
            capo_chime_sdk_identity.types.app_instance_bot.serialize_json(
                value["app_instance_bot"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceBotResponse:
    out: DescribeAppInstanceBotResponse = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceBot") is not None:
        import capo_chime_sdk_identity.types.app_instance_bot

        out["app_instance_bot"] = (
            capo_chime_sdk_identity.types.app_instance_bot.deserialize_json(
                data["AppInstanceBot"]
            )
        )
    return out


def redact_sensitive(value: DescribeAppInstanceBotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_bot" in value:
        import capo_chime_sdk_identity.types.app_instance_bot

        out["app_instance_bot"] = (
            capo_chime_sdk_identity.types.app_instance_bot.redact_sensitive(
                value["app_instance_bot"]
            )
        )
    return out
