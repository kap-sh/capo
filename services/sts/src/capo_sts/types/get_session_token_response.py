"""Generated from Smithy shape ``com.amazonaws.sts#GetSessionTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.credentials
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type


class GetSessionTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSessionTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
        )
    if "session_token_utilization" in value:
        pairs.append(
            (
                f"{key_prefix}SessionTokenUtilization",
                str(value["session_token_utilization"]),
            )
        )
    if "session_token_size" in value:
        pairs.append(
            (f"{key_prefix}SessionTokenSize", str(value["session_token_size"]))
        )


def deserialize_query(el: Element) -> GetSessionTokenResponse:
    out: GetSessionTokenResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_session_token_utilization = el.find("SessionTokenUtilization")
    if child_session_token_utilization is not None:
        out["session_token_utilization"] = int(
            child_session_token_utilization.text or ""
        )
    child_session_token_size = el.find("SessionTokenSize")
    if child_session_token_size is not None:
        out["session_token_size"] = int(child_session_token_size.text or "")
    return out


def redact_sensitive(value: GetSessionTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
