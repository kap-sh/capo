"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ClientIds``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.client_id

ClientIds: TypeAlias = list["capo_verifiedpermissions.types.client_id.ClientId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClientIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ClientIds:
    return [item for item in data if item is not None]


def redact_sensitive(value: ClientIds) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
