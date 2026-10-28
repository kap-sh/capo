"""Generated from Smithy shape ``com.amazonaws.grafana#IdpMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_grafana.errors import DeserializationError, SerializationError
from capo_grafana.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_grafana.types.idp_metadata_url


class IdpMetadataUrlMember(TypedDict, closed=True):
    url: "capo_grafana.types.idp_metadata_url.IdpMetadataUrl"


class IdpMetadataXmlMember(TypedDict, closed=True):
    xml: "str"


IdpMetadata: TypeAlias = (
    IdpMetadataUrlMember | IdpMetadataXmlMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IdpMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IdpMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "url" in value:
        return {"url": value["url"]}
    elif "xml" in value:
        return {"xml": value["xml"]}
    else:
        raise SerializationError("IdpMetadata: no variant present")


def deserialize_json(data: dict) -> IdpMetadata:
    if data.get("url") is not None:
        return {"url": data["url"]}
    elif data.get("xml") is not None:
        return {"xml": data["xml"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IdpMetadata: no recognized variant key")
