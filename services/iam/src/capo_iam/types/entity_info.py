"""Generated from Smithy shape ``com.amazonaws.iam#EntityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.id_type
    import capo_iam.types.path_type
    import capo_iam.types.policy_owner_entity_type
    import capo_iam.types.user_name_type


class EntityInfo(TypedDict, closed=True):
    arn: "capo_iam.types.arn_type.arnType"
    name: "capo_iam.types.user_name_type.userNameType"
    """<p>The name of the entity (user or role).</p>"""
    type: "capo_iam.types.policy_owner_entity_type.policyOwnerEntityType"
    """<p>The type of entity (user or role).</p>"""
    id: "capo_iam.types.id_type.idType"
    """<p>The identifier of the entity (user or role).</p>"""
    path: NotRequired["capo_iam.types.path_type.pathType"]
    """<p>The path to the entity (user or role). For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    import capo_iam.types.policy_owner_entity_type

    capo_iam.types.policy_owner_entity_type.serialize_query(
        value["type"], pairs, f"{key_prefix}Type"
    )
    pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))


def deserialize_query(el: Element) -> EntityInfo:
    out: EntityInfo = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("EntityInfo.arn required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("EntityInfo.name required")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_iam.types.policy_owner_entity_type

        out["type"] = capo_iam.types.policy_owner_entity_type.deserialize_query(
            child_type
        )
    else:
        raise DeserializationError("EntityInfo.type required")
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("EntityInfo.id required")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    return out
