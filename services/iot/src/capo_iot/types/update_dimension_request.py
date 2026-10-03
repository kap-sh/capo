"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDimensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.dimension_name
    import capo_iot.types.dimension_string_values


class UpdateDimensionRequest(TypedDict, closed=True):
    name: "capo_iot.types.dimension_name.DimensionName"
    """<p>A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.</p>"""
    string_values: "capo_iot.types.dimension_string_values.DimensionStringValues"
    """<p>Specifies the value or list of values for the dimension. For <code>TOPIC_FILTER</code> dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDimensionRequest) -> dict:
    out: dict = {}
    import capo_iot.types.dimension_string_values

    out["stringValues"] = capo_iot.types.dimension_string_values.serialize_json(
        value["string_values"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDimensionRequest:
    out: UpdateDimensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("stringValues") is not None:
        import capo_iot.types.dimension_string_values

        out["string_values"] = capo_iot.types.dimension_string_values.deserialize_json(
            data["stringValues"]
        )
    else:
        raise DeserializationError("UpdateDimensionRequest.string_values required")
    return out
