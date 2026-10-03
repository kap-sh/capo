"""Generated from Smithy shape ``com.amazonaws.s3control#S3CopyObjectOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.kms_key_arn_string
    import capo_s3_control.types.non_empty_max_length1024_string
    import capo_s3_control.types.non_empty_max_length2048_string
    import capo_s3_control.types.s3_annotation_directive
    import capo_s3_control.types.s3_canned_access_control_list
    import capo_s3_control.types.s3_checksum_algorithm
    import capo_s3_control.types.s3_grant_list
    import capo_s3_control.types.s3_metadata_directive
    import capo_s3_control.types.s3_object_lock_event_hold
    import capo_s3_control.types.s3_object_lock_event_hold_duration
    import capo_s3_control.types.s3_object_lock_legal_hold_status
    import capo_s3_control.types.s3_object_lock_mode
    import capo_s3_control.types.s3_object_metadata
    import capo_s3_control.types.s3_regional_or_s3_express_bucket_arn_string
    import capo_s3_control.types.s3_storage_class
    import capo_s3_control.types.s3_tag_set
    import capo_s3_control.types.time_stamp


class S3CopyObjectOperation(TypedDict, closed=True):
    target_resource: NotRequired[
        "capo_s3_control.types.s3_regional_or_s3_express_bucket_arn_string.S3RegionalOrS3ExpressBucketArnString"
    ]
    """<p>Specifies the destination bucket Amazon Resource Name (ARN) for the batch copy operation.</p> <ul> <li> <p> <b>General purpose buckets</b> - For example, to copy objects to a general purpose bucket named <code>destinationBucket</code>, set the <code>TargetResource</code> property to <code>arn:aws:s3:::destinationBucket</code>.</p> </li> <li> <p> <b>Directory buckets</b> - For example, to copy objects to a directory bucket named <code>destinationBucket</code> in the Availability Zone identified by the AZ ID <code>usw2-az1</code>, set the <code>TargetResource</code> property to <code>arn:aws:s3express:<i>region</i>:<i>account_id</i>:/bucket/<i>destination_bucket_base_name</i>--<i>usw2-az1</i>--x-s3</code>. A directory bucket as a destination bucket can be in Availability Zone or Local Zone. </p> <note> <p>Copying objects across different Amazon Web Services Regions isn't supported when the source or destination bucket is in Amazon Web Services Local Zones. The source and destination buckets must have the same parent Amazon Web Services Region. Otherwise, you get an HTTP <code>400 Bad Request</code> error with the error code <code>InvalidRequest</code>.</p> </note> </li> </ul>"""
    canned_access_control_list: NotRequired[
        "capo_s3_control.types.s3_canned_access_control_list.S3CannedAccessControlList"
    ]
    """<p></p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    access_control_grants: NotRequired[
        "capo_s3_control.types.s3_grant_list.S3GrantList"
    ]
    """<p></p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    metadata_directive: NotRequired[
        "capo_s3_control.types.s3_metadata_directive.S3MetadataDirective"
    ]
    """<p></p>"""
    annotation_directive: NotRequired[
        "capo_s3_control.types.s3_annotation_directive.S3AnnotationDirective"
    ]
    """<p>Specifies whether the Batch Operations copy job copies object annotations from the source object or skips them. If this property isn't specified, <code>COPY</code> is the default behavior.</p> <p>Valid Values: <code>COPY | EXCLUDE</code> </p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    modified_since_constraint: NotRequired["capo_s3_control.types.time_stamp.TimeStamp"]
    """<p></p>"""
    new_object_metadata: NotRequired[
        "capo_s3_control.types.s3_object_metadata.S3ObjectMetadata"
    ]
    """<p>If you don't provide this parameter, Amazon S3 copies all the metadata from the original objects. If you specify an empty set, the new objects will have no tags. Otherwise, Amazon S3 assigns the supplied tags to the new objects.</p>"""
    new_object_tagging: NotRequired["capo_s3_control.types.s3_tag_set.S3TagSet"]
    """<p>Specifies a list of tags to add to the destination objects after they are copied. If <code>NewObjectTagging</code> is not specified, the tags of the source objects are copied to destination objects by default.</p> <note> <p> <b>Directory buckets</b> - Tags aren't supported by directory buckets. If your source objects have tags and your destination bucket is a directory bucket, specify an empty tag set in the <code>NewObjectTagging</code> field to prevent copying the source object tags to the directory bucket.</p> </note>"""
    redirect_location: NotRequired[
        "capo_s3_control.types.non_empty_max_length2048_string.NonEmptyMaxLength2048String"
    ]
    """<p>If the destination bucket is configured as a website, specifies an optional metadata property for website redirects, <code>x-amz-website-redirect-location</code>. Allows webpage redirects if the object copy is accessed through a website endpoint.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    requester_pays: "capo_s3_control.types.boolean.Boolean"
    """<p></p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    storage_class: NotRequired["capo_s3_control.types.s3_storage_class.S3StorageClass"]
    """<p>Specify the storage class for the destination objects in a <code>Copy</code> operation.</p> <note> <p> <b>Directory buckets </b> - This functionality is not supported by directory buckets. </p> </note>"""
    un_modified_since_constraint: NotRequired[
        "capo_s3_control.types.time_stamp.TimeStamp"
    ]
    """<p></p>"""
    sse_aws_kms_key_id: NotRequired[
        "capo_s3_control.types.kms_key_arn_string.KmsKeyArnString"
    ]
    """<p>Specifies the KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same account that's issuing the command, you must use the full Key ARN not the Key ID.</p> <note> <p> <b>Directory buckets</b> - If you specify <code>SSEAlgorithm</code> with <code>KMS</code>, you must specify the <code> SSEAwsKmsKeyId</code> parameter with the ID (Key ID or Key ARN) of the KMS symmetric encryption customer managed key to use. Otherwise, you get an HTTP <code>400 Bad Request</code> error. The key alias format of the KMS key isn't supported. To encrypt new object copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer managed key</a>). The <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed key</a> (<code>aws/s3</code>) isn't supported. Your SSE-KMS configuration can only support 1 <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">customer managed key</a> per directory bucket for the lifetime of the bucket. After you specify a customer managed key for SSE-KMS as the bucket default encryption, you can't override the customer managed key for the bucket's SSE-KMS configuration. Then, when you specify server-side encryption settings for new object copies with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucket's default encryption configuration. </p> </note>"""
    target_key_prefix: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>Specifies the folder prefix that you want the objects to be copied into. For example, to copy objects into a folder named <code>Folder1</code> in the destination bucket, set the <code>TargetKeyPrefix</code> property to <code>Folder1</code>.</p>"""
    object_lock_legal_hold_status: NotRequired[
        "capo_s3_control.types.s3_object_lock_legal_hold_status.S3ObjectLockLegalHoldStatus"
    ]
    """<p>The legal hold status to be applied to all objects in the Batch Operations job.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    object_lock_mode: NotRequired[
        "capo_s3_control.types.s3_object_lock_mode.S3ObjectLockMode"
    ]
    """<p>The retention mode to be applied to all objects in the Batch Operations job.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    object_lock_retain_until_date: NotRequired[
        "capo_s3_control.types.time_stamp.TimeStamp"
    ]
    """<p>The date when the applied object retention configuration expires on all objects in the Batch Operations job.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    bucket_key_enabled: "capo_s3_control.types.boolean.Boolean"
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Amazon Web Services KMS (SSE-KMS). Setting this header to <code>true</code> causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS.</p> <p>Specifying this header with an <i>Copy</i> action doesn’t affect <i>bucket-level</i> settings for S3 Bucket Key.</p> <note> <p> <b>Directory buckets</b> - S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>. In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.</p> </note>"""
    checksum_algorithm: NotRequired[
        "capo_s3_control.types.s3_checksum_algorithm.S3ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    object_lock_event_hold: NotRequired[
        "capo_s3_control.types.s3_object_lock_event_hold.S3ObjectLockEventHold"
    ]
    """<p>The event hold status to be applied to all objects in the Batch Operations copy job. Set to <code>ON</code> to enable an event hold or <code>OFF</code> to disable it.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""
    object_lock_event_hold_duration: NotRequired[
        "capo_s3_control.types.s3_object_lock_event_hold_duration.S3ObjectLockEventHoldDuration"
    ]
    """<p>The event hold duration to be applied to all objects in the Batch Operations copy job. The duration specifies how long the object remains protected after the event hold is released.</p> <note> <p>This functionality is not supported by directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: S3CopyObjectOperation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "target_resource" in value:
        SubElement(el, "TargetResource").text = str(value["target_resource"])
    if "canned_access_control_list" in value:
        import capo_s3_control.types.s3_canned_access_control_list

        capo_s3_control.types.s3_canned_access_control_list.serialize_xml(
            value["canned_access_control_list"], el, "CannedAccessControlList"
        )
    if "access_control_grants" in value:
        import capo_s3_control.types.s3_grant_list

        capo_s3_control.types.s3_grant_list.serialize_xml(
            value["access_control_grants"], el, "AccessControlGrants"
        )
    if "metadata_directive" in value:
        import capo_s3_control.types.s3_metadata_directive

        capo_s3_control.types.s3_metadata_directive.serialize_xml(
            value["metadata_directive"], el, "MetadataDirective"
        )
    if "annotation_directive" in value:
        import capo_s3_control.types.s3_annotation_directive

        capo_s3_control.types.s3_annotation_directive.serialize_xml(
            value["annotation_directive"], el, "AnnotationDirective"
        )
    if "modified_since_constraint" in value:
        import capo_s3_control.types.time_stamp

        capo_s3_control.types.time_stamp.serialize_xml(
            value["modified_since_constraint"], el, "ModifiedSinceConstraint"
        )
    if "new_object_metadata" in value:
        import capo_s3_control.types.s3_object_metadata

        capo_s3_control.types.s3_object_metadata.serialize_xml(
            value["new_object_metadata"], el, "NewObjectMetadata"
        )
    if "new_object_tagging" in value:
        import capo_s3_control.types.s3_tag_set

        capo_s3_control.types.s3_tag_set.serialize_xml(
            value["new_object_tagging"], el, "NewObjectTagging"
        )
    if "redirect_location" in value:
        SubElement(el, "RedirectLocation").text = str(value["redirect_location"])
    SubElement(el, "RequesterPays").text = (
        "true" if value.get("requester_pays", False) else "false"
    )
    if "storage_class" in value:
        import capo_s3_control.types.s3_storage_class

        capo_s3_control.types.s3_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "un_modified_since_constraint" in value:
        import capo_s3_control.types.time_stamp

        capo_s3_control.types.time_stamp.serialize_xml(
            value["un_modified_since_constraint"], el, "UnModifiedSinceConstraint"
        )
    if "sse_aws_kms_key_id" in value:
        SubElement(el, "SSEAwsKmsKeyId").text = str(value["sse_aws_kms_key_id"])
    if "target_key_prefix" in value:
        SubElement(el, "TargetKeyPrefix").text = str(value["target_key_prefix"])
    if "object_lock_legal_hold_status" in value:
        import capo_s3_control.types.s3_object_lock_legal_hold_status

        capo_s3_control.types.s3_object_lock_legal_hold_status.serialize_xml(
            value["object_lock_legal_hold_status"], el, "ObjectLockLegalHoldStatus"
        )
    if "object_lock_mode" in value:
        import capo_s3_control.types.s3_object_lock_mode

        capo_s3_control.types.s3_object_lock_mode.serialize_xml(
            value["object_lock_mode"], el, "ObjectLockMode"
        )
    if "object_lock_retain_until_date" in value:
        import capo_s3_control.types.time_stamp

        capo_s3_control.types.time_stamp.serialize_xml(
            value["object_lock_retain_until_date"], el, "ObjectLockRetainUntilDate"
        )
    SubElement(el, "BucketKeyEnabled").text = (
        "true" if value.get("bucket_key_enabled", False) else "false"
    )
    if "checksum_algorithm" in value:
        import capo_s3_control.types.s3_checksum_algorithm

        capo_s3_control.types.s3_checksum_algorithm.serialize_xml(
            value["checksum_algorithm"], el, "ChecksumAlgorithm"
        )
    if "object_lock_event_hold" in value:
        import capo_s3_control.types.s3_object_lock_event_hold

        capo_s3_control.types.s3_object_lock_event_hold.serialize_xml(
            value["object_lock_event_hold"], el, "ObjectLockEventHold"
        )
    if "object_lock_event_hold_duration" in value:
        import capo_s3_control.types.s3_object_lock_event_hold_duration

        capo_s3_control.types.s3_object_lock_event_hold_duration.serialize_xml(
            value["object_lock_event_hold_duration"], el, "ObjectLockEventHoldDuration"
        )


def deserialize_xml(el: Element) -> S3CopyObjectOperation:
    out: S3CopyObjectOperation = {}  # type: ignore[typeddict-item]
    child_target_resource = el.find("TargetResource")
    if child_target_resource is not None:
        out["target_resource"] = str(child_target_resource.text or "")
    child_canned_access_control_list = el.find("CannedAccessControlList")
    if child_canned_access_control_list is not None:
        import capo_s3_control.types.s3_canned_access_control_list

        out["canned_access_control_list"] = (
            capo_s3_control.types.s3_canned_access_control_list.deserialize_xml(
                child_canned_access_control_list
            )
        )
    child_access_control_grants = el.find("AccessControlGrants")
    if child_access_control_grants is not None:
        import capo_s3_control.types.s3_grant_list

        out["access_control_grants"] = (
            capo_s3_control.types.s3_grant_list.deserialize_xml(
                child_access_control_grants
            )
        )
    child_metadata_directive = el.find("MetadataDirective")
    if child_metadata_directive is not None:
        import capo_s3_control.types.s3_metadata_directive

        out["metadata_directive"] = (
            capo_s3_control.types.s3_metadata_directive.deserialize_xml(
                child_metadata_directive
            )
        )
    child_annotation_directive = el.find("AnnotationDirective")
    if child_annotation_directive is not None:
        import capo_s3_control.types.s3_annotation_directive

        out["annotation_directive"] = (
            capo_s3_control.types.s3_annotation_directive.deserialize_xml(
                child_annotation_directive
            )
        )
    child_modified_since_constraint = el.find("ModifiedSinceConstraint")
    if child_modified_since_constraint is not None:
        import capo_s3_control.types.time_stamp

        out["modified_since_constraint"] = (
            capo_s3_control.types.time_stamp.deserialize_xml(
                child_modified_since_constraint
            )
        )
    child_new_object_metadata = el.find("NewObjectMetadata")
    if child_new_object_metadata is not None:
        import capo_s3_control.types.s3_object_metadata

        out["new_object_metadata"] = (
            capo_s3_control.types.s3_object_metadata.deserialize_xml(
                child_new_object_metadata
            )
        )
    child_new_object_tagging = el.find("NewObjectTagging")
    if child_new_object_tagging is not None:
        import capo_s3_control.types.s3_tag_set

        out["new_object_tagging"] = capo_s3_control.types.s3_tag_set.deserialize_xml(
            child_new_object_tagging
        )
    child_redirect_location = el.find("RedirectLocation")
    if child_redirect_location is not None:
        out["redirect_location"] = str(child_redirect_location.text or "")
    child_requester_pays = el.find("RequesterPays")
    if child_requester_pays is not None:
        out["requester_pays"] = (child_requester_pays.text or "").lower() == "true"
    else:
        out["requester_pays"] = False
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3_control.types.s3_storage_class

        out["storage_class"] = capo_s3_control.types.s3_storage_class.deserialize_xml(
            child_storage_class
        )
    child_un_modified_since_constraint = el.find("UnModifiedSinceConstraint")
    if child_un_modified_since_constraint is not None:
        import capo_s3_control.types.time_stamp

        out["un_modified_since_constraint"] = (
            capo_s3_control.types.time_stamp.deserialize_xml(
                child_un_modified_since_constraint
            )
        )
    child_sse_aws_kms_key_id = el.find("SSEAwsKmsKeyId")
    if child_sse_aws_kms_key_id is not None:
        out["sse_aws_kms_key_id"] = str(child_sse_aws_kms_key_id.text or "")
    child_target_key_prefix = el.find("TargetKeyPrefix")
    if child_target_key_prefix is not None:
        out["target_key_prefix"] = str(child_target_key_prefix.text or "")
    child_object_lock_legal_hold_status = el.find("ObjectLockLegalHoldStatus")
    if child_object_lock_legal_hold_status is not None:
        import capo_s3_control.types.s3_object_lock_legal_hold_status

        out["object_lock_legal_hold_status"] = (
            capo_s3_control.types.s3_object_lock_legal_hold_status.deserialize_xml(
                child_object_lock_legal_hold_status
            )
        )
    child_object_lock_mode = el.find("ObjectLockMode")
    if child_object_lock_mode is not None:
        import capo_s3_control.types.s3_object_lock_mode

        out["object_lock_mode"] = (
            capo_s3_control.types.s3_object_lock_mode.deserialize_xml(
                child_object_lock_mode
            )
        )
    child_object_lock_retain_until_date = el.find("ObjectLockRetainUntilDate")
    if child_object_lock_retain_until_date is not None:
        import capo_s3_control.types.time_stamp

        out["object_lock_retain_until_date"] = (
            capo_s3_control.types.time_stamp.deserialize_xml(
                child_object_lock_retain_until_date
            )
        )
    child_bucket_key_enabled = el.find("BucketKeyEnabled")
    if child_bucket_key_enabled is not None:
        out["bucket_key_enabled"] = (
            child_bucket_key_enabled.text or ""
        ).lower() == "true"
    else:
        out["bucket_key_enabled"] = False
    child_checksum_algorithm = el.find("ChecksumAlgorithm")
    if child_checksum_algorithm is not None:
        import capo_s3_control.types.s3_checksum_algorithm

        out["checksum_algorithm"] = (
            capo_s3_control.types.s3_checksum_algorithm.deserialize_xml(
                child_checksum_algorithm
            )
        )
    child_object_lock_event_hold = el.find("ObjectLockEventHold")
    if child_object_lock_event_hold is not None:
        import capo_s3_control.types.s3_object_lock_event_hold

        out["object_lock_event_hold"] = (
            capo_s3_control.types.s3_object_lock_event_hold.deserialize_xml(
                child_object_lock_event_hold
            )
        )
    child_object_lock_event_hold_duration = el.find("ObjectLockEventHoldDuration")
    if child_object_lock_event_hold_duration is not None:
        import capo_s3_control.types.s3_object_lock_event_hold_duration

        out["object_lock_event_hold_duration"] = (
            capo_s3_control.types.s3_object_lock_event_hold_duration.deserialize_xml(
                child_object_lock_event_hold_duration
            )
        )
    return out
