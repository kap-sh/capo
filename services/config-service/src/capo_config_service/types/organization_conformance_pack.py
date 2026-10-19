"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.date
    import capo_config_service.types.delivery_s3_bucket
    import capo_config_service.types.delivery_s3_key_prefix
    import capo_config_service.types.excluded_accounts
    import capo_config_service.types.organization_conformance_pack_name
    import capo_config_service.types.string_with_char_limit256


class OrganizationConformancePack(TypedDict, closed=True):
    organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>The name you assign to an organization conformance pack.</p>"""
    organization_conformance_pack_arn: (
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>Amazon Resource Name (ARN) of organization conformance pack.</p>"""
    delivery_s3_bucket: NotRequired[
        "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
    ]
    """<p>The name of the Amazon S3 bucket where Config stores conformance pack templates. </p> <note> <p>This field is optional.</p> </note>"""
    delivery_s3_key_prefix: NotRequired[
        "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
    ]
    """<p>Any folder structure you want to add to an Amazon S3 bucket.</p> <note> <p>This field is optional.</p> </note>"""
    conformance_pack_input_parameters: NotRequired[
        "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
    ]
    """<p>A list of <code>ConformancePackInputParameter</code> objects.</p>"""
    excluded_accounts: NotRequired[
        "capo_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A comma-separated list of accounts excluded from organization conformance pack.</p>"""
    last_update_time: "capo_config_service.types.date.Date"
    """<p>Last time when organization conformation pack was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePack) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    out["OrganizationConformancePackArn"] = value["organization_conformance_pack_arn"]
    if "delivery_s3_bucket" in value:
        out["DeliveryS3Bucket"] = value["delivery_s3_bucket"]
    if "delivery_s3_key_prefix" in value:
        out["DeliveryS3KeyPrefix"] = value["delivery_s3_key_prefix"]
    if "conformance_pack_input_parameters" in value:
        import capo_config_service.types.conformance_pack_input_parameters

        out["ConformancePackInputParameters"] = (
            capo_config_service.types.conformance_pack_input_parameters.serialize_aws_json_1_1(
                value["conformance_pack_input_parameters"]
            )
        )
    if "excluded_accounts" in value:
        import capo_config_service.types.excluded_accounts

        out["ExcludedAccounts"] = (
            capo_config_service.types.excluded_accounts.serialize_aws_json_1_1(
                value["excluded_accounts"]
            )
        )
    import capo_config_service.types.date

    out["LastUpdateTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
        value["last_update_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConformancePack:
    out: OrganizationConformancePack = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackName") is not None:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        out["organization_conformance_pack_name"] = ""
    if data.get("OrganizationConformancePackArn") is not None:
        out["organization_conformance_pack_arn"] = data[
            "OrganizationConformancePackArn"
        ]
    else:
        out["organization_conformance_pack_arn"] = ""
    if data.get("DeliveryS3Bucket") is not None:
        out["delivery_s3_bucket"] = data["DeliveryS3Bucket"]
    if data.get("DeliveryS3KeyPrefix") is not None:
        out["delivery_s3_key_prefix"] = data["DeliveryS3KeyPrefix"]
    if data.get("ConformancePackInputParameters") is not None:
        import capo_config_service.types.conformance_pack_input_parameters

        out["conformance_pack_input_parameters"] = (
            capo_config_service.types.conformance_pack_input_parameters.deserialize_aws_json_1_1(
                data["ConformancePackInputParameters"]
            )
        )
    if data.get("ExcludedAccounts") is not None:
        import capo_config_service.types.excluded_accounts

        out["excluded_accounts"] = (
            capo_config_service.types.excluded_accounts.deserialize_aws_json_1_1(
                data["ExcludedAccounts"]
            )
        )
    if data.get("LastUpdateTime") is not None:
        import capo_config_service.types.date

        out["last_update_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    else:
        import datetime

        out["last_update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
