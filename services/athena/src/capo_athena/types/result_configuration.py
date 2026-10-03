"""Generated from Smithy shape ``com.amazonaws.athena#ResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.acl_configuration
    import capo_athena.types.aws_account_id
    import capo_athena.types.encryption_configuration
    import capo_athena.types.result_output_location


class ResultConfiguration(TypedDict, closed=True):
    output_location: NotRequired[
        "capo_athena.types.result_output_location.ResultOutputLocation"
    ]
    """<p>The location in Amazon S3 where your query and calculation results are stored, such as <code>s3://path/to/query/bucket/</code>. To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using <a>WorkGroupConfiguration</a>. If none of them is set, Athena issues an error that no output location is provided. If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>.</p>"""
    encryption_configuration: NotRequired[
        "capo_athena.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>If query and calculation results are encrypted in Amazon S3, indicates the encryption option used (for example, <code>SSE_KMS</code> or <code>CSE_KMS</code>) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a> and <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    expected_bucket_owner: NotRequired["capo_athena.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID that you expect to be the owner of the Amazon S3 bucket specified by <a>ResultConfiguration$OutputLocation</a>. If set, Athena uses the value for <code>ExpectedBucketOwner</code> when it makes Amazon S3 calls to your specified output location. If the <code>ExpectedBucketOwner</code> Amazon Web Services account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.</p> <p>This is a client-side setting. If workgroup settings override client-side settings, then the query uses the <code>ExpectedBucketOwner</code> setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a> and <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""
    acl_configuration: NotRequired[
        "capo_athena.types.acl_configuration.AclConfiguration"
    ]
    """<p>Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results. Currently the only supported canned ACL is <code>BUCKET_OWNER_FULL_CONTROL</code>. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. For more information, see <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a> and <a href="https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html">Workgroup Settings Override Client-Side Settings</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultConfiguration) -> dict:
    out: dict = {}
    if "output_location" in value:
        out["OutputLocation"] = value["output_location"]
    if "encryption_configuration" in value:
        import capo_athena.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_athena.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "expected_bucket_owner" in value:
        out["ExpectedBucketOwner"] = value["expected_bucket_owner"]
    if "acl_configuration" in value:
        import capo_athena.types.acl_configuration

        out["AclConfiguration"] = (
            capo_athena.types.acl_configuration.serialize_aws_json_1_1(
                value["acl_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultConfiguration:
    out: ResultConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("OutputLocation") is not None:
        out["output_location"] = data["OutputLocation"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_athena.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_athena.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("ExpectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["ExpectedBucketOwner"]
    if data.get("AclConfiguration") is not None:
        import capo_athena.types.acl_configuration

        out["acl_configuration"] = (
            capo_athena.types.acl_configuration.deserialize_aws_json_1_1(
                data["AclConfiguration"]
            )
        )
    return out
