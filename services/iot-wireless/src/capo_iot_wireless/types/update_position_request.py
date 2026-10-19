"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdatePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_coordinate
    import capo_iot_wireless.types.position_resource_identifier
    import capo_iot_wireless.types.position_resource_type


class UpdatePositionRequest(TypedDict, closed=True):
    resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>Resource identifier of the resource for which position is updated.</p>"""
    resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType"
    """<p>Resource type of the resource for which position is updated.</p>"""
    position: "capo_iot_wireless.types.position_coordinate.PositionCoordinate"
    """<p>The position information of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePositionRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.position_coordinate

    out["Position"] = capo_iot_wireless.types.position_coordinate.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePositionRequest:
    out: UpdatePositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_iot_wireless.types.position_coordinate

        out["position"] = capo_iot_wireless.types.position_coordinate.deserialize_json(
            data["Position"]
        )
    else:
        out["position"] = []
    return out
