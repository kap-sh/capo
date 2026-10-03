"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.access_rules
    import capo_lightsail.types.bucket_access_log_config
    import capo_lightsail.types.bucket_cors_config
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.partner_id_list


class UpdateBucketRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket to update.</p>"""
    access_rules: NotRequired["capo_lightsail.types.access_rules.AccessRules"]
    """<p>An object that sets the public accessibility of objects in the specified bucket.</p>"""
    versioning: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Specifies whether to enable or suspend versioning of objects in the bucket.</p> <p>The following options can be specified:</p> <ul> <li> <p> <code>Enabled</code> - Enables versioning of objects in the specified bucket.</p> </li> <li> <p> <code>Suspended</code> - Suspends versioning of objects in the specified bucket. Existing object versions are retained.</p> </li> </ul>"""
    readonly_access_accounts: NotRequired[
        "capo_lightsail.types.partner_id_list.PartnerIdList"
    ]
    """<p>An array of strings to specify the Amazon Web Services account IDs that can access the bucket.</p> <p>You can give a maximum of 10 Amazon Web Services accounts access to a bucket.</p>"""
    access_log_config: NotRequired[
        "capo_lightsail.types.bucket_access_log_config.BucketAccessLogConfig"
    ]
    """<p>An object that describes the access log configuration for the bucket.</p>"""
    cors: NotRequired["capo_lightsail.types.bucket_cors_config.BucketCorsConfig"]
    """<p>Sets the cross-origin resource sharing (CORS) configuration for your bucket. If a CORS configuration exists, it is replaced with the specified configuration. For AWS CLI operations, this parameter can also be passed as a file. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html">Configuring cross-origin resource sharing (CORS)</a>.</p> <note> <p>CORS information is only returned in a response when you update the CORS policy.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBucketRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "access_rules" in value:
        import capo_lightsail.types.access_rules

        out["accessRules"] = capo_lightsail.types.access_rules.serialize_aws_json_1_1(
            value["access_rules"]
        )
    if "versioning" in value:
        out["versioning"] = value["versioning"]
    if "readonly_access_accounts" in value:
        import capo_lightsail.types.partner_id_list

        out["readonlyAccessAccounts"] = (
            capo_lightsail.types.partner_id_list.serialize_aws_json_1_1(
                value["readonly_access_accounts"]
            )
        )
    if "access_log_config" in value:
        import capo_lightsail.types.bucket_access_log_config

        out["accessLogConfig"] = (
            capo_lightsail.types.bucket_access_log_config.serialize_aws_json_1_1(
                value["access_log_config"]
            )
        )
    if "cors" in value:
        import capo_lightsail.types.bucket_cors_config

        out["cors"] = capo_lightsail.types.bucket_cors_config.serialize_aws_json_1_1(
            value["cors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBucketRequest:
    out: UpdateBucketRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("UpdateBucketRequest.bucket_name required")
    if data.get("accessRules") is not None:
        import capo_lightsail.types.access_rules

        out["access_rules"] = (
            capo_lightsail.types.access_rules.deserialize_aws_json_1_1(
                data["accessRules"]
            )
        )
    if data.get("versioning") is not None:
        out["versioning"] = data["versioning"]
    if data.get("readonlyAccessAccounts") is not None:
        import capo_lightsail.types.partner_id_list

        out["readonly_access_accounts"] = (
            capo_lightsail.types.partner_id_list.deserialize_aws_json_1_1(
                data["readonlyAccessAccounts"]
            )
        )
    if data.get("accessLogConfig") is not None:
        import capo_lightsail.types.bucket_access_log_config

        out["access_log_config"] = (
            capo_lightsail.types.bucket_access_log_config.deserialize_aws_json_1_1(
                data["accessLogConfig"]
            )
        )
    if data.get("cors") is not None:
        import capo_lightsail.types.bucket_cors_config

        out["cors"] = capo_lightsail.types.bucket_cors_config.deserialize_aws_json_1_1(
            data["cors"]
        )
    return out
