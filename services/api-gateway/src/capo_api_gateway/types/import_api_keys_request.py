"""Generated from Smithy shape ``com.amazonaws.apigateway#ImportApiKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_api_gateway.types.api_keys_format
    import capo_api_gateway.types.blob
    import capo_api_gateway.types.boolean


class ImportApiKeysRequest(TypedDict, closed=True):
    body: "capo_api_gateway.types.blob.Blob"
    """<p>The payload of the POST request to import API keys. For the payload format, see API Key File Format.</p>"""
    format: "capo_api_gateway.types.api_keys_format.ApiKeysFormat"
    """<p>A query parameter to specify the input format to imported API keys. Currently, only the <code>csv</code> format is supported.</p>"""
    fail_on_warnings: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>A query parameter to indicate whether to rollback ApiKey importation (<code>true</code>) or not (<code>false</code>) when error is encountered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportApiKeysRequest) -> dict:
    out: dict = {}
    import capo_api_gateway.types.blob

    out["body"] = capo_api_gateway.types.blob.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> ImportApiKeysRequest:
    out: ImportApiKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_api_gateway.types.blob

        out["body"] = capo_api_gateway.types.blob.deserialize_json(data["body"])
    else:
        raise DeserializationError("ImportApiKeysRequest.body required")
    return out
