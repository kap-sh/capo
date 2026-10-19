"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseWalletInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.general_input_string
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.sensitive_string
    import capo_odb.types.wallet_password_source
    import capo_odb.types.wallet_password_source_configuration_input
    import capo_odb.types.wallet_type


class CreateAutonomousDatabaseWalletInput(TypedDict, closed=True):
    autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to create a wallet for.</p>"""
    wallet_type: NotRequired["capo_odb.types.wallet_type.WalletType"]
    """<p>The type of wallet to create, either a regional wallet or an instance wallet.</p>"""
    password: NotRequired["capo_odb.types.sensitive_string.SensitiveString"]
    """<p>The password to encrypt the keys inside the wallet.</p>"""
    password_source: NotRequired[
        "capo_odb.types.wallet_password_source.WalletPasswordSource"
    ]
    """<p>The source of the password for encrypting the wallet. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the password is retrieved from an Amazon Web Services Secrets Manager secret.</p>"""
    password_source_configuration: NotRequired[
        "capo_odb.types.wallet_password_source_configuration_input.WalletPasswordSourceConfigurationInput"
    ]
    """<p>The configuration of the password source for the Autonomous Database wallet.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A client-provided token to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseWalletInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "wallet_type" in value:
        import capo_odb.types.wallet_type

        out["walletType"] = capo_odb.types.wallet_type.serialize_aws_json_1_0(
            value["wallet_type"]
        )
    if "password" in value:
        out["password"] = value["password"]
    if "password_source" in value:
        import capo_odb.types.wallet_password_source

        out["passwordSource"] = (
            capo_odb.types.wallet_password_source.serialize_aws_json_1_0(
                value["password_source"]
            )
        )
    if "password_source_configuration" in value:
        import capo_odb.types.wallet_password_source_configuration_input

        out["passwordSourceConfiguration"] = (
            capo_odb.types.wallet_password_source_configuration_input.serialize_aws_json_1_0(
                value["password_source_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseWalletInput:
    out: CreateAutonomousDatabaseWalletInput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseId") is not None:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        out["autonomous_database_id"] = ""
    if data.get("walletType") is not None:
        import capo_odb.types.wallet_type

        out["wallet_type"] = capo_odb.types.wallet_type.deserialize_aws_json_1_0(
            data["walletType"]
        )
    if data.get("password") is not None:
        out["password"] = data["password"]
    if data.get("passwordSource") is not None:
        import capo_odb.types.wallet_password_source

        out["password_source"] = (
            capo_odb.types.wallet_password_source.deserialize_aws_json_1_0(
                data["passwordSource"]
            )
        )
    if data.get("passwordSourceConfiguration") is not None:
        import capo_odb.types.wallet_password_source_configuration_input

        out["password_source_configuration"] = (
            capo_odb.types.wallet_password_source_configuration_input.deserialize_aws_json_1_0(
                data["passwordSourceConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateAutonomousDatabaseWalletInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
