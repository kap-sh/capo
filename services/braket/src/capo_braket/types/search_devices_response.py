"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.device_summary_list


class SearchDevicesResponse(TypedDict, closed=True):
    devices: "capo_braket.types.device_summary_list.DeviceSummaryList"
    """<p>An array of <code>DeviceSummary</code> objects for devices that match the specified filter values.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results, or null if there are no additional results. Use the token value in a subsequent request to continue search where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesResponse) -> dict:
    out: dict = {}
    import capo_braket.types.device_summary_list

    out["devices"] = capo_braket.types.device_summary_list.serialize_json(
        value["devices"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchDevicesResponse:
    out: SearchDevicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("devices") is not None:
        import capo_braket.types.device_summary_list

        out["devices"] = capo_braket.types.device_summary_list.deserialize_json(
            data["devices"]
        )
    else:
        out["devices"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
