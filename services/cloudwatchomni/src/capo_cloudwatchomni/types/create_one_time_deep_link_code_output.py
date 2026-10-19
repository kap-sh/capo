"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateOneTimeDeepLinkCodeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.deep_link_code
    import capo_cloudwatchomni.types.deep_link_url


class CreateOneTimeDeepLinkCodeOutput(TypedDict, closed=True):
    code: "capo_cloudwatchomni.types.deep_link_code.DeepLinkCode"
    """The one-time deep-link code."""
    deep_link_url: "capo_cloudwatchomni.types.deep_link_url.DeepLinkUrl"
    """The deep-link URL containing the one-time code."""
    expires_at: "datetime.datetime"
    """The timestamp when the code expires."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateOneTimeDeepLinkCodeOutput) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["deepLinkUrl"] = value["deep_link_url"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["expiresAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["expires_at"]
    )
    return out


def deserialize_cbor(data: dict) -> CreateOneTimeDeepLinkCodeOutput:
    out: CreateOneTimeDeepLinkCodeOutput = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("deepLinkUrl") is not None:
        out["deep_link_url"] = data["deepLinkUrl"]
    else:
        out["deep_link_url"] = ""
    if data.get("expiresAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["expires_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["expiresAt"]
            )
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: CreateOneTimeDeepLinkCodeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    if "deep_link_url" in value:
        out["deep_link_url"] = "*** Sensitive Data Redacted ***"
    return out
