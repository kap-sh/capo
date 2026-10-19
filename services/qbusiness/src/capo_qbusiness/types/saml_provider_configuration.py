"""Generated from Smithy shape ``com.amazonaws.qbusiness#SamlProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.saml_authentication_url


class SamlProviderConfiguration(TypedDict, closed=True):
    authentication_url: (
        "capo_qbusiness.types.saml_authentication_url.SamlAuthenticationUrl"
    )
    """<p>The URL where Amazon Q Business end users will be redirected for authentication. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamlProviderConfiguration) -> dict:
    out: dict = {}
    out["authenticationUrl"] = value["authentication_url"]
    return out


def deserialize_json(data: dict) -> SamlProviderConfiguration:
    out: SamlProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authenticationUrl") is not None:
        out["authentication_url"] = data["authenticationUrl"]
    else:
        out["authentication_url"] = ""
    return out
