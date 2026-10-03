"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeArchiveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.archive_arn
    import capo_eventbridge.types.archive_description
    import capo_eventbridge.types.archive_name
    import capo_eventbridge.types.archive_state
    import capo_eventbridge.types.archive_state_reason
    import capo_eventbridge.types.event_bus_arn
    import capo_eventbridge.types.event_pattern
    import capo_eventbridge.types.kms_key_identifier
    import capo_eventbridge.types.long
    import capo_eventbridge.types.retention_days
    import capo_eventbridge.types.timestamp


class DescribeArchiveResponse(TypedDict, closed=True):
    archive_arn: NotRequired["capo_eventbridge.types.archive_arn.ArchiveArn"]
    """<p>The ARN of the archive.</p>"""
    archive_name: NotRequired["capo_eventbridge.types.archive_name.ArchiveName"]
    """<p>The name of the archive.</p>"""
    event_source_arn: NotRequired["capo_eventbridge.types.event_bus_arn.EventBusArn"]
    """<p>The ARN of the event source associated with the archive.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.archive_description.ArchiveDescription"
    ]
    """<p>The description of the archive.</p>"""
    event_pattern: NotRequired["capo_eventbridge.types.event_pattern.EventPattern"]
    """<p>The event pattern used to filter events sent to the archive.</p>"""
    state: NotRequired["capo_eventbridge.types.archive_state.ArchiveState"]
    """<p>The state of the archive.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.archive_state_reason.ArchiveStateReason"
    ]
    """<p>The reason that the archive is in the state.</p>"""
    kms_key_identifier: NotRequired[
        "capo_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt this archive, if one has been specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html">Encrypting archives</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    retention_days: NotRequired["capo_eventbridge.types.retention_days.RetentionDays"]
    """<p>The number of days to retain events for in the archive.</p>"""
    size_bytes: "capo_eventbridge.types.long.Long"
    """<p>The size of the archive in bytes.</p>"""
    event_count: "capo_eventbridge.types.long.Long"
    """<p>The number of events in the archive.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time at which the archive was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeArchiveResponse) -> dict:
    out: dict = {}
    if "archive_arn" in value:
        out["ArchiveArn"] = value["archive_arn"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "state" in value:
        import capo_eventbridge.types.archive_state

        out["State"] = capo_eventbridge.types.archive_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    out["SizeBytes"] = value.get("size_bytes", 0)
    out["EventCount"] = value.get("event_count", 0)
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeArchiveResponse:
    out: DescribeArchiveResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArchiveArn") is not None:
        out["archive_arn"] = data["ArchiveArn"]
    if data.get("ArchiveName") is not None:
        out["archive_name"] = data["ArchiveName"]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EventPattern") is not None:
        out["event_pattern"] = data["EventPattern"]
    if data.get("State") is not None:
        import capo_eventbridge.types.archive_state

        out["state"] = capo_eventbridge.types.archive_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if data.get("RetentionDays") is not None:
        out["retention_days"] = data["RetentionDays"]
    if data.get("SizeBytes") is not None:
        out["size_bytes"] = data["SizeBytes"]
    else:
        out["size_bytes"] = 0
    if data.get("EventCount") is not None:
        out["event_count"] = data["EventCount"]
    else:
        out["event_count"] = 0
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
