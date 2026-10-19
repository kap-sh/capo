"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateApiKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.list_of_stage_keys
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class CreateApiKeyRequest(TypedDict, closed=True):
    name: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The name of the ApiKey.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the ApiKey.</p>"""
    enabled: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>Specifies whether the ApiKey can be used by callers.</p>"""
    generate_distinct_id: NotRequired["capo_api_gateway.types.boolean.Boolean"]
    """<p>Specifies whether (<code>true</code>) or not (<code>false</code>) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</p>"""
    value: NotRequired["capo_api_gateway.types.string.String"]
    """<p>Specifies a value of the API key.</p>"""
    stage_keys: NotRequired["capo_api_gateway.types.list_of_stage_keys.ListOfStageKeys"]
    """<p>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</p>"""
    customer_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>An Amazon Web Services Marketplace customer identifier, when integrating with the Amazon Web Services SaaS Marketplace.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiKeyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "generate_distinct_id" in value:
        out["generateDistinctId"] = value["generate_distinct_id"]
    if "value" in value:
        out["value"] = value["value"]
    if "stage_keys" in value:
        import capo_api_gateway.types.list_of_stage_keys

        out["stageKeys"] = capo_api_gateway.types.list_of_stage_keys.serialize_json(
            value["stage_keys"]
        )
    if "customer_id" in value:
        out["customerId"] = value["customer_id"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateApiKeyRequest:
    out: CreateApiKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("generateDistinctId") is not None:
        out["generate_distinct_id"] = data["generateDistinctId"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("stageKeys") is not None:
        import capo_api_gateway.types.list_of_stage_keys

        out["stage_keys"] = capo_api_gateway.types.list_of_stage_keys.deserialize_json(
            data["stageKeys"]
        )
    if data.get("customerId") is not None:
        out["customer_id"] = data["customerId"]
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
