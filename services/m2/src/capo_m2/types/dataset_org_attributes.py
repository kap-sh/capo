"""Generated from Smithy shape ``com.amazonaws.m2#DatasetOrgAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.gdg_attributes
    import capo_m2.types.po_attributes
    import capo_m2.types.ps_attributes
    import capo_m2.types.vsam_attributes


class DatasetOrgAttributesVsamMember(TypedDict, closed=True):
    vsam: "capo_m2.types.vsam_attributes.VsamAttributes"


class DatasetOrgAttributesGdgMember(TypedDict, closed=True):
    gdg: "capo_m2.types.gdg_attributes.GdgAttributes"


class DatasetOrgAttributesPoMember(TypedDict, closed=True):
    po: "capo_m2.types.po_attributes.PoAttributes"


class DatasetOrgAttributesPsMember(TypedDict, closed=True):
    ps: "capo_m2.types.ps_attributes.PsAttributes"


DatasetOrgAttributes: TypeAlias = (
    DatasetOrgAttributesVsamMember
    | DatasetOrgAttributesGdgMember
    | DatasetOrgAttributesPoMember
    | DatasetOrgAttributesPsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatasetOrgAttributes) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DatasetOrgAttributes: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "vsam" in value:
        import capo_m2.types.vsam_attributes

        return {"vsam": capo_m2.types.vsam_attributes.serialize_json(value["vsam"])}
    elif "gdg" in value:
        import capo_m2.types.gdg_attributes

        return {"gdg": capo_m2.types.gdg_attributes.serialize_json(value["gdg"])}
    elif "po" in value:
        import capo_m2.types.po_attributes

        return {"po": capo_m2.types.po_attributes.serialize_json(value["po"])}
    elif "ps" in value:
        import capo_m2.types.ps_attributes

        return {"ps": capo_m2.types.ps_attributes.serialize_json(value["ps"])}
    else:
        raise SerializationError("DatasetOrgAttributes: no variant present")


def deserialize_json(data: dict) -> DatasetOrgAttributes:
    if data.get("vsam") is not None:
        import capo_m2.types.vsam_attributes

        return {"vsam": capo_m2.types.vsam_attributes.deserialize_json(data["vsam"])}
    elif data.get("gdg") is not None:
        import capo_m2.types.gdg_attributes

        return {"gdg": capo_m2.types.gdg_attributes.deserialize_json(data["gdg"])}
    elif data.get("po") is not None:
        import capo_m2.types.po_attributes

        return {"po": capo_m2.types.po_attributes.deserialize_json(data["po"])}
    elif data.get("ps") is not None:
        import capo_m2.types.ps_attributes

        return {"ps": capo_m2.types.ps_attributes.deserialize_json(data["ps"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DatasetOrgAttributes: no recognized variant key")
