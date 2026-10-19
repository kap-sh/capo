"""Generated from Smithy shape ``com.amazonaws.chime#CreateBotRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.sensitive_string


class CreateBotRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    display_name: "capo_chime.types.sensitive_string.SensitiveString"
    """<p>The bot display name.</p>"""
    domain: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The domain of the Amazon Chime Enterprise account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotRequest) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> CreateBotRequest:
    out: CreateBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    else:
        out["display_name"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    return out


def redact_sensitive(value: CreateBotRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
