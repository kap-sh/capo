"""Generated from Smithy shape ``com.amazonaws.datazone#AwsAccount``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.parameter_store_path


class _AwsAccount_awsAccountId(TypedDict, closed=True):
    awsAccountId: "capo_datazone.types.aws_account_id.AwsAccountId"


class _AwsAccount_awsAccountIdPath(TypedDict, closed=True):
    awsAccountIdPath: "capo_datazone.types.parameter_store_path.ParameterStorePath"


AwsAccount: TypeAlias = (
    _AwsAccount_awsAccountId | _AwsAccount_awsAccountIdPath | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AwsAccount) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AwsAccount: cannot serialize unknown variant {value.name!r}"
        )
    elif "awsAccountId" in value:
        return {"awsAccountId": value["awsAccountId"]}
    elif "awsAccountIdPath" in value:
        return {"awsAccountIdPath": value["awsAccountIdPath"]}
    else:
        raise SerializationError("AwsAccount: no variant present")


def deserialize_json(data: dict) -> AwsAccount:
    if data.get("awsAccountId") is not None:
        return {"awsAccountId": data["awsAccountId"]}
    elif data.get("awsAccountIdPath") is not None:
        return {"awsAccountIdPath": data["awsAccountIdPath"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AwsAccount: no recognized variant key")
