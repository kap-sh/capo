"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn
    import capo_license_manager.types.arn_list
    import capo_license_manager.types.client_token
    import capo_license_manager.types.integer
    import capo_license_manager.types.max_size3_string_list


class CreateTokenRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license. The ARN is mapped to the aud claim of the JWT token.</p>"""
    role_arns: NotRequired["capo_license_manager.types.arn_list.ArnList"]
    """<p>Amazon Resource Name (ARN) of the IAM roles to embed in the token. License Manager does not check whether the roles are in use.</p>"""
    expiration_in_days: NotRequired["capo_license_manager.types.integer.Integer"]
    """<p>Token expiration, in days, counted from token creation. The default is 365 days.</p>"""
    token_properties: NotRequired[
        "capo_license_manager.types.max_size3_string_list.MaxSize3StringList"
    ]
    """<p>Data specified by the caller to be included in the JWT token. The data is mapped to the amr claim of the JWT token.</p>"""
    client_token: "capo_license_manager.types.client_token.ClientToken"
    """<p>Idempotency token, valid for 10 minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTokenRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    if "role_arns" in value:
        import capo_license_manager.types.arn_list

        out["RoleArns"] = capo_license_manager.types.arn_list.serialize_aws_json_1_1(
            value["role_arns"]
        )
    if "expiration_in_days" in value:
        out["ExpirationInDays"] = value["expiration_in_days"]
    if "token_properties" in value:
        import capo_license_manager.types.max_size3_string_list

        out["TokenProperties"] = (
            capo_license_manager.types.max_size3_string_list.serialize_aws_json_1_1(
                value["token_properties"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTokenRequest:
    out: CreateTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    if data.get("RoleArns") is not None:
        import capo_license_manager.types.arn_list

        out["role_arns"] = capo_license_manager.types.arn_list.deserialize_aws_json_1_1(
            data["RoleArns"]
        )
    if data.get("ExpirationInDays") is not None:
        out["expiration_in_days"] = data["ExpirationInDays"]
    if data.get("TokenProperties") is not None:
        import capo_license_manager.types.max_size3_string_list

        out["token_properties"] = (
            capo_license_manager.types.max_size3_string_list.deserialize_aws_json_1_1(
                data["TokenProperties"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
