"""Generated from Smithy shape ``com.amazonaws.redshift#GetIdentityCenterAuthTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.t_stamp


class GetIdentityCenterAuthTokenResponse(TypedDict, closed=True):
    token: NotRequired["capo_redshift.types.sensitive_string.SensitiveString"]
    """<p>The encrypted authentication token containing the caller's Amazon Web Services IAM Identity Center identity information. This token is encrypted using Key Management Service and can only be decrypted by the specified Amazon Redshift clusters. Use this token with Amazon Redshift drivers to authenticate using your Amazon Web Services IAM Identity Center identity.</p>"""
    expiration_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The time (UTC) when the token expires. After this timestamp, the token will no longer be valid for authentication.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityCenterAuthTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "token" in value:
        pairs.append((f"{key_prefix}Token", str(value["token"])))
    if "expiration_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["expiration_time"], pairs, f"{key_prefix}ExpirationTime"
        )


def deserialize_query(el: Element) -> GetIdentityCenterAuthTokenResponse:
    out: GetIdentityCenterAuthTokenResponse = {}  # type: ignore[typeddict-item]
    child_token = el.find("Token")
    if child_token is not None:
        out["token"] = str(child_token.text or "")
    child_expiration_time = el.find("ExpirationTime")
    if child_expiration_time is not None:
        import capo_redshift.types.t_stamp

        out["expiration_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_expiration_time
        )
    return out


def redact_sensitive(value: GetIdentityCenterAuthTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
