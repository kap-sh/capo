"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentAssociationContents``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.amazon_connect_guide_association_data


class _ContentAssociationContents_amazonConnectGuideAssociation(TypedDict, closed=True):
    amazonConnectGuideAssociation: "capo_qconnect.types.amazon_connect_guide_association_data.AmazonConnectGuideAssociationData"


ContentAssociationContents: TypeAlias = (
    _ContentAssociationContents_amazonConnectGuideAssociation | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentAssociationContents) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ContentAssociationContents: cannot serialize unknown variant {value.name!r}"
        )
    elif "amazonConnectGuideAssociation" in value:
        import capo_qconnect.types.amazon_connect_guide_association_data

        return {
            "amazonConnectGuideAssociation": capo_qconnect.types.amazon_connect_guide_association_data.serialize_json(
                value["amazonConnectGuideAssociation"]
            )
        }
    else:
        raise SerializationError("ContentAssociationContents: no variant present")


def deserialize_json(data: dict) -> ContentAssociationContents:
    if data.get("amazonConnectGuideAssociation") is not None:
        import capo_qconnect.types.amazon_connect_guide_association_data

        return {
            "amazonConnectGuideAssociation": capo_qconnect.types.amazon_connect_guide_association_data.deserialize_json(
                data["amazonConnectGuideAssociation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ContentAssociationContents: no recognized variant key"
        )
