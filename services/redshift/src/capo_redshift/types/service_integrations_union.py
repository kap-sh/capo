"""Generated from Smithy shape ``com.amazonaws.redshift#ServiceIntegrationsUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import DeserializationError, SerializationError
from capo_redshift.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_redshift.types.lake_formation_service_integrations
    import capo_redshift.types.redshift_service_integrations
    import capo_redshift.types.s3_access_grants_service_integrations


class _ServiceIntegrationsUnion_LakeFormation(TypedDict, closed=True):
    LakeFormation: "capo_redshift.types.lake_formation_service_integrations.LakeFormationServiceIntegrations"


class _ServiceIntegrationsUnion_S3AccessGrants(TypedDict, closed=True):
    S3AccessGrants: "capo_redshift.types.s3_access_grants_service_integrations.S3AccessGrantsServiceIntegrations"


class _ServiceIntegrationsUnion_Redshift(TypedDict, closed=True):
    Redshift: (
        "capo_redshift.types.redshift_service_integrations.RedshiftServiceIntegrations"
    )


ServiceIntegrationsUnion: TypeAlias = (
    _ServiceIntegrationsUnion_LakeFormation
    | _ServiceIntegrationsUnion_S3AccessGrants
    | _ServiceIntegrationsUnion_Redshift
    | UnknownUnionMember
)


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceIntegrationsUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceIntegrationsUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "LakeFormation" in value:
        import capo_redshift.types.lake_formation_service_integrations

        capo_redshift.types.lake_formation_service_integrations.serialize_query(
            value["LakeFormation"], pairs, f"{prefix}.LakeFormation"
        )
    elif "S3AccessGrants" in value:
        import capo_redshift.types.s3_access_grants_service_integrations

        capo_redshift.types.s3_access_grants_service_integrations.serialize_query(
            value["S3AccessGrants"], pairs, f"{prefix}.S3AccessGrants"
        )
    elif "Redshift" in value:
        import capo_redshift.types.redshift_service_integrations

        capo_redshift.types.redshift_service_integrations.serialize_query(
            value["Redshift"], pairs, f"{prefix}.Redshift"
        )
    else:
        raise SerializationError("ServiceIntegrationsUnion: no variant present")


def deserialize_query(el: Element) -> ServiceIntegrationsUnion:
    for child in el:
        if child.tag == "LakeFormation":
            import capo_redshift.types.lake_formation_service_integrations

            return {
                "LakeFormation": capo_redshift.types.lake_formation_service_integrations.deserialize_query(
                    child
                )
            }
        elif child.tag == "S3AccessGrants":
            import capo_redshift.types.s3_access_grants_service_integrations

            return {
                "S3AccessGrants": capo_redshift.types.s3_access_grants_service_integrations.deserialize_query(
                    child
                )
            }
        elif child.tag == "Redshift":
            import capo_redshift.types.redshift_service_integrations

            return {
                "Redshift": capo_redshift.types.redshift_service_integrations.deserialize_query(
                    child
                )
            }
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError(
        "ServiceIntegrationsUnion: no recognized variant element"
    )
