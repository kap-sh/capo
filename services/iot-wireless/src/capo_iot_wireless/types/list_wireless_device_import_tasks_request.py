"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessDeviceImportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.next_token


class ListWirelessDeviceImportTasksRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessDeviceImportTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWirelessDeviceImportTasksRequest:
    out: ListWirelessDeviceImportTasksRequest = {}  # type: ignore[typeddict-item]
    return out
