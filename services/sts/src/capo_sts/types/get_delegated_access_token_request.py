"""Generated from Smithy shape ``com.amazonaws.sts#GetDelegatedAccessTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sts.types.trade_in_token_type


class GetDelegatedAccessTokenRequest(TypedDict, closed=True):
    trade_in_token: "capo_sts.types.trade_in_token_type.tradeInTokenType"
    """<p>The token to exchange for temporary Amazon Web Services credentials. This token must be valid and unexpired at the time of the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDelegatedAccessTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TradeInToken", str(value["trade_in_token"])))


def deserialize_query(el: Element) -> GetDelegatedAccessTokenRequest:
    out: GetDelegatedAccessTokenRequest = {}  # type: ignore[typeddict-item]
    child_trade_in_token = el.find("TradeInToken")
    if child_trade_in_token is not None:
        out["trade_in_token"] = str(child_trade_in_token.text or "")
    else:
        raise DeserializationError(
            "GetDelegatedAccessTokenRequest.trade_in_token required"
        )
    return out


def redact_sensitive(value: GetDelegatedAccessTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "trade_in_token" in value:
        out["trade_in_token"] = "*** Sensitive Data Redacted ***"
    return out
