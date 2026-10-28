"""Generated from Smithy shape ``com.amazonaws.connect#NextContactMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.quick_connect_contact_data


class NextContactMetadataQuickConnectContactDataMember(TypedDict, closed=True):
    QuickConnectContactData: (
        "capo_connect.types.quick_connect_contact_data.QuickConnectContactData"
    )


NextContactMetadata: TypeAlias = (
    NextContactMetadataQuickConnectContactDataMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NextContactMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NextContactMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "QuickConnectContactData" in value:
        import capo_connect.types.quick_connect_contact_data

        return {
            "QuickConnectContactData": capo_connect.types.quick_connect_contact_data.serialize_json(
                value["QuickConnectContactData"]
            )
        }
    else:
        raise SerializationError("NextContactMetadata: no variant present")


def deserialize_json(data: dict) -> NextContactMetadata:
    if data.get("QuickConnectContactData") is not None:
        import capo_connect.types.quick_connect_contact_data

        return {
            "QuickConnectContactData": capo_connect.types.quick_connect_contact_data.deserialize_json(
                data["QuickConnectContactData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NextContactMetadata: no recognized variant key")
