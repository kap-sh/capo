"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxConnectionStringResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.signed_kx_connection_string


class GetKxConnectionStringResponse(TypedDict, closed=True):
    signed_connection_string: NotRequired[
        "capo_finspace.types.signed_kx_connection_string.SignedKxConnectionString"
    ]
    """<p>The signed connection string that you can use to connect to clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxConnectionStringResponse) -> dict:
    out: dict = {}
    if "signed_connection_string" in value:
        out["signedConnectionString"] = value["signed_connection_string"]
    return out


def deserialize_json(data: dict) -> GetKxConnectionStringResponse:
    out: GetKxConnectionStringResponse = {}  # type: ignore[typeddict-item]
    if data.get("signedConnectionString") is not None:
        out["signed_connection_string"] = data["signedConnectionString"]
    return out


def redact_sensitive(value: GetKxConnectionStringResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "signed_connection_string" in value:
        out["signed_connection_string"] = "*** Sensitive Data Redacted ***"
    return out
