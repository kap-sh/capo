"""Generated from Smithy shape ``com.amazonaws.redshift#S3AccessGrantsScopeUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import DeserializationError, SerializationError
from capo_redshift.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_redshift.types.read_write_access


class S3AccessGrantsScopeUnionReadWriteAccessMember(TypedDict, closed=True):
    ReadWriteAccess: "capo_redshift.types.read_write_access.ReadWriteAccess"


S3AccessGrantsScopeUnion: TypeAlias = (
    S3AccessGrantsScopeUnionReadWriteAccessMember | UnknownUnionMember
)


# --- awsQuery ser/de ---
def serialize_query(
    value: S3AccessGrantsScopeUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "$unknown" in value:
        raise SerializationError(
            f"S3AccessGrantsScopeUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ReadWriteAccess" in value:
        import capo_redshift.types.read_write_access

        capo_redshift.types.read_write_access.serialize_query(
            value["ReadWriteAccess"], pairs, f"{prefix}.ReadWriteAccess"
        )
    else:
        raise SerializationError("S3AccessGrantsScopeUnion: no variant present")


def deserialize_query(el: Element) -> S3AccessGrantsScopeUnion:
    for child in el:
        if child.tag == "ReadWriteAccess":
            import capo_redshift.types.read_write_access

            return {
                "ReadWriteAccess": capo_redshift.types.read_write_access.deserialize_query(
                    child
                )
            }
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError(
        "S3AccessGrantsScopeUnion: no recognized variant element"
    )
