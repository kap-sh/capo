"""Generated from Smithy shape ``com.amazonaws.health#AffectedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.account_id
    import capo_health.types.account_tag_set
    import capo_health.types.entity_arn
    import capo_health.types.entity_metadata
    import capo_health.types.entity_status_code
    import capo_health.types.entity_url
    import capo_health.types.entity_value
    import capo_health.types.event_arn
    import capo_health.types.resource_tag_set
    import capo_health.types.timestamp


class AffectedEntity(TypedDict, closed=True):
    entity_arn: NotRequired["capo_health.types.entity_arn.entityArn"]
    """<p>The unique identifier for the entity. Format: <code>arn:aws:health:<i>entity-region</i>:<i>aws-account</i>:entity/<i>entity-id</i> </code>. Example: <code>arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K</code> </p>"""
    event_arn: NotRequired["capo_health.types.event_arn.eventArn"]
    """<p>The unique identifier for the event. The event ARN has the <code>arn:aws:health:<i>event-region</i>::event/<i>SERVICE</i>/<i>EVENT_TYPE_CODE</i>/<i>EVENT_TYPE_PLUS_ID</i> </code> format.</p> <p>For example, an event ARN might look like the following:</p> <p> <code>arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456</code> </p>"""
    entity_value: NotRequired["capo_health.types.entity_value.entityValue"]
    """<p>The ID of the affected entity.</p>"""
    entity_url: NotRequired["capo_health.types.entity_url.entityUrl"]
    """<p>The URL of the affected entity.</p>"""
    aws_account_id: NotRequired["capo_health.types.account_id.accountId"]
    """<p>The 12-digit Amazon Web Services account number that contains the affected entity.</p>"""
    last_updated_time: NotRequired["capo_health.types.timestamp.timestamp"]
    """<p>The most recent time that the entity was updated.</p>"""
    status_code: NotRequired["capo_health.types.entity_status_code.entityStatusCode"]
    """<p>The most recent status of the entity affected by the event. The possible values are <code>IMPAIRED</code>, <code>UNIMPAIRED</code>, <code>UNKNOWN</code>, <code>PENDING</code>, and <code>RESOLVED</code>.</p>"""
    resource_tags: NotRequired["capo_health.types.resource_tag_set.ResourceTagSet"]
    """<p>A map of resource tag key-value pairs attached to the affected entity.</p>"""
    account_tags: NotRequired["capo_health.types.account_tag_set.AccountTagSet"]
    """<p>A map of account tag key-value pairs for the account that owns the affected entity. This field is returned only by DescribeAffectedEntitiesForOrganization and is not populated by DescribeAffectedEntities.</p>"""
    entity_metadata: NotRequired["capo_health.types.entity_metadata.entityMetadata"]
    """<p>Additional metadata about the affected entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AffectedEntity) -> dict:
    out: dict = {}
    if "entity_arn" in value:
        out["entityArn"] = value["entity_arn"]
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "entity_value" in value:
        out["entityValue"] = value["entity_value"]
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "last_updated_time" in value:
        import capo_health.types.timestamp

        out["lastUpdatedTime"] = capo_health.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import capo_health.types.entity_status_code

        out["statusCode"] = capo_health.types.entity_status_code.serialize_aws_json_1_1(
            value["status_code"]
        )
    if "resource_tags" in value:
        import capo_health.types.resource_tag_set

        out["resourceTags"] = capo_health.types.resource_tag_set.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    if "account_tags" in value:
        import capo_health.types.account_tag_set

        out["accountTags"] = capo_health.types.account_tag_set.serialize_aws_json_1_1(
            value["account_tags"]
        )
    if "entity_metadata" in value:
        import capo_health.types.entity_metadata

        out["entityMetadata"] = (
            capo_health.types.entity_metadata.serialize_aws_json_1_1(
                value["entity_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AffectedEntity:
    out: AffectedEntity = {}  # type: ignore[typeddict-item]
    if data.get("entityArn") is not None:
        out["entity_arn"] = data["entityArn"]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("entityValue") is not None:
        out["entity_value"] = data["entityValue"]
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("lastUpdatedTime") is not None:
        import capo_health.types.timestamp

        out["last_updated_time"] = capo_health.types.timestamp.deserialize_aws_json_1_1(
            data["lastUpdatedTime"]
        )
    if data.get("statusCode") is not None:
        import capo_health.types.entity_status_code

        out["status_code"] = (
            capo_health.types.entity_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if data.get("resourceTags") is not None:
        import capo_health.types.resource_tag_set

        out["resource_tags"] = (
            capo_health.types.resource_tag_set.deserialize_aws_json_1_1(
                data["resourceTags"]
            )
        )
    if data.get("accountTags") is not None:
        import capo_health.types.account_tag_set

        out["account_tags"] = (
            capo_health.types.account_tag_set.deserialize_aws_json_1_1(
                data["accountTags"]
            )
        )
    if data.get("entityMetadata") is not None:
        import capo_health.types.entity_metadata

        out["entity_metadata"] = (
            capo_health.types.entity_metadata.deserialize_aws_json_1_1(
                data["entityMetadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AffectedEntity) -> dict:
    out: dict = {}
    if "entity_arn" in value:
        out["entityArn"] = value["entity_arn"]
    if "event_arn" in value:
        out["eventArn"] = value["event_arn"]
    if "entity_value" in value:
        out["entityValue"] = value["entity_value"]
    if "entity_url" in value:
        out["entityUrl"] = value["entity_url"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "last_updated_time" in value:
        import capo_health.types.timestamp

        out["lastUpdatedTime"] = capo_health.types.timestamp.serialize_cbor(
            value["last_updated_time"]
        )
    if "status_code" in value:
        import capo_health.types.entity_status_code

        out["statusCode"] = capo_health.types.entity_status_code.serialize_cbor(
            value["status_code"]
        )
    if "resource_tags" in value:
        import capo_health.types.resource_tag_set

        out["resourceTags"] = capo_health.types.resource_tag_set.serialize_cbor(
            value["resource_tags"]
        )
    if "account_tags" in value:
        import capo_health.types.account_tag_set

        out["accountTags"] = capo_health.types.account_tag_set.serialize_cbor(
            value["account_tags"]
        )
    if "entity_metadata" in value:
        import capo_health.types.entity_metadata

        out["entityMetadata"] = capo_health.types.entity_metadata.serialize_cbor(
            value["entity_metadata"]
        )
    return out


def deserialize_cbor(data: dict) -> AffectedEntity:
    out: AffectedEntity = {}  # type: ignore[typeddict-item]
    if data.get("entityArn") is not None:
        out["entity_arn"] = data["entityArn"]
    if data.get("eventArn") is not None:
        out["event_arn"] = data["eventArn"]
    if data.get("entityValue") is not None:
        out["entity_value"] = data["entityValue"]
    if data.get("entityUrl") is not None:
        out["entity_url"] = data["entityUrl"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("lastUpdatedTime") is not None:
        import capo_health.types.timestamp

        out["last_updated_time"] = capo_health.types.timestamp.deserialize_cbor(
            data["lastUpdatedTime"]
        )
    if data.get("statusCode") is not None:
        import capo_health.types.entity_status_code

        out["status_code"] = capo_health.types.entity_status_code.deserialize_cbor(
            data["statusCode"]
        )
    if data.get("resourceTags") is not None:
        import capo_health.types.resource_tag_set

        out["resource_tags"] = capo_health.types.resource_tag_set.deserialize_cbor(
            data["resourceTags"]
        )
    if data.get("accountTags") is not None:
        import capo_health.types.account_tag_set

        out["account_tags"] = capo_health.types.account_tag_set.deserialize_cbor(
            data["accountTags"]
        )
    if data.get("entityMetadata") is not None:
        import capo_health.types.entity_metadata

        out["entity_metadata"] = capo_health.types.entity_metadata.deserialize_cbor(
            data["entityMetadata"]
        )
    return out
