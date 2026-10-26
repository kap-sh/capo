"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceParametersForGet``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, SerializationError
from capo_mpa.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mpa.types.iam_identity_center_for_get


class _IdentitySourceParametersForGet_IamIdentityCenter(TypedDict, closed=True):
    IamIdentityCenter: (
        "capo_mpa.types.iam_identity_center_for_get.IamIdentityCenterForGet"
    )


IdentitySourceParametersForGet: TypeAlias = (
    _IdentitySourceParametersForGet_IamIdentityCenter | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceParametersForGet) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IdentitySourceParametersForGet: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "IamIdentityCenter" in value:
        import capo_mpa.types.iam_identity_center_for_get

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_get.serialize_json(
                value["IamIdentityCenter"]
            )
        }
    else:
        raise SerializationError("IdentitySourceParametersForGet: no variant present")


def deserialize_json(data: dict) -> IdentitySourceParametersForGet:
    if data.get("IamIdentityCenter") is not None:
        import capo_mpa.types.iam_identity_center_for_get

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_get.deserialize_json(
                data["IamIdentityCenter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IdentitySourceParametersForGet: no recognized variant key"
        )
