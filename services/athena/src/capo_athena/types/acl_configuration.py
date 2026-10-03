"""Generated from Smithy shape ``com.amazonaws.athena#AclConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.s3_acl_option


class AclConfiguration(TypedDict, closed=True):
    s3_acl_option: "capo_athena.types.s3_acl_option.S3AclOption"
    """<p>The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is <code>BUCKET_OWNER_FULL_CONTROL</code>. If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroup's settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl">Canned ACL</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AclConfiguration) -> dict:
    out: dict = {}
    import capo_athena.types.s3_acl_option

    out["S3AclOption"] = capo_athena.types.s3_acl_option.serialize_aws_json_1_1(
        value["s3_acl_option"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AclConfiguration:
    out: AclConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("S3AclOption") is not None:
        import capo_athena.types.s3_acl_option

        out["s3_acl_option"] = capo_athena.types.s3_acl_option.deserialize_aws_json_1_1(
            data["S3AclOption"]
        )
    else:
        raise DeserializationError("AclConfiguration.s3_acl_option required")
    return out
