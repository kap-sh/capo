"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateOneTimeDeepLinkCodeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError

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
        raise DeserializationError("CreateOneTimeDeepLinkCodeOutput.code required")
    if data.get("deepLinkUrl") is not None:
        out["deep_link_url"] = data["deepLinkUrl"]
    else:
        raise DeserializationError(
            "CreateOneTimeDeepLinkCodeOutput.deep_link_url required"
        )
    if data.get("expiresAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["expires_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["expiresAt"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOneTimeDeepLinkCodeOutput.expires_at required"
        )
    return out


def redact_sensitive(value: CreateOneTimeDeepLinkCodeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    if "deep_link_url" in value:
        out["deep_link_url"] = "*** Sensitive Data Redacted ***"
    return out
