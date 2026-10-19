"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseWalletOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_wallet_file


class CreateAutonomousDatabaseWalletOutput(TypedDict, closed=True):
    autonomous_database_wallet_file: (
        "capo_odb.types.autonomous_database_wallet_file.AutonomousDatabaseWalletFile"
    )
    """<p>The generated wallet file for the Autonomous Database, returned as a compressed archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseWalletOutput) -> dict:
    out: dict = {}
    import capo_odb.types.autonomous_database_wallet_file

    out["autonomousDatabaseWalletFile"] = (
        capo_odb.types.autonomous_database_wallet_file.serialize_aws_json_1_0(
            value["autonomous_database_wallet_file"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseWalletOutput:
    out: CreateAutonomousDatabaseWalletOutput = {}  # type: ignore[typeddict-item]
    if data.get("autonomousDatabaseWalletFile") is not None:
        import capo_odb.types.autonomous_database_wallet_file

        out["autonomous_database_wallet_file"] = (
            capo_odb.types.autonomous_database_wallet_file.deserialize_aws_json_1_0(
                data["autonomousDatabaseWalletFile"]
            )
        )
    else:
        out["autonomous_database_wallet_file"] = b""
    return out


def redact_sensitive(value: CreateAutonomousDatabaseWalletOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "autonomous_database_wallet_file" in value:
        out["autonomous_database_wallet_file"] = "*** Sensitive Data Redacted ***"
    return out
