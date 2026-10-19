"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateUsagePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_api_stage
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.quota_settings
    import capo_api_gateway.types.string
    import capo_api_gateway.types.throttle_settings


class CreateUsagePlanRequest(TypedDict, closed=True):
    name: "capo_api_gateway.types.string.String"
    """<p>The name of the usage plan.</p>"""
    description: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The description of the usage plan.</p>"""
    api_stages: NotRequired["capo_api_gateway.types.list_of_api_stage.ListOfApiStage"]
    """<p>The associated API stages of the usage plan.</p>"""
    throttle: NotRequired["capo_api_gateway.types.throttle_settings.ThrottleSettings"]
    """<p>The throttling limits of the usage plan.</p>"""
    quota: NotRequired["capo_api_gateway.types.quota_settings.QuotaSettings"]
    """<p>The quota of the usage plan.</p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUsagePlanRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "api_stages" in value:
        import capo_api_gateway.types.list_of_api_stage

        out["apiStages"] = capo_api_gateway.types.list_of_api_stage.serialize_json(
            value["api_stages"]
        )
    if "throttle" in value:
        import capo_api_gateway.types.throttle_settings

        out["throttle"] = capo_api_gateway.types.throttle_settings.serialize_json(
            value["throttle"]
        )
    if "quota" in value:
        import capo_api_gateway.types.quota_settings

        out["quota"] = capo_api_gateway.types.quota_settings.serialize_json(
            value["quota"]
        )
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateUsagePlanRequest:
    out: CreateUsagePlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("apiStages") is not None:
        import capo_api_gateway.types.list_of_api_stage

        out["api_stages"] = capo_api_gateway.types.list_of_api_stage.deserialize_json(
            data["apiStages"]
        )
    if data.get("throttle") is not None:
        import capo_api_gateway.types.throttle_settings

        out["throttle"] = capo_api_gateway.types.throttle_settings.deserialize_json(
            data["throttle"]
        )
    if data.get("quota") is not None:
        import capo_api_gateway.types.quota_settings

        out["quota"] = capo_api_gateway.types.quota_settings.deserialize_json(
            data["quota"]
        )
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
