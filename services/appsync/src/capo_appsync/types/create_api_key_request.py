"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.long
    import capo_appsync.types.string


class CreateApiKeyRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The ID for your GraphQL API.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>A description of the purpose of the API key.</p>"""
    expires: NotRequired["capo_appsync.types.long.Long"]
    """<p>From the creation time, the time after which the API key expires. The date is represented as seconds since the epoch, rounded down to the nearest hour. The default value for this parameter is 7 days from creation time. For more information, see .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "expires" in value:
        out["expires"] = value["expires"]
    return out


def deserialize_json(data: dict) -> CreateApiKeyRequest:
    out: CreateApiKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("expires") is not None:
        out["expires"] = data["expires"]
    return out
