"""Generated from Smithy shape ``com.amazonaws.connect#Preview``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.allowed_user_actions
    import capo_connect.types.post_accept_timeout_config


class Preview(TypedDict, closed=True):
    post_accept_timeout_config: (
        "capo_connect.types.post_accept_timeout_config.PostAcceptTimeoutConfig"
    )
    """<p>Countdown timer configuration after the agent accepted the preview outbound contact.</p>"""
    allowed_user_actions: "capo_connect.types.allowed_user_actions.AllowedUserActions"
    """<p>The actions the agent can perform after accepting the preview outbound contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Preview) -> dict:
    out: dict = {}
    import capo_connect.types.post_accept_timeout_config

    out["PostAcceptTimeoutConfig"] = (
        capo_connect.types.post_accept_timeout_config.serialize_json(
            value["post_accept_timeout_config"]
        )
    )
    import capo_connect.types.allowed_user_actions

    out["AllowedUserActions"] = capo_connect.types.allowed_user_actions.serialize_json(
        value["allowed_user_actions"]
    )
    return out


def deserialize_json(data: dict) -> Preview:
    out: Preview = {}  # type: ignore[typeddict-item]
    if data.get("PostAcceptTimeoutConfig") is not None:
        import capo_connect.types.post_accept_timeout_config

        out["post_accept_timeout_config"] = (
            capo_connect.types.post_accept_timeout_config.deserialize_json(
                data["PostAcceptTimeoutConfig"]
            )
        )
    else:
        raise DeserializationError("Preview.post_accept_timeout_config required")
    if data.get("AllowedUserActions") is not None:
        import capo_connect.types.allowed_user_actions

        out["allowed_user_actions"] = (
            capo_connect.types.allowed_user_actions.deserialize_json(
                data["AllowedUserActions"]
            )
        )
    else:
        out["allowed_user_actions"] = []
    return out
