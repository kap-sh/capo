"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListTelemetryFieldsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.telemetry_type


class ListTelemetryFieldsRequest(TypedDict, closed=True):
    data_set_name: "str"
    """The name of the dataset to list fields for."""
    telemetry_type: NotRequired[
        "capo_cloudwatchomni.types.telemetry_type.TelemetryType"
    ]
    """The type of telemetry to filter fields by."""
    start_time: NotRequired["datetime.datetime"]
    """Inclusive start of the lookback window. When omitted, the service defaults to the configured lookback before endTime."""
    end_time: NotRequired["datetime.datetime"]
    """Inclusive end of the lookback window. When omitted, the service defaults to the current time."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results. Reserved for future pagination; the service does not paginate at this time and returns null."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTelemetryFieldsRequest) -> dict:
    out: dict = {}
    out["dataSetName"] = value["data_set_name"]
    if "telemetry_type" in value:
        import capo_cloudwatchomni.types.telemetry_type

        out["telemetryType"] = capo_cloudwatchomni.types.telemetry_type.serialize_cbor(
            value["telemetry_type"]
        )
    if "start_time" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["startTime"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["endTime"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTelemetryFieldsRequest:
    out: ListTelemetryFieldsRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSetName") is not None:
        out["data_set_name"] = data["dataSetName"]
    else:
        out["data_set_name"] = ""
    if data.get("telemetryType") is not None:
        import capo_cloudwatchomni.types.telemetry_type

        out["telemetry_type"] = (
            capo_cloudwatchomni.types.telemetry_type.deserialize_cbor(
                data["telemetryType"]
            )
        )
    if data.get("startTime") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["start_time"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["end_time"] = capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
            data["endTime"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
