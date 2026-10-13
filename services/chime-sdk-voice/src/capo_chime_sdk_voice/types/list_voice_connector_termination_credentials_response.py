"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorTerminationCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_string_list


class ListVoiceConnectorTerminationCredentialsResponse(TypedDict, closed=True):
    usernames: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>A list of user names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorTerminationCredentialsResponse) -> dict:
    out: dict = {}
    if "usernames" in value:
        import capo_chime_sdk_voice.types.sensitive_string_list

        out["Usernames"] = (
            capo_chime_sdk_voice.types.sensitive_string_list.serialize_json(
                value["usernames"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorTerminationCredentialsResponse:
    out: ListVoiceConnectorTerminationCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Usernames") is not None:
        import capo_chime_sdk_voice.types.sensitive_string_list

        out["usernames"] = (
            capo_chime_sdk_voice.types.sensitive_string_list.deserialize_json(
                data["Usernames"]
            )
        )
    return out


def redact_sensitive(
    value: ListVoiceConnectorTerminationCredentialsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "usernames" in value:
        import capo_chime_sdk_voice.types.sensitive_string_list

        out["usernames"] = (
            capo_chime_sdk_voice.types.sensitive_string_list.redact_sensitive(
                value["usernames"]
            )
        )
    return out
