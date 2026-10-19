"""Generated from Smithy shape ``com.amazonaws.iotdataplane#DeleteThingShadowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_data_plane.types.json_document


class DeleteThingShadowResponse(TypedDict, closed=True):
    payload: "capo_iot_data_plane.types.json_document.JsonDocument"
    """<p>The state information, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThingShadowResponse) -> dict:
    out: dict = {}
    import capo_iot_data_plane.types.json_document

    out["payload"] = capo_iot_data_plane.types.json_document.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> DeleteThingShadowResponse:
    out: DeleteThingShadowResponse = {}  # type: ignore[typeddict-item]
    if data.get("payload") is not None:
        import capo_iot_data_plane.types.json_document

        out["payload"] = capo_iot_data_plane.types.json_document.deserialize_json(
            data["payload"]
        )
    else:
        out["payload"] = b""
    return out
