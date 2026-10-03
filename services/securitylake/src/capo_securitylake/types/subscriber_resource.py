"""Generated from Smithy shape ``com.amazonaws.securitylake#SubscriberResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securitylake.types.access_type_list
    import capo_securitylake.types.amazon_resource_name
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.resource_share_arn
    import capo_securitylake.types.resource_share_name
    import capo_securitylake.types.role_arn
    import capo_securitylake.types.s3_bucket_arn
    import capo_securitylake.types.safe_string
    import capo_securitylake.types.subscriber_status
    import capo_securitylake.types.uuid


class SubscriberResource(TypedDict, closed=True):
    subscriber_id: "capo_securitylake.types.uuid.UUID"
    """<p>The subscriber ID of the Amazon Security Lake subscriber account.</p>"""
    subscriber_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The subscriber ARN of the Amazon Security Lake subscriber account.</p>"""
    subscriber_identity: "capo_securitylake.types.aws_identity.AwsIdentity"
    """<p>The Amazon Web Services identity used to access your data.</p>"""
    subscriber_name: "capo_securitylake.types.safe_string.SafeString"
    """<p>The name of your Amazon Security Lake subscriber account.</p>"""
    subscriber_description: NotRequired[
        "capo_securitylake.types.safe_string.SafeString"
    ]
    """<p>The subscriber descriptions for a subscriber account. The description for a subscriber includes <code>subscriberName</code>, <code>accountID</code>, <code>externalID</code>, and <code>subscriberId</code>.</p>"""
    sources: "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
    """<p>Amazon Security Lake supports log and event collection for natively supported Amazon Web Services services. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html">Amazon Security Lake User Guide</a>.</p>"""
    access_types: NotRequired["capo_securitylake.types.access_type_list.AccessTypeList"]
    """<p>You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.</p> <p> Subscribers can consume data by directly querying Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as <code>LAKEFORMATION</code>.</p>"""
    role_arn: NotRequired["capo_securitylake.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) specifying the role of the subscriber.</p>"""
    s3_bucket_arn: NotRequired["capo_securitylake.types.s3_bucket_arn.S3BucketArn"]
    """<p>The ARN for the Amazon S3 bucket.</p>"""
    subscriber_endpoint: NotRequired["capo_securitylake.types.safe_string.SafeString"]
    """<p>The subscriber endpoint to which exception messages are posted.</p>"""
    subscriber_status: NotRequired[
        "capo_securitylake.types.subscriber_status.SubscriberStatus"
    ]
    """<p>The subscriber status of the Amazon Security Lake subscriber account.</p>"""
    resource_share_arn: NotRequired[
        "capo_securitylake.types.resource_share_arn.ResourceShareArn"
    ]
    """<p>The Amazon Resource Name (ARN) which uniquely defines the Amazon Web Services RAM resource share. Before accepting the RAM resource share invitation, you can view details related to the RAM resource share.</p> <p>This field is available only for Lake Formation subscribers created after March 8, 2023.</p>"""
    resource_share_name: NotRequired[
        "capo_securitylake.types.resource_share_name.ResourceShareName"
    ]
    """<p>The name of the resource share.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the subscriber was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the subscriber was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriberResource) -> dict:
    out: dict = {}
    out["subscriberId"] = value["subscriber_id"]
    out["subscriberArn"] = value["subscriber_arn"]
    import capo_securitylake.types.aws_identity

    out["subscriberIdentity"] = capo_securitylake.types.aws_identity.serialize_json(
        value["subscriber_identity"]
    )
    out["subscriberName"] = value["subscriber_name"]
    if "subscriber_description" in value:
        out["subscriberDescription"] = value["subscriber_description"]
    import capo_securitylake.types.log_source_resource_list

    out["sources"] = capo_securitylake.types.log_source_resource_list.serialize_json(
        value["sources"]
    )
    if "access_types" in value:
        import capo_securitylake.types.access_type_list

        out["accessTypes"] = capo_securitylake.types.access_type_list.serialize_json(
            value["access_types"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "s3_bucket_arn" in value:
        out["s3BucketArn"] = value["s3_bucket_arn"]
    if "subscriber_endpoint" in value:
        out["subscriberEndpoint"] = value["subscriber_endpoint"]
    if "subscriber_status" in value:
        import capo_securitylake.types.subscriber_status

        out["subscriberStatus"] = (
            capo_securitylake.types.subscriber_status.serialize_json(
                value["subscriber_status"]
            )
        )
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "resource_share_name" in value:
        out["resourceShareName"] = value["resource_share_name"]
    if "created_at" in value:
        import capo_securitylake._protocol.serialize

        out["createdAt"] = capo_securitylake._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securitylake._protocol.serialize

        out["updatedAt"] = capo_securitylake._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> SubscriberResource:
    out: SubscriberResource = {}  # type: ignore[typeddict-item]
    if data.get("subscriberId") is not None:
        out["subscriber_id"] = data["subscriberId"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_id required")
    if data.get("subscriberArn") is not None:
        out["subscriber_arn"] = data["subscriberArn"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_arn required")
    if data.get("subscriberIdentity") is not None:
        import capo_securitylake.types.aws_identity

        out["subscriber_identity"] = (
            capo_securitylake.types.aws_identity.deserialize_json(
                data["subscriberIdentity"]
            )
        )
    else:
        raise DeserializationError("SubscriberResource.subscriber_identity required")
    if data.get("subscriberName") is not None:
        out["subscriber_name"] = data["subscriberName"]
    else:
        raise DeserializationError("SubscriberResource.subscriber_name required")
    if data.get("subscriberDescription") is not None:
        out["subscriber_description"] = data["subscriberDescription"]
    if data.get("sources") is not None:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        raise DeserializationError("SubscriberResource.sources required")
    if data.get("accessTypes") is not None:
        import capo_securitylake.types.access_type_list

        out["access_types"] = capo_securitylake.types.access_type_list.deserialize_json(
            data["accessTypes"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("s3BucketArn") is not None:
        out["s3_bucket_arn"] = data["s3BucketArn"]
    if data.get("subscriberEndpoint") is not None:
        out["subscriber_endpoint"] = data["subscriberEndpoint"]
    if data.get("subscriberStatus") is not None:
        import capo_securitylake.types.subscriber_status

        out["subscriber_status"] = (
            capo_securitylake.types.subscriber_status.deserialize_json(
                data["subscriberStatus"]
            )
        )
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("resourceShareName") is not None:
        out["resource_share_name"] = data["resourceShareName"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
