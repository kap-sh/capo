"""Generated from Smithy shape ``com.amazonaws.servicecatalog#BatchAssociateServiceActionWithProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.failed_service_action_associations


class BatchAssociateServiceActionWithProvisioningArtifactOutput(TypedDict, closed=True):
    failed_service_action_associations: NotRequired[
        "capo_service_catalog.types.failed_service_action_associations.FailedServiceActionAssociations"
    ]
    """<p>An object that contains a list of errors, along with information to help you identify the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateServiceActionWithProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    if "failed_service_action_associations" in value:
        import capo_service_catalog.types.failed_service_action_associations

        out["FailedServiceActionAssociations"] = (
            capo_service_catalog.types.failed_service_action_associations.serialize_aws_json_1_1(
                value["failed_service_action_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchAssociateServiceActionWithProvisioningArtifactOutput:
    out: BatchAssociateServiceActionWithProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("FailedServiceActionAssociations") is not None:
        import capo_service_catalog.types.failed_service_action_associations

        out["failed_service_action_associations"] = (
            capo_service_catalog.types.failed_service_action_associations.deserialize_aws_json_1_1(
                data["FailedServiceActionAssociations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    value: BatchAssociateServiceActionWithProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    if "failed_service_action_associations" in value:
        import capo_service_catalog.types.failed_service_action_associations

        out["FailedServiceActionAssociations"] = (
            capo_service_catalog.types.failed_service_action_associations.serialize_cbor(
                value["failed_service_action_associations"]
            )
        )
    return out


def deserialize_cbor(
    data: dict,
) -> BatchAssociateServiceActionWithProvisioningArtifactOutput:
    out: BatchAssociateServiceActionWithProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("FailedServiceActionAssociations") is not None:
        import capo_service_catalog.types.failed_service_action_associations

        out["failed_service_action_associations"] = (
            capo_service_catalog.types.failed_service_action_associations.deserialize_cbor(
                data["FailedServiceActionAssociations"]
            )
        )
    return out
