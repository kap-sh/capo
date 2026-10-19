"""Generated from Smithy shape ``com.amazonaws.quicksight#WebProxyCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.db_username
    import capo_quicksight.types.password


class WebProxyCredentials(TypedDict, closed=True):
    web_proxy_username: "capo_quicksight.types.db_username.DbUsername"
    """<p>The username for authenticating with the web proxy server.</p>"""
    web_proxy_password: "capo_quicksight.types.password.Password"
    """<p>The password for authenticating with the web proxy server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebProxyCredentials) -> dict:
    out: dict = {}
    out["WebProxyUsername"] = value["web_proxy_username"]
    out["WebProxyPassword"] = value["web_proxy_password"]
    return out


def deserialize_json(data: dict) -> WebProxyCredentials:
    out: WebProxyCredentials = {}  # type: ignore[typeddict-item]
    if data.get("WebProxyUsername") is not None:
        out["web_proxy_username"] = data["WebProxyUsername"]
    else:
        out["web_proxy_username"] = ""
    if data.get("WebProxyPassword") is not None:
        out["web_proxy_password"] = data["WebProxyPassword"]
    else:
        out["web_proxy_password"] = ""
    return out
