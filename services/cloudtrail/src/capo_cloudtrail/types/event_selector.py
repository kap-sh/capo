"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.data_resources
    import capo_cloudtrail.types.exclude_management_event_sources
    import capo_cloudtrail.types.read_write_type


class EventSelector(TypedDict, closed=True):
    read_write_type: NotRequired["capo_cloudtrail.types.read_write_type.ReadWriteType"]
    """<p>Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 <code>GetConsoleOutput</code> is a read-only API operation and <code>RunInstances</code> is a write-only API operation.</p> <p> By default, the value is <code>All</code>.</p>"""
    include_management_events: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specify if you want your event selector to include management events for your trail.</p> <p> For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html">Management Events</a> in the <i>CloudTrail User Guide</i>.</p> <p>By default, the value is <code>true</code>.</p> <p>The first copy of management events is free. You are charged for additional copies of management events that you are logging on any subsequent trail in the same Region. For more information about CloudTrail pricing, see <a href="http://aws.amazon.com/cloudtrail/pricing/">CloudTrail Pricing</a>.</p>"""
    data_resources: NotRequired["capo_cloudtrail.types.data_resources.DataResources"]
    """<p>CloudTrail supports data event logging for Amazon S3 objects in standard S3 buckets, Lambda functions, and Amazon DynamoDB tables with basic event selectors. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html">Data Events</a> and <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">Limits in CloudTrail</a> in the <i>CloudTrail User Guide</i>.</p> <note> <p>To log data events for all other resource types including objects stored in <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html">directory buckets</a>, you must use <a href="https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html">AdvancedEventSelectors</a>. You must also use <code>AdvancedEventSelectors</code> if you want to filter on the <code>eventName</code> field.</p> </note>"""
    exclude_management_event_sources: NotRequired[
        "capo_cloudtrail.types.exclude_management_event_sources.ExcludeManagementEventSources"
    ]
    """<p>An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out Key Management Service or Amazon RDS Data API events by containing <code>kms.amazonaws.com</code> or <code>rdsdata.amazonaws.com</code>. By default, <code>ExcludeManagementEventSources</code> is empty, and KMS and Amazon RDS Data API events are logged to your trail. You can exclude management event sources only in Regions that support the event source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSelector) -> dict:
    out: dict = {}
    if "read_write_type" in value:
        import capo_cloudtrail.types.read_write_type

        out["ReadWriteType"] = (
            capo_cloudtrail.types.read_write_type.serialize_aws_json_1_1(
                value["read_write_type"]
            )
        )
    if "include_management_events" in value:
        out["IncludeManagementEvents"] = value["include_management_events"]
    if "data_resources" in value:
        import capo_cloudtrail.types.data_resources

        out["DataResources"] = (
            capo_cloudtrail.types.data_resources.serialize_aws_json_1_1(
                value["data_resources"]
            )
        )
    if "exclude_management_event_sources" in value:
        import capo_cloudtrail.types.exclude_management_event_sources

        out["ExcludeManagementEventSources"] = (
            capo_cloudtrail.types.exclude_management_event_sources.serialize_aws_json_1_1(
                value["exclude_management_event_sources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventSelector:
    out: EventSelector = {}  # type: ignore[typeddict-item]
    if data.get("ReadWriteType") is not None:
        import capo_cloudtrail.types.read_write_type

        out["read_write_type"] = (
            capo_cloudtrail.types.read_write_type.deserialize_aws_json_1_1(
                data["ReadWriteType"]
            )
        )
    if data.get("IncludeManagementEvents") is not None:
        out["include_management_events"] = data["IncludeManagementEvents"]
    if data.get("DataResources") is not None:
        import capo_cloudtrail.types.data_resources

        out["data_resources"] = (
            capo_cloudtrail.types.data_resources.deserialize_aws_json_1_1(
                data["DataResources"]
            )
        )
    if data.get("ExcludeManagementEventSources") is not None:
        import capo_cloudtrail.types.exclude_management_event_sources

        out["exclude_management_event_sources"] = (
            capo_cloudtrail.types.exclude_management_event_sources.deserialize_aws_json_1_1(
                data["ExcludeManagementEventSources"]
            )
        )
    return out
