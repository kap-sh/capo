"""Generated from Smithy shape ``com.amazonaws.servicecatalog#BatchDisassociateServiceActionFromProvisioningArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.service_action_associations


class BatchDisassociateServiceActionFromProvisioningArtifactInput(
    TypedDict, closed=True
):
    service_action_associations: "capo_service_catalog.types.service_action_associations.ServiceActionAssociations"
    """<p>One or more associations, each consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchDisassociateServiceActionFromProvisioningArtifactInput,
) -> dict:
    out: dict = {}
    import capo_service_catalog.types.service_action_associations

    out["ServiceActionAssociations"] = (
        capo_service_catalog.types.service_action_associations.serialize_aws_json_1_1(
            value["service_action_associations"]
        )
    )
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchDisassociateServiceActionFromProvisioningArtifactInput:
    out: BatchDisassociateServiceActionFromProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionAssociations") is not None:
        import capo_service_catalog.types.service_action_associations

        out["service_action_associations"] = (
            capo_service_catalog.types.service_action_associations.deserialize_aws_json_1_1(
                data["ServiceActionAssociations"]
            )
        )
    else:
        out["service_action_associations"] = []
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    return out
