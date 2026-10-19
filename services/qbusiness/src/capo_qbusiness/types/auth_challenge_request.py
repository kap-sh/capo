"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.url


class AuthChallengeRequest(TypedDict, closed=True):
    authorization_url: "capo_qbusiness.types.url.Url"
    """<p>The URL sent by Amazon Q Business to the third party authentication server to authenticate a custom plugin user through an OAuth protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeRequest) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> AuthChallengeRequest:
    out: AuthChallengeRequest = {}  # type: ignore[typeddict-item]
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        out["authorization_url"] = ""
    return out
