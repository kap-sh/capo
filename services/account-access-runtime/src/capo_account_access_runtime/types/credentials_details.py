"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#CredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_account_access_runtime.errors import DeserializationError, SerializationError
from capo_account_access_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_account_access_runtime.types.programmatic_access_details


class CredentialsDetailsProgrammaticAccessMember(TypedDict, closed=True):
    programmaticAccess: "capo_account_access_runtime.types.programmatic_access_details.ProgrammaticAccessDetails"


CredentialsDetails: TypeAlias = (
    CredentialsDetailsProgrammaticAccessMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CredentialsDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "programmaticAccess" in value:
        import capo_account_access_runtime.types.programmatic_access_details

        return {
            "programmaticAccess": capo_account_access_runtime.types.programmatic_access_details.serialize_json(
                value["programmaticAccess"]
            )
        }
    else:
        raise SerializationError("CredentialsDetails: no variant present")


def deserialize_json(data: dict) -> CredentialsDetails:
    if data.get("programmaticAccess") is not None:
        import capo_account_access_runtime.types.programmatic_access_details

        return {
            "programmaticAccess": capo_account_access_runtime.types.programmatic_access_details.deserialize_json(
                data["programmaticAccess"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CredentialsDetails: no recognized variant key")
