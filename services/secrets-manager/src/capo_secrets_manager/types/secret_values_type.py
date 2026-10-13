"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretValuesType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_value_entry

SecretValuesType: TypeAlias = list[
    "capo_secrets_manager.types.secret_value_entry.SecretValueEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretValuesType) -> list:
    import capo_secrets_manager.types.secret_value_entry

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.secret_value_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecretValuesType:
    import capo_secrets_manager.types.secret_value_entry

    out: SecretValuesType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_secrets_manager.types.secret_value_entry.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: SecretValuesType) -> list[Any]:
    import capo_secrets_manager.types.secret_value_entry

    return [
        capo_secrets_manager.types.secret_value_entry.redact_sensitive(item)
        for item in value
    ]
