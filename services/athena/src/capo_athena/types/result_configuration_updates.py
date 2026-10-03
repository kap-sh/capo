"""Generated from Smithy shape ``com.amazonaws.athena#ResultConfigurationUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.acl_configuration
    import capo_athena.types.aws_account_id
    import capo_athena.types.boxed_boolean
    import capo_athena.types.encryption_configuration
    import capo_athena.types.result_output_location


class ResultConfigurationUpdates(TypedDict, closed=True):
    output_location: NotRequired[
        "capo_athena.types.result_output_location.ResultOutputLocation"
    ]
    """<p>The location in Amazon S3 where your query and calculation results are stored, such as <code>s3://path/to/query/bucket/</code>. If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The "workgroup settings override" is specified in <code>EnforceWorkGroupConfiguration</code> (true/false) in the <code>WorkGroupConfiguration</code>. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    remove_output_location: NotRequired["capo_athena.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to "true", indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the <code>OutputLocation</code> in <code>ResultConfigurationUpdates</code> (the client-side setting), the <code>OutputLocation</code> in the workgroup's <code>ResultConfiguration</code> will be updated with the new value. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_athena.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for query and calculation results.</p>"""
    remove_encryption_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to "true", indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the <code>EncryptionConfiguration</code> in <code>ResultConfigurationUpdates</code> (the client-side setting), the <code>EncryptionConfiguration</code> in the workgroup's <code>ResultConfiguration</code> will be updated with the new value. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    expected_bucket_owner: NotRequired["capo_athena.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID that you expect to be the owner of the Amazon S3 bucket specified by <a>ResultConfiguration$OutputLocation</a>. If set, Athena uses the value for <code>ExpectedBucketOwner</code> when it makes Amazon S3 calls to your specified output location. If the <code>ExpectedBucketOwner</code> Amazon Web Services account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.</p> <p>If workgroup settings override client-side settings, then the query uses the <code>ExpectedBucketOwner</code> setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a> and <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    remove_expected_bucket_owner: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to "true", removes the Amazon Web Services account ID previously specified for <a>ResultConfiguration$ExpectedBucketOwner</a>. If set to "false" or not set, and a value is present in the <code>ExpectedBucketOwner</code> in <code>ResultConfigurationUpdates</code> (the client-side setting), the <code>ExpectedBucketOwner</code> in the workgroup's <code>ResultConfiguration</code> is updated with the new value. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    acl_configuration: NotRequired[
        "capo_athena.types.acl_configuration.AclConfiguration"
    ]
    """<p>The ACL configuration for the query results.</p>"""
    remove_acl_configuration: NotRequired[
        "capo_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to <code>true</code>, indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null. If set to <code>false</code> or not set, and a value is present in the <code>AclConfiguration</code> of <code>ResultConfigurationUpdates</code>, the <code>AclConfiguration</code> in the workgroup's <code>ResultConfiguration</code> is updated with the new value. For more information, see <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultConfigurationUpdates) -> dict:
    out: dict = {}
    if "output_location" in value:
        out["OutputLocation"] = value["output_location"]
    if "remove_output_location" in value:
        out["RemoveOutputLocation"] = value["remove_output_location"]
    if "encryption_configuration" in value:
        import capo_athena.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_athena.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "remove_encryption_configuration" in value:
        out["RemoveEncryptionConfiguration"] = value["remove_encryption_configuration"]
    if "expected_bucket_owner" in value:
        out["ExpectedBucketOwner"] = value["expected_bucket_owner"]
    if "remove_expected_bucket_owner" in value:
        out["RemoveExpectedBucketOwner"] = value["remove_expected_bucket_owner"]
    if "acl_configuration" in value:
        import capo_athena.types.acl_configuration

        out["AclConfiguration"] = (
            capo_athena.types.acl_configuration.serialize_aws_json_1_1(
                value["acl_configuration"]
            )
        )
    if "remove_acl_configuration" in value:
        out["RemoveAclConfiguration"] = value["remove_acl_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultConfigurationUpdates:
    out: ResultConfigurationUpdates = {}  # type: ignore[typeddict-item]
    if data.get("OutputLocation") is not None:
        out["output_location"] = data["OutputLocation"]
    if data.get("RemoveOutputLocation") is not None:
        out["remove_output_location"] = data["RemoveOutputLocation"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_athena.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_athena.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("RemoveEncryptionConfiguration") is not None:
        out["remove_encryption_configuration"] = data["RemoveEncryptionConfiguration"]
    if data.get("ExpectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["ExpectedBucketOwner"]
    if data.get("RemoveExpectedBucketOwner") is not None:
        out["remove_expected_bucket_owner"] = data["RemoveExpectedBucketOwner"]
    if data.get("AclConfiguration") is not None:
        import capo_athena.types.acl_configuration

        out["acl_configuration"] = (
            capo_athena.types.acl_configuration.deserialize_aws_json_1_1(
                data["AclConfiguration"]
            )
        )
    if data.get("RemoveAclConfiguration") is not None:
        out["remove_acl_configuration"] = data["RemoveAclConfiguration"]
    return out
