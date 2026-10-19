"""Generated from Smithy shape ``com.amazonaws.xray#PutTelemetryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.ec2_instance_id
    import capo_xray.types.hostname
    import capo_xray.types.resource_arn
    import capo_xray.types.telemetry_record_list


class PutTelemetryRecordsRequest(TypedDict, closed=True):
    telemetry_records: "capo_xray.types.telemetry_record_list.TelemetryRecordList"
    """<p></p>"""
    ec2_instance_id: NotRequired["capo_xray.types.ec2_instance_id.EC2InstanceId"]
    """<p></p>"""
    hostname: NotRequired["capo_xray.types.hostname.Hostname"]
    """<p></p>"""
    resource_arn: NotRequired["capo_xray.types.resource_arn.ResourceARN"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTelemetryRecordsRequest) -> dict:
    out: dict = {}
    import capo_xray.types.telemetry_record_list

    out["TelemetryRecords"] = capo_xray.types.telemetry_record_list.serialize_json(
        value["telemetry_records"]
    )
    if "ec2_instance_id" in value:
        out["EC2InstanceId"] = value["ec2_instance_id"]
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> PutTelemetryRecordsRequest:
    out: PutTelemetryRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TelemetryRecords") is not None:
        import capo_xray.types.telemetry_record_list

        out["telemetry_records"] = (
            capo_xray.types.telemetry_record_list.deserialize_json(
                data["TelemetryRecords"]
            )
        )
    else:
        out["telemetry_records"] = []
    if data.get("EC2InstanceId") is not None:
        out["ec2_instance_id"] = data["EC2InstanceId"]
    if data.get("Hostname") is not None:
        out["hostname"] = data["Hostname"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    return out
