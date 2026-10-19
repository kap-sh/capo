"""Generated from Smithy shape ``com.amazonaws.timestreamquery#AccountSettingsNotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.sns_configuration


class AccountSettingsNotificationConfiguration(TypedDict, closed=True):
    sns_configuration: NotRequired[
        "capo_timestream_query.types.sns_configuration.SnsConfiguration"
    ]
    role_arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>An Amazon Resource Name (ARN) that grants Timestream permission to publish notifications. This field is only visible if SNS Topic is provided when updating the account settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSettingsNotificationConfiguration) -> dict:
    out: dict = {}
    if "sns_configuration" in value:
        import capo_timestream_query.types.sns_configuration

        out["SnsConfiguration"] = (
            capo_timestream_query.types.sns_configuration.serialize_aws_json_1_0(
                value["sns_configuration"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSettingsNotificationConfiguration:
    out: AccountSettingsNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnsConfiguration") is not None:
        import capo_timestream_query.types.sns_configuration

        out["sns_configuration"] = (
            capo_timestream_query.types.sns_configuration.deserialize_aws_json_1_0(
                data["SnsConfiguration"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    return out
