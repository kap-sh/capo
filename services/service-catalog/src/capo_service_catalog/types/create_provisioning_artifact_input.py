"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisioningArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.provisioning_artifact_properties


class CreateProvisioningArtifactInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    parameters: "capo_service_catalog.types.provisioning_artifact_properties.ProvisioningArtifactProperties"
    """<p>The configuration for the provisioning artifact.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisioningArtifactInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    import capo_service_catalog.types.provisioning_artifact_properties

    out["Parameters"] = (
        capo_service_catalog.types.provisioning_artifact_properties.serialize_aws_json_1_1(
            value["parameters"]
        )
    )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisioningArtifactInput:
    out: CreateProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("Parameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_properties

        out["parameters"] = (
            capo_service_catalog.types.provisioning_artifact_properties.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProvisioningArtifactInput.parameters required"
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
