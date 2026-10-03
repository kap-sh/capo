"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateEventDataStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.billing_mode
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.event_data_store_kms_key_id
    import capo_cloudtrail.types.event_data_store_name
    import capo_cloudtrail.types.event_data_store_status
    import capo_cloudtrail.types.federation_role_arn
    import capo_cloudtrail.types.federation_status
    import capo_cloudtrail.types.retention_period
    import capo_cloudtrail.types.termination_protection_enabled


class UpdateEventDataStoreResponse(TypedDict, closed=True):
    event_data_store_arn: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN of the event data store.</p>"""
    name: NotRequired["capo_cloudtrail.types.event_data_store_name.EventDataStoreName"]
    """<p>The name of the event data store.</p>"""
    status: NotRequired[
        "capo_cloudtrail.types.event_data_store_status.EventDataStoreStatus"
    ]
    """<p>The status of an event data store.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>The advanced event selectors that are applied to the event data store.</p>"""
    multi_region_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates whether the event data store includes events from all Regions, or only from the Region in which it was created.</p>"""
    organization_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates whether an event data store is collecting logged events for an organization in Organizations.</p>"""
    retention_period: NotRequired[
        "capo_cloudtrail.types.retention_period.RetentionPeriod"
    ]
    """<p>The retention period, in days.</p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p>Indicates whether termination protection is enabled for the event data store.</p>"""
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp that shows when an event data store was first created.</p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp that shows when the event data store was last updated. <code>UpdatedTimestamp</code> is always either the same or newer than the time shown in <code>CreatedTimestamp</code>.</p>"""
    kms_key_id: NotRequired[
        "capo_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
    ]
    """<p>Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.</p> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p>"""
    billing_mode: NotRequired["capo_cloudtrail.types.billing_mode.BillingMode"]
    """<p>The billing mode for the event data store.</p>"""
    federation_status: NotRequired[
        "capo_cloudtrail.types.federation_status.FederationStatus"
    ]
    """<p> Indicates the <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html">Lake query federation</a> status. The status is <code>ENABLED</code> if Lake query federation is enabled, or <code>DISABLED</code> if Lake query federation is disabled. You cannot delete an event data store if the <code>FederationStatus</code> is <code>ENABLED</code>. </p>"""
    federation_role_arn: NotRequired[
        "capo_cloudtrail.types.federation_role_arn.FederationRoleArn"
    ]
    """<p> If Lake query federation is enabled, provides the ARN of the federation role used to access the resources for the federated event data store. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEventDataStoreResponse) -> dict:
    out: dict = {}
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_cloudtrail.types.event_data_store_status

        out["Status"] = (
            capo_cloudtrail.types.event_data_store_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
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
    if "created_timestamp" in value:
        import capo_cloudtrail.types.date

        out["CreatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_cloudtrail.types.date

        out["UpdatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "billing_mode" in value:
        import capo_cloudtrail.types.billing_mode

        out["BillingMode"] = capo_cloudtrail.types.billing_mode.serialize_aws_json_1_1(
            value["billing_mode"]
        )
    if "federation_status" in value:
        import capo_cloudtrail.types.federation_status

        out["FederationStatus"] = (
            capo_cloudtrail.types.federation_status.serialize_aws_json_1_1(
                value["federation_status"]
            )
        )
    if "federation_role_arn" in value:
        out["FederationRoleArn"] = value["federation_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEventDataStoreResponse:
    out: UpdateEventDataStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStoreArn") is not None:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_cloudtrail.types.event_data_store_status

        out["status"] = (
            capo_cloudtrail.types.event_data_store_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
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
    if data.get("CreatedTimestamp") is not None:
        import capo_cloudtrail.types.date

        out["created_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreatedTimestamp"]
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_cloudtrail.types.date

        out["updated_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["UpdatedTimestamp"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("BillingMode") is not None:
        import capo_cloudtrail.types.billing_mode

        out["billing_mode"] = (
            capo_cloudtrail.types.billing_mode.deserialize_aws_json_1_1(
                data["BillingMode"]
            )
        )
    if data.get("FederationStatus") is not None:
        import capo_cloudtrail.types.federation_status

        out["federation_status"] = (
            capo_cloudtrail.types.federation_status.deserialize_aws_json_1_1(
                data["FederationStatus"]
            )
        )
    if data.get("FederationRoleArn") is not None:
        out["federation_role_arn"] = data["FederationRoleArn"]
    return out
