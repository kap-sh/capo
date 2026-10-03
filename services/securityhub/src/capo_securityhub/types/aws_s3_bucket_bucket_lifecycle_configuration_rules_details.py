"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list
    import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesDetails(TypedDict, closed=True):
    abort_incomplete_multipart_upload: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details.AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails"
    ]
    """<p>How Amazon S3 responds when a multipart upload is incomplete. Specifically, provides a number of days before Amazon S3 cancels the entire upload.</p>"""
    expiration_date: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date when objects are moved or deleted.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    expiration_in_days: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The length in days of the lifetime for objects that are subject to the rule.</p>"""
    expired_object_delete_marker: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether Amazon S3 removes a delete marker that has no noncurrent versions. If set to <code>true</code>, the delete marker is expired. If set to <code>false</code>, the policy takes no action.</p> <p>If you provide <code>ExpiredObjectDeleteMarker</code>, you cannot provide <code>ExpirationInDays</code> or <code>ExpirationDate</code>.</p>"""
    filter: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details.AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails"
    ]
    """<p>Identifies the objects that a rule applies to.</p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the rule.</p>"""
    noncurrent_version_expiration_in_days: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of days that an object is noncurrent before Amazon S3 can perform the associated action.</p>"""
    noncurrent_version_transitions: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list.AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsList"
    ]
    """<p>Transition rules that describe when noncurrent objects transition to a specified storage class.</p>"""
    prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A prefix that identifies one or more objects that the rule applies to.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current status of the rule. Indicates whether the rule is currently being applied.</p>"""
    transitions: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list.AwsS3BucketBucketLifecycleConfigurationRulesTransitionsList"
    ]
    """<p>Transition rules that indicate when objects transition to a specified storage class.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketBucketLifecycleConfigurationRulesDetails) -> dict:
    out: dict = {}
    if "abort_incomplete_multipart_upload" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details

        out["AbortIncompleteMultipartUpload"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details.serialize_json(
                value["abort_incomplete_multipart_upload"]
            )
        )
    if "expiration_date" in value:
        out["ExpirationDate"] = value["expiration_date"]
    if "expiration_in_days" in value:
        out["ExpirationInDays"] = value["expiration_in_days"]
    if "expired_object_delete_marker" in value:
        out["ExpiredObjectDeleteMarker"] = value["expired_object_delete_marker"]
    if "filter" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details

        out["Filter"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details.serialize_json(
                value["filter"]
            )
        )
    if "id" in value:
        out["ID"] = value["id"]
    if "noncurrent_version_expiration_in_days" in value:
        out["NoncurrentVersionExpirationInDays"] = value[
            "noncurrent_version_expiration_in_days"
        ]
    if "noncurrent_version_transitions" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list

        out["NoncurrentVersionTransitions"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list.serialize_json(
                value["noncurrent_version_transitions"]
            )
        )
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "status" in value:
        out["Status"] = value["status"]
    if "transitions" in value:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list

        out["Transitions"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list.serialize_json(
                value["transitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketBucketLifecycleConfigurationRulesDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesDetails = {}  # type: ignore[typeddict-item]
    if data.get("AbortIncompleteMultipartUpload") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details

        out["abort_incomplete_multipart_upload"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_abort_incomplete_multipart_upload_details.deserialize_json(
                data["AbortIncompleteMultipartUpload"]
            )
        )
    if data.get("ExpirationDate") is not None:
        out["expiration_date"] = data["ExpirationDate"]
    if data.get("ExpirationInDays") is not None:
        out["expiration_in_days"] = data["ExpirationInDays"]
    if data.get("ExpiredObjectDeleteMarker") is not None:
        out["expired_object_delete_marker"] = data["ExpiredObjectDeleteMarker"]
    if data.get("Filter") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details

        out["filter"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_filter_details.deserialize_json(
                data["Filter"]
            )
        )
    if data.get("ID") is not None:
        out["id"] = data["ID"]
    if data.get("NoncurrentVersionExpirationInDays") is not None:
        out["noncurrent_version_expiration_in_days"] = data[
            "NoncurrentVersionExpirationInDays"
        ]
    if data.get("NoncurrentVersionTransitions") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list

        out["noncurrent_version_transitions"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_noncurrent_version_transitions_list.deserialize_json(
                data["NoncurrentVersionTransitions"]
            )
        )
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("Transitions") is not None:
        import capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list

        out["transitions"] = (
            capo_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_transitions_list.deserialize_json(
                data["Transitions"]
            )
        )
    return out
