"""Generated from Smithy shape ``com.amazonaws.securityhub#CspmProviderDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.azure_detail


class _CspmProviderDetail_Azure(TypedDict, closed=True):
    Azure: "capo_securityhub.types.azure_detail.AzureDetail"


CspmProviderDetail: TypeAlias = _CspmProviderDetail_Azure | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CspmProviderDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CspmProviderDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Azure" in value:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.serialize_json(value["Azure"])
        }
    else:
        raise SerializationError("CspmProviderDetail: no variant present")


def deserialize_json(data: dict) -> CspmProviderDetail:
    if data.get("Azure") is not None:
        import capo_securityhub.types.azure_detail

        return {
            "Azure": capo_securityhub.types.azure_detail.deserialize_json(data["Azure"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CspmProviderDetail: no recognized variant key")
