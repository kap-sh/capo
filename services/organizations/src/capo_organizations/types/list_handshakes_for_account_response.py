"""Generated from Smithy shape ``com.amazonaws.organizations#ListHandshakesForAccountResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshakes
    import capo_organizations.types.next_token


class ListHandshakesForAccountResponse(TypedDict, closed=True):
    handshakes: NotRequired["capo_organizations.types.handshakes.Handshakes"]
    """<p>An array of <code>Handshake</code>objects. Contains details for a handshake.</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHandshakesForAccountResponse) -> dict:
    out: dict = {}
    if "handshakes" in value:
        import capo_organizations.types.handshakes

        out["Handshakes"] = capo_organizations.types.handshakes.serialize_aws_json_1_1(
            value["handshakes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHandshakesForAccountResponse:
    out: ListHandshakesForAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("Handshakes") is not None:
        import capo_organizations.types.handshakes

        out["handshakes"] = (
            capo_organizations.types.handshakes.deserialize_aws_json_1_1(
                data["Handshakes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListHandshakesForAccountResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "handshakes" in value:
        import capo_organizations.types.handshakes

        out["handshakes"] = capo_organizations.types.handshakes.redact_sensitive(
            value["handshakes"]
        )
    return out
