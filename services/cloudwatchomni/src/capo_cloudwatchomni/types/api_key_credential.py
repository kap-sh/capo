"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ApiKeyCredential``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.sensitive_string


class ApiKeyCredential(TypedDict, closed=True):
    api_key_value: "capo_cloudwatchomni.types.sensitive_string.SensitiveString"
    """The API key value used to authenticate with the external system."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApiKeyCredential) -> dict:
    out: dict = {}
    out["apiKeyValue"] = value["api_key_value"]
    return out


def deserialize_cbor(data: dict) -> ApiKeyCredential:
    out: ApiKeyCredential = {}  # type: ignore[typeddict-item]
    if data.get("apiKeyValue") is not None:
        out["api_key_value"] = data["apiKeyValue"]
    else:
        out["api_key_value"] = ""
    return out
