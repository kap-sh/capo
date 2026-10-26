"""Generated from Smithy shape ``com.amazonaws.groundstation#GetConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_type_data
    import capo_groundstation.types.tags_map


class GetConfigResponse(TypedDict, closed=True):
    config_id: "str"
    """<p>UUID of a <code>Config</code>.</p>"""
    config_arn: "capo_groundstation.types.config_arn.ConfigArn"
    """<p>ARN of a <code>Config</code> </p>"""
    name: "str"
    """<p>Name of a <code>Config</code>.</p>"""
    config_type: NotRequired[
        "capo_groundstation.types.config_capability_type.ConfigCapabilityType"
    ]
    """<p>Type of a <code>Config</code>.</p>"""
    config_data: "capo_groundstation.types.config_type_data.ConfigTypeData"
    """<p>Data elements in a <code>Config</code>.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigResponse) -> dict:
    out: dict = {}
    out["configId"] = value["config_id"]
    out["configArn"] = value["config_arn"]
    out["name"] = value["name"]
    if "config_type" in value:
        import capo_groundstation.types.config_capability_type

        out["configType"] = (
            capo_groundstation.types.config_capability_type.serialize_json(
                value["config_type"]
            )
        )
    import capo_groundstation.types.config_type_data

    out["configData"] = capo_groundstation.types.config_type_data.serialize_json(
        value["config_data"]
    )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetConfigResponse:
    out: GetConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("configId") is not None:
        out["config_id"] = data["configId"]
    else:
        out["config_id"] = ""
    if data.get("configArn") is not None:
        out["config_arn"] = data["configArn"]
    else:
        out["config_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("configType") is not None:
        import capo_groundstation.types.config_capability_type

        out["config_type"] = (
            capo_groundstation.types.config_capability_type.deserialize_json(
                data["configType"]
            )
        )
    if data.get("configData") is not None:
        import capo_groundstation.types.config_type_data

        out["config_data"] = capo_groundstation.types.config_type_data.deserialize_json(
            data["configData"]
        )
    else:
        out["config_data"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    return out
