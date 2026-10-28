"""Generated from Smithy shape ``com.amazonaws.m2#DatasetDetailOrgAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.gdg_detail_attributes
    import capo_m2.types.po_detail_attributes
    import capo_m2.types.ps_detail_attributes
    import capo_m2.types.vsam_detail_attributes


class DatasetDetailOrgAttributesVsamMember(TypedDict, closed=True):
    vsam: "capo_m2.types.vsam_detail_attributes.VsamDetailAttributes"


class DatasetDetailOrgAttributesGdgMember(TypedDict, closed=True):
    gdg: "capo_m2.types.gdg_detail_attributes.GdgDetailAttributes"


class DatasetDetailOrgAttributesPoMember(TypedDict, closed=True):
    po: "capo_m2.types.po_detail_attributes.PoDetailAttributes"


class DatasetDetailOrgAttributesPsMember(TypedDict, closed=True):
    ps: "capo_m2.types.ps_detail_attributes.PsDetailAttributes"


DatasetDetailOrgAttributes: TypeAlias = (
    DatasetDetailOrgAttributesVsamMember
    | DatasetDetailOrgAttributesGdgMember
    | DatasetDetailOrgAttributesPoMember
    | DatasetDetailOrgAttributesPsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatasetDetailOrgAttributes) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DatasetDetailOrgAttributes: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "vsam" in value:
        import capo_m2.types.vsam_detail_attributes

        return {
            "vsam": capo_m2.types.vsam_detail_attributes.serialize_json(value["vsam"])
        }
    elif "gdg" in value:
        import capo_m2.types.gdg_detail_attributes

        return {"gdg": capo_m2.types.gdg_detail_attributes.serialize_json(value["gdg"])}
    elif "po" in value:
        import capo_m2.types.po_detail_attributes

        return {"po": capo_m2.types.po_detail_attributes.serialize_json(value["po"])}
    elif "ps" in value:
        import capo_m2.types.ps_detail_attributes

        return {"ps": capo_m2.types.ps_detail_attributes.serialize_json(value["ps"])}
    else:
        raise SerializationError("DatasetDetailOrgAttributes: no variant present")


def deserialize_json(data: dict) -> DatasetDetailOrgAttributes:
    if data.get("vsam") is not None:
        import capo_m2.types.vsam_detail_attributes

        return {
            "vsam": capo_m2.types.vsam_detail_attributes.deserialize_json(data["vsam"])
        }
    elif data.get("gdg") is not None:
        import capo_m2.types.gdg_detail_attributes

        return {
            "gdg": capo_m2.types.gdg_detail_attributes.deserialize_json(data["gdg"])
        }
    elif data.get("po") is not None:
        import capo_m2.types.po_detail_attributes

        return {"po": capo_m2.types.po_detail_attributes.deserialize_json(data["po"])}
    elif data.get("ps") is not None:
        import capo_m2.types.ps_detail_attributes

        return {"ps": capo_m2.types.ps_detail_attributes.deserialize_json(data["ps"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DatasetDetailOrgAttributes: no recognized variant key"
        )
