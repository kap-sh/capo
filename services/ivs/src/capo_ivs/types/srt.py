"""Generated from Smithy shape ``com.amazonaws.ivs#Srt``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.srt_endpoint
    import capo_ivs.types.srt_passphrase


class Srt(TypedDict, closed=True):
    endpoint: NotRequired["capo_ivs.types.srt_endpoint.SrtEndpoint"]
    """<p>The endpoint to be used when streaming with IVS using the SRT protocol.</p>"""
    passphrase: NotRequired["capo_ivs.types.srt_passphrase.SrtPassphrase"]
    """<p>Auto-generated passphrase to enable encryption. This field is applicable only if the end user has <i>not</i> enabled the <code>insecureIngest</code> option for the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Srt) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "passphrase" in value:
        out["passphrase"] = value["passphrase"]
    return out


def deserialize_json(data: dict) -> Srt:
    out: Srt = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("passphrase") is not None:
        out["passphrase"] = data["passphrase"]
    return out


def redact_sensitive(value: Srt) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "passphrase" in value:
        out["passphrase"] = "*** Sensitive Data Redacted ***"
    return out
