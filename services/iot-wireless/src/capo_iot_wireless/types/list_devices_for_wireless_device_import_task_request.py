"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListDevicesForWirelessDeviceImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.import_task_id
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.onboard_status


class ListDevicesForWirelessDeviceImportTaskRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.import_task_id.ImportTaskId"
    """<p>The identifier of the import task for which wireless devices are listed.</p>"""
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""
    status: NotRequired["capo_iot_wireless.types.onboard_status.OnboardStatus"]
    """<p>The status of the devices in the import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesForWirelessDeviceImportTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesForWirelessDeviceImportTaskRequest:
    out: ListDevicesForWirelessDeviceImportTaskRequest = {}  # type: ignore[typeddict-item]
    return out
