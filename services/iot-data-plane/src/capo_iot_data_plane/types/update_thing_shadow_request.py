"""Generated from Smithy shape ``com.amazonaws.iotdataplane#UpdateThingShadowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.json_document
    import capo_iot_data_plane.types.shadow_name
    import capo_iot_data_plane.types.thing_name


class UpdateThingShadowRequest(TypedDict, closed=True):
    thing_name: "capo_iot_data_plane.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    shadow_name: NotRequired["capo_iot_data_plane.types.shadow_name.ShadowName"]
    """<p>The name of the shadow.</p>"""
    payload: "capo_iot_data_plane.types.json_document.JsonDocument"
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingShadowRequest) -> dict:
    out: dict = {}
    import capo_iot_data_plane.types.json_document

    out["payload"] = capo_iot_data_plane.types.json_document.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> UpdateThingShadowRequest:
    out: UpdateThingShadowRequest = {}  # type: ignore[typeddict-item]
    if data.get("payload") is not None:
        import capo_iot_data_plane.types.json_document

        out["payload"] = capo_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    else:
        out["payload"] = b""
    return out
