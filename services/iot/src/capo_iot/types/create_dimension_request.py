"""Generated from Smithy shape ``com.amazonaws.iot#CreateDimensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.client_request_token
    import capo_iot.types.dimension_name
    import capo_iot.types.dimension_string_values
    import capo_iot.types.dimension_type
    import capo_iot.types.tag_list


class CreateDimensionRequest(TypedDict, closed=True):
    name: "capo_iot.types.dimension_name.DimensionName"
    """<p>A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.</p>"""
    type: "capo_iot.types.dimension_type.DimensionType"
    """<p>Specifies the type of dimension. Supported types: <code>TOPIC_FILTER.</code> </p>"""
    string_values: "capo_iot.types.dimension_string_values.DimensionStringValues"
    """<p>Specifies the value or list of values for the dimension. For <code>TOPIC_FILTER</code> dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the dimension.</p>"""
    client_request_token: "capo_iot.types.client_request_token.ClientRequestToken"
    """<p>Each dimension must have a unique client request token. If you try to create a new dimension with the same token as a dimension that already exists, an exception occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDimensionRequest) -> dict:
    out: dict = {}
    import capo_iot.types.dimension_type

    out["type"] = capo_iot.types.dimension_type.serialize_json(value["type"])
    import capo_iot.types.dimension_string_values

    out["stringValues"] = capo_iot.types.dimension_string_values.serialize_json(
        value["string_values"]
    )
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateDimensionRequest:
    out: CreateDimensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_iot.types.dimension_type

        out["type"] = capo_iot.types.dimension_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CreateDimensionRequest.type required")
    if data.get("stringValues") is not None:
        import capo_iot.types.dimension_string_values

        out["string_values"] = capo_iot.types.dimension_string_values.deserialize_json(
            data["stringValues"]
        )
    else:
        raise DeserializationError("CreateDimensionRequest.string_values required")
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        raise DeserializationError(
            "CreateDimensionRequest.client_request_token required"
        )
    return out
