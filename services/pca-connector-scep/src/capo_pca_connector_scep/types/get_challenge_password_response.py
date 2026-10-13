"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetChallengePasswordResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.sensitive_string


class GetChallengePasswordResponse(TypedDict, closed=True):
    password: NotRequired[
        "capo_pca_connector_scep.types.sensitive_string.SensitiveString"
    ]
    """<p>The SCEP challenge password.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChallengePasswordResponse) -> dict:
    out: dict = {}
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> GetChallengePasswordResponse:
    out: GetChallengePasswordResponse = {}  # type: ignore[typeddict-item]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out


def redact_sensitive(value: GetChallengePasswordResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
