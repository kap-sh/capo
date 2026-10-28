"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceIntegrationUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError, SerializationError
from capo_lakeformation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_lakeformation.types.redshift_service_integrations


class ServiceIntegrationUnionRedshiftMember(TypedDict, closed=True):
    Redshift: "capo_lakeformation.types.redshift_service_integrations.RedshiftServiceIntegrations"


ServiceIntegrationUnion: TypeAlias = (
    ServiceIntegrationUnionRedshiftMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIntegrationUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceIntegrationUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Redshift" in value:
        import capo_lakeformation.types.redshift_service_integrations

        return {
            "Redshift": capo_lakeformation.types.redshift_service_integrations.serialize_json(
                value["Redshift"]
            )
        }
    else:
        raise SerializationError("ServiceIntegrationUnion: no variant present")


def deserialize_json(data: dict) -> ServiceIntegrationUnion:
    if data.get("Redshift") is not None:
        import capo_lakeformation.types.redshift_service_integrations

        return {
            "Redshift": capo_lakeformation.types.redshift_service_integrations.deserialize_json(
                data["Redshift"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ServiceIntegrationUnion: no recognized variant key")
