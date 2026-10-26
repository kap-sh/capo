"""Generated from Smithy shape ``com.amazonaws.controlcatalog#Mapping``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_controlcatalog.errors import DeserializationError, SerializationError
from capo_controlcatalog.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_mapping_details
    import capo_controlcatalog.types.framework_mapping_details
    import capo_controlcatalog.types.related_control_mapping_details


class _Mapping_Framework(TypedDict, closed=True):
    Framework: (
        "capo_controlcatalog.types.framework_mapping_details.FrameworkMappingDetails"
    )


class _Mapping_CommonControl(TypedDict, closed=True):
    CommonControl: "capo_controlcatalog.types.common_control_mapping_details.CommonControlMappingDetails"


class _Mapping_RelatedControl(TypedDict, closed=True):
    RelatedControl: "capo_controlcatalog.types.related_control_mapping_details.RelatedControlMappingDetails"


Mapping: TypeAlias = (
    _Mapping_Framework
    | _Mapping_CommonControl
    | _Mapping_RelatedControl
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Mapping) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Mapping: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Framework" in value:
        import capo_controlcatalog.types.framework_mapping_details

        return {
            "Framework": capo_controlcatalog.types.framework_mapping_details.serialize_json(
                value["Framework"]
            )
        }
    elif "CommonControl" in value:
        import capo_controlcatalog.types.common_control_mapping_details

        return {
            "CommonControl": capo_controlcatalog.types.common_control_mapping_details.serialize_json(
                value["CommonControl"]
            )
        }
    elif "RelatedControl" in value:
        import capo_controlcatalog.types.related_control_mapping_details

        return {
            "RelatedControl": capo_controlcatalog.types.related_control_mapping_details.serialize_json(
                value["RelatedControl"]
            )
        }
    else:
        raise SerializationError("Mapping: no variant present")


def deserialize_json(data: dict) -> Mapping:
    if data.get("Framework") is not None:
        import capo_controlcatalog.types.framework_mapping_details

        return {
            "Framework": capo_controlcatalog.types.framework_mapping_details.deserialize_json(
                data["Framework"]
            )
        }
    elif data.get("CommonControl") is not None:
        import capo_controlcatalog.types.common_control_mapping_details

        return {
            "CommonControl": capo_controlcatalog.types.common_control_mapping_details.deserialize_json(
                data["CommonControl"]
            )
        }
    elif data.get("RelatedControl") is not None:
        import capo_controlcatalog.types.related_control_mapping_details

        return {
            "RelatedControl": capo_controlcatalog.types.related_control_mapping_details.deserialize_json(
                data["RelatedControl"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Mapping: no recognized variant key")
