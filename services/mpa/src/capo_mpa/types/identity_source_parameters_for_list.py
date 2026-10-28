"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceParametersForList``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, SerializationError
from capo_mpa.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mpa.types.iam_identity_center_for_list


class IdentitySourceParametersForListIamIdentityCenterMember(TypedDict, closed=True):
    IamIdentityCenter: (
        "capo_mpa.types.iam_identity_center_for_list.IamIdentityCenterForList"
    )


IdentitySourceParametersForList: TypeAlias = (
    IdentitySourceParametersForListIamIdentityCenterMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceParametersForList) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IdentitySourceParametersForList: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "IamIdentityCenter" in value:
        import capo_mpa.types.iam_identity_center_for_list

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_list.serialize_json(
                value["IamIdentityCenter"]
            )
        }
    else:
        raise SerializationError("IdentitySourceParametersForList: no variant present")


def deserialize_json(data: dict) -> IdentitySourceParametersForList:
    if data.get("IamIdentityCenter") is not None:
        import capo_mpa.types.iam_identity_center_for_list

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_list.deserialize_json(
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
            "IdentitySourceParametersForList: no recognized variant key"
        )
