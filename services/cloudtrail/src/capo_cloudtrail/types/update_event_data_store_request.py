"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateEventDataStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.billing_mode
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.event_data_store_kms_key_id
    import capo_cloudtrail.types.event_data_store_name
    import capo_cloudtrail.types.retention_period
    import capo_cloudtrail.types.termination_protection_enabled


class UpdateEventDataStoreRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or the ID suffix of the ARN) of the event data store that you want to update.</p>"""
    name: NotRequired["capo_cloudtrail.types.event_data_store_name.EventDataStoreName"]
    """<p>The event data store name.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>The advanced event selectors used to select events for the event data store. You can configure up to five advanced event selectors for each event data store.</p>"""
    multi_region_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether an event data store collects events from all Regions, or only from the Region in which it was created.</p>"""
    organization_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether an event data store collects events logged for an organization in Organizations.</p> <note> <p>Only the management account for the organization can convert an organization event data store to a non-organization event data store, or convert a non-organization event data store to an organization event data store.</p> </note>"""
    retention_period: NotRequired[
        "capo_cloudtrail.types.retention_period.RetentionPeriod"
    ]
    """<p>The retention period of the event data store, in days. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code>, you can set a retention period of up to 3653 days, the equivalent of 10 years. If <code>BillingMode</code> is set to <code>FIXED_RETENTION_PRICING</code>, you can set a retention period of up to 2557 days, the equivalent of seven years.</p> <p>CloudTrail Lake determines whether to retain an event by checking if the <code>eventTime</code> of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the <code>eventTime</code> is older than 90 days.</p> <note> <p>If you decrease the retention period of an event data store, CloudTrail will remove any events with an <code>eventTime</code> older than the new retention period. For example, if the previous retention period was 365 days and you decrease it to 100 days, CloudTrail will remove events with an <code>eventTime</code> older than 100 days.</p> </note>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p>Indicates that termination protection is enabled and the event data store cannot be automatically deleted.</p>"""
    kms_key_id: NotRequired[
        "capo_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
    ]
    """<p>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <important> <p>Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.</p> </important> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>"""
    billing_mode: NotRequired["capo_cloudtrail.types.billing_mode.BillingMode"]
    """<note> <p>You can't change the billing mode from <code>EXTENDABLE_RETENTION_PRICING</code> to <code>FIXED_RETENTION_PRICING</code>. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code> and you want to use <code>FIXED_RETENTION_PRICING</code> instead, you'll need to stop ingestion on the event data store and create a new event data store that uses <code>FIXED_RETENTION_PRICING</code>.</p> </note> <p>The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.</p> <p>The following are the possible values:</p> <ul> <li> <p> <code>EXTENDABLE_RETENTION_PRICING</code> - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.</p> </li> <li> <p> <code>FIXED_RETENTION_PRICING</code> - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.</p> </li> </ul> <p>For more information about CloudTrail pricing, see <a href="http://aws.amazon.com/cloudtrail/pricing/">CloudTrail Pricing</a> and <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html">Managing CloudTrail Lake costs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEventDataStoreRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    if "name" in value:
        out["Name"] = value["name"]
    if "advanced_event_selectors" in value:
        import capo_cloudtrail.types.advanced_event_selectors

        out["AdvancedEventSelectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.serialize_aws_json_1_1(
                value["advanced_event_selectors"]
            )
        )
    if "multi_region_enabled" in value:
        out["MultiRegionEnabled"] = value["multi_region_enabled"]
    if "organization_enabled" in value:
        out["OrganizationEnabled"] = value["organization_enabled"]
    if "retention_period" in value:
        out["RetentionPeriod"] = value["retention_period"]
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "billing_mode" in value:
        import capo_cloudtrail.types.billing_mode

        out["BillingMode"] = capo_cloudtrail.types.billing_mode.serialize_aws_json_1_1(
            value["billing_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEventDataStoreRequest:
    out: UpdateEventDataStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError(
            "UpdateEventDataStoreRequest.event_data_store required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AdvancedEventSelectors") is not None:
        import capo_cloudtrail.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.deserialize_aws_json_1_1(
                data["AdvancedEventSelectors"]
            )
        )
    if data.get("MultiRegionEnabled") is not None:
        out["multi_region_enabled"] = data["MultiRegionEnabled"]
    if data.get("OrganizationEnabled") is not None:
        out["organization_enabled"] = data["OrganizationEnabled"]
    if data.get("RetentionPeriod") is not None:
        out["retention_period"] = data["RetentionPeriod"]
    if data.get("TerminationProtectionEnabled") is not None:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("BillingMode") is not None:
        import capo_cloudtrail.types.billing_mode

        out["billing_mode"] = (
            capo_cloudtrail.types.billing_mode.deserialize_aws_json_1_1(
                data["BillingMode"]
            )
        )
    return out
