"""Generated from Smithy shape ``com.amazonaws.organizations#CancelHandshakeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake


class CancelHandshakeResponse(TypedDict, closed=True):
    handshake: NotRequired["capo_organizations.types.handshake.Handshake"]
    """<p>A <code>Handshake</code> object. Contains for the handshake that you canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelHandshakeResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["Handshake"] = capo_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelHandshakeResponse:
    out: CancelHandshakeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Handshake") is not None:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.deserialize_aws_json_1_1(
            data["Handshake"]
        )
    return out


def redact_sensitive(value: CancelHandshakeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.redact_sensitive(
            value["handshake"]
        )
    return out
