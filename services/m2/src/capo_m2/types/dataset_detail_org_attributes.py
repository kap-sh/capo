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


class _DatasetDetailOrgAttributes_vsam(TypedDict, closed=True):
    vsam: "capo_m2.types.vsam_detail_attributes.VsamDetailAttributes"


class _DatasetDetailOrgAttributes_gdg(TypedDict, closed=True):
    gdg: "capo_m2.types.gdg_detail_attributes.GdgDetailAttributes"


class _DatasetDetailOrgAttributes_po(TypedDict, closed=True):
    po: "capo_m2.types.po_detail_attributes.PoDetailAttributes"


class _DatasetDetailOrgAttributes_ps(TypedDict, closed=True):
    ps: "capo_m2.types.ps_detail_attributes.PsDetailAttributes"


DatasetDetailOrgAttributes: TypeAlias = (
    _DatasetDetailOrgAttributes_vsam
    | _DatasetDetailOrgAttributes_gdg
    | _DatasetDetailOrgAttributes_po
    | _DatasetDetailOrgAttributes_ps
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatasetDetailOrgAttributes) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DatasetDetailOrgAttributes: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DatasetDetailOrgAttributes: no recognized variant key"
        )
