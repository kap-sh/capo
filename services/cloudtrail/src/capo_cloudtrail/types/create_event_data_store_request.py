"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateEventDataStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.billing_mode
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.event_data_store_kms_key_id
    import capo_cloudtrail.types.event_data_store_name
    import capo_cloudtrail.types.retention_period
    import capo_cloudtrail.types.tags_list
    import capo_cloudtrail.types.termination_protection_enabled


class CreateEventDataStoreRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.event_data_store_name.EventDataStoreName"
    """<p>The name of the event data store.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>The advanced event selectors to use to select the events for the data store. You can configure up to five advanced event selectors for each event data store.</p> <p> For more information about how to use advanced event selectors to log CloudTrail events, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced">Log events by using advanced event selectors</a> in the CloudTrail User Guide.</p> <p>For more information about how to use advanced event selectors to include Config configuration items in your event data store, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html#lake-cli-create-eds-config">Create an event data store for Config configuration items</a> in the CloudTrail User Guide.</p> <p>For more information about how to use advanced event selectors to include events outside of Amazon Web Services events in your event data store, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html#lake-cli-create-integration">Create an integration to log events from outside Amazon Web Services</a> in the CloudTrail User Guide.</p>"""
    multi_region_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.</p>"""
    organization_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether an event data store collects events logged for an organization in Organizations.</p>"""
    retention_period: NotRequired[
        "capo_cloudtrail.types.retention_period.RetentionPeriod"
    ]
    """<p>The retention period of the event data store, in days. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code>, you can set a retention period of up to 3653 days, the equivalent of 10 years. If <code>BillingMode</code> is set to <code>FIXED_RETENTION_PRICING</code>, you can set a retention period of up to 2557 days, the equivalent of seven years.</p> <p>CloudTrail Lake determines whether to retain an event by checking if the <code>eventTime</code> of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the <code>eventTime</code> is older than 90 days.</p> <note> <p>If you plan to copy trail events to this event data store, we recommend that you consider both the age of the events that you want to copy as well as how long you want to keep the copied events in your event data store. For example, if you copy trail events that are 5 years old and specify a retention period of 7 years, the event data store will retain those events for two years.</p> </note>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p>Specifies whether termination protection is enabled for the event data store. If termination protection is enabled, you cannot delete the event data store until termination protection is disabled.</p>"""
    tags_list: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]
    kms_key_id: NotRequired[
        "capo_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
    ]
    """<p>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <important> <p>Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.</p> </important> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>"""
    start_ingestion: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the event data store should start ingesting live events. The default is true.</p>"""
    billing_mode: NotRequired["capo_cloudtrail.types.billing_mode.BillingMode"]
    """<p>The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.</p> <p>The following are the possible values:</p> <ul> <li> <p> <code>EXTENDABLE_RETENTION_PRICING</code> - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.</p> </li> <li> <p> <code>FIXED_RETENTION_PRICING</code> - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.</p> </li> </ul> <p>The default value is <code>EXTENDABLE_RETENTION_PRICING</code>.</p> <p>For more information about CloudTrail pricing, see <a href="http://aws.amazon.com/cloudtrail/pricing/">CloudTrail Pricing</a> and <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html">Managing CloudTrail Lake costs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventDataStoreRequest) -> dict:
    out: dict = {}
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
    if "tags_list" in value:
        import capo_cloudtrail.types.tags_list

        out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "start_ingestion" in value:
        out["StartIngestion"] = value["start_ingestion"]
    if "billing_mode" in value:
        import capo_cloudtrail.types.billing_mode

        out["BillingMode"] = capo_cloudtrail.types.billing_mode.serialize_aws_json_1_1(
            value["billing_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventDataStoreRequest:
    out: CreateEventDataStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEventDataStoreRequest.name required")
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
    if data.get("TagsList") is not None:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("StartIngestion") is not None:
        out["start_ingestion"] = data["StartIngestion"]
    if data.get("BillingMode") is not None:
        import capo_cloudtrail.types.billing_mode

        out["billing_mode"] = (
            capo_cloudtrail.types.billing_mode.deserialize_aws_json_1_1(
                data["BillingMode"]
            )
        )
    return out
