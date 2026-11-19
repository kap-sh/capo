"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EngineWorkflowResourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.unique_tag_resource_identifier


class EngineWorkflowResourceIdentifier(TypedDict, closed=True):
    unique_tag: NotRequired[
        "capo_service_catalog.types.unique_tag_resource_identifier.UniqueTagResourceIdentifier"
    ]
    """<p> The unique key-value pair for a tag that identifies provisioned product resources. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineWorkflowResourceIdentifier) -> dict:
    out: dict = {}
    if "unique_tag" in value:
        import capo_service_catalog.types.unique_tag_resource_identifier

        out["UniqueTag"] = (
            capo_service_catalog.types.unique_tag_resource_identifier.serialize_aws_json_1_1(
                value["unique_tag"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineWorkflowResourceIdentifier:
    out: EngineWorkflowResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("UniqueTag") is not None:
        import capo_service_catalog.types.unique_tag_resource_identifier

        out["unique_tag"] = (
            capo_service_catalog.types.unique_tag_resource_identifier.deserialize_aws_json_1_1(
                data["UniqueTag"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EngineWorkflowResourceIdentifier) -> dict:
    out: dict = {}
    if "unique_tag" in value:
        import capo_service_catalog.types.unique_tag_resource_identifier

        out["UniqueTag"] = (
            capo_service_catalog.types.unique_tag_resource_identifier.serialize_cbor(
                value["unique_tag"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EngineWorkflowResourceIdentifier:
    out: EngineWorkflowResourceIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("UniqueTag") is not None:
        import capo_service_catalog.types.unique_tag_resource_identifier

        out["unique_tag"] = (
            capo_service_catalog.types.unique_tag_resource_identifier.deserialize_cbor(
                data["UniqueTag"]
            )
        )
    return out
