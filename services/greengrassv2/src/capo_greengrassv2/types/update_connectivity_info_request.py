"""Generated from Smithy shape ``com.amazonaws.greengrassv2#UpdateConnectivityInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.connectivity_info_list
    import capo_greengrassv2.types.core_device_thing_name


class UpdateConnectivityInfoRequest(TypedDict, closed=True):
    thing_name: "capo_greengrassv2.types.core_device_thing_name.CoreDeviceThingName"
    """<p>The name of the core device. This is also the name of the IoT thing.</p>"""
    connectivity_info: (
        "capo_greengrassv2.types.connectivity_info_list.connectivityInfoList"
    )
    """<p>The connectivity information for the core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityInfoRequest) -> dict:
    out: dict = {}
    import capo_greengrassv2.types.connectivity_info_list

    out["ConnectivityInfo"] = (
        capo_greengrassv2.types.connectivity_info_list.serialize_json(
            value["connectivity_info"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConnectivityInfoRequest:
    out: UpdateConnectivityInfoRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectivityInfo") is not None:
        import capo_greengrassv2.types.connectivity_info_list

        out["connectivity_info"] = (
            capo_greengrassv2.types.connectivity_info_list.deserialize_json(
                data["ConnectivityInfo"]
            )
        )
    else:
        out["connectivity_info"] = []
    return out
