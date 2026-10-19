"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethod``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError
from capo_sso_admin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sso_admin.types.iam_authentication_method


class _AuthenticationMethod_Iam(TypedDict, closed=True):
    Iam: "capo_sso_admin.types.iam_authentication_method.IamAuthenticationMethod"


AuthenticationMethod: TypeAlias = _AuthenticationMethod_Iam | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethod) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AuthenticationMethod: cannot serialize unknown variant {value.name!r}"
        )
    elif "Iam" in value:
        import capo_sso_admin.types.iam_authentication_method

        return {
            "Iam": capo_sso_admin.types.iam_authentication_method.serialize_aws_json_1_1(
                value["Iam"]
            )
        }
    else:
        raise SerializationError("AuthenticationMethod: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMethod:
    if data.get("Iam") is not None:
        import capo_sso_admin.types.iam_authentication_method

        return {
            "Iam": capo_sso_admin.types.iam_authentication_method.deserialize_aws_json_1_1(
                data["Iam"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AuthenticationMethod: no recognized variant key")
