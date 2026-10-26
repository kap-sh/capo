"""Generated from Smithy shape ``com.amazonaws.securityhub#Criteria``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_finding_filters
    import capo_securityhub.types.resources_filters


class _Criteria_OcsfFindingCriteria(TypedDict, closed=True):
    OcsfFindingCriteria: (
        "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    )


class _Criteria_ResourceCriteria(TypedDict, closed=True):
    ResourceCriteria: "capo_securityhub.types.resources_filters.ResourcesFilters"


Criteria: TypeAlias = (
    _Criteria_OcsfFindingCriteria | _Criteria_ResourceCriteria | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Criteria) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Criteria: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "OcsfFindingCriteria" in value:
        import capo_securityhub.types.ocsf_finding_filters

        return {
            "OcsfFindingCriteria": capo_securityhub.types.ocsf_finding_filters.serialize_json(
                value["OcsfFindingCriteria"]
            )
        }
    elif "ResourceCriteria" in value:
        import capo_securityhub.types.resources_filters

        return {
            "ResourceCriteria": capo_securityhub.types.resources_filters.serialize_json(
                value["ResourceCriteria"]
            )
        }
    else:
        raise SerializationError("Criteria: no variant present")


def deserialize_json(data: dict) -> Criteria:
    if data.get("OcsfFindingCriteria") is not None:
        import capo_securityhub.types.ocsf_finding_filters

        return {
            "OcsfFindingCriteria": capo_securityhub.types.ocsf_finding_filters.deserialize_json(
                data["OcsfFindingCriteria"]
            )
        }
    elif data.get("ResourceCriteria") is not None:
        import capo_securityhub.types.resources_filters

        return {
            "ResourceCriteria": capo_securityhub.types.resources_filters.deserialize_json(
                data["ResourceCriteria"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Criteria: no recognized variant key")
