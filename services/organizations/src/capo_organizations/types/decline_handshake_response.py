"""Generated from Smithy shape ``com.amazonaws.organizations#DeclineHandshakeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake


class DeclineHandshakeResponse(TypedDict, closed=True):
    handshake: NotRequired["capo_organizations.types.handshake.Handshake"]
    """<p>A <code>Handshake</code> object. Contains details for the declined handshake.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeclineHandshakeResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["Handshake"] = capo_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeclineHandshakeResponse:
    out: DeclineHandshakeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Handshake") is not None:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.deserialize_aws_json_1_1(
            data["Handshake"]
        )
    return out


def redact_sensitive(value: DeclineHandshakeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.redact_sensitive(
            value["handshake"]
        )
    return out
