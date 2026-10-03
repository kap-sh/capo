"""Generated from Smithy shape ``com.amazonaws.iot#HttpAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.sig_v4_authorization


class HttpAuthorization(TypedDict, closed=True):
    sigv4: NotRequired["capo_iot.types.sig_v4_authorization.SigV4Authorization"]
    """<p>Use Sig V4 authorization. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 Signing Process</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpAuthorization) -> dict:
    out: dict = {}
    if "sigv4" in value:
        import capo_iot.types.sig_v4_authorization

        out["sigv4"] = capo_iot.types.sig_v4_authorization.serialize_json(
            value["sigv4"]
        )
    return out


def deserialize_json(data: dict) -> HttpAuthorization:
    out: HttpAuthorization = {}  # type: ignore[typeddict-item]
    if data.get("sigv4") is not None:
        import capo_iot.types.sig_v4_authorization

        out["sigv4"] = capo_iot.types.sig_v4_authorization.deserialize_json(
            data["sigv4"]
        )
    return out
