"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AclGrantee``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.acl_canonical_id
    import capo_accessanalyzer.types.acl_uri


class AclGranteeIdMember(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.acl_canonical_id.AclCanonicalId"


class AclGranteeUriMember(TypedDict, closed=True):
    uri: "capo_accessanalyzer.types.acl_uri.AclUri"


AclGrantee: TypeAlias = AclGranteeIdMember | AclGranteeUriMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: AclGrantee) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AclGrantee: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "id" in value:
        return {"id": value["id"]}
    elif "uri" in value:
        return {"uri": value["uri"]}
    else:
        raise SerializationError("AclGrantee: no variant present")


def deserialize_json(data: dict) -> AclGrantee:
    if data.get("id") is not None:
        return {"id": data["id"]}
    elif data.get("uri") is not None:
        return {"uri": data["uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AclGrantee: no recognized variant key")
