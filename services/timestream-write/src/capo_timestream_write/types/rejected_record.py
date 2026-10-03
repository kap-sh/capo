"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RejectedRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.error_message
    import capo_timestream_write.types.record_index
    import capo_timestream_write.types.record_version


class RejectedRecord(TypedDict, closed=True):
    record_index: "capo_timestream_write.types.record_index.RecordIndex"
    """<p> The index of the record in the input request for WriteRecords. Indexes begin with 0. </p>"""
    reason: NotRequired["capo_timestream_write.types.error_message.ErrorMessage"]
    """<p> The reason why a record was not successfully inserted into Timestream. Possible causes of failure include: </p> <ul> <li> <p>Records with duplicate data where there are multiple records with the same dimensions, timestamps, and measure names but: </p> <ul> <li> <p>Measure values are different</p> </li> <li> <p>Version is not present in the request, <i>or</i> the value of version in the new record is equal to or lower than the existing value</p> </li> </ul> <p>If Timestream rejects data for this case, the <code>ExistingVersion</code> field in the <code>RejectedRecords</code> response will indicate the current record’s version. To force an update, you can resend the request with a version for the record set to a value greater than the <code>ExistingVersion</code>.</p> </li> <li> <p> Records with timestamps that lie outside the retention duration of the memory store. </p> <note> <p>When the retention window is updated, you will receive a <code>RejectedRecords</code> exception if you immediately try to ingest data within the new window. To avoid a <code>RejectedRecords</code> exception, wait until the duration of the new window to ingest new data. For further information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices.html#configuration"> Best Practices for Configuring Timestream</a> and <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html">the explanation of how storage works in Timestream</a>.</p> </note> </li> <li> <p> Records with dimensions or measures that exceed the Timestream defined limits. </p> </li> </ul> <p> For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html">Access Management</a> in the Timestream Developer Guide. </p>"""
    existing_version: NotRequired[
        "capo_timestream_write.types.record_version.RecordVersion"
    ]
    """<p>The existing version of the record. This value is populated in scenarios where an identical record exists with a higher version than the version in the write request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectedRecord) -> dict:
    out: dict = {}
    out["RecordIndex"] = value.get("record_index", 0)
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "existing_version" in value:
        out["ExistingVersion"] = value["existing_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectedRecord:
    out: RejectedRecord = {}  # type: ignore[typeddict-item]
    if data.get("RecordIndex") is not None:
        out["record_index"] = data["RecordIndex"]
    else:
        out["record_index"] = 0
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("ExistingVersion") is not None:
        out["existing_version"] = data["ExistingVersion"]
    return out
