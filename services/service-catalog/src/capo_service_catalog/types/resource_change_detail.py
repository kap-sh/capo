"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceChangeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.causing_entity
    import capo_service_catalog.types.evaluation_type
    import capo_service_catalog.types.resource_target_definition


class ResourceChangeDetail(TypedDict, closed=True):
    target: NotRequired[
        "capo_service_catalog.types.resource_target_definition.ResourceTargetDefinition"
    ]
    """<p>Information about the resource attribute to be modified.</p>"""
    evaluation: NotRequired["capo_service_catalog.types.evaluation_type.EvaluationType"]
    """<p>For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.</p>"""
    causing_entity: NotRequired[
        "capo_service_catalog.types.causing_entity.CausingEntity"
    ]
    """<p>The ID of the entity that caused the change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceChangeDetail) -> dict:
    out: dict = {}
    if "target" in value:
        import capo_service_catalog.types.resource_target_definition

        out["Target"] = (
            capo_service_catalog.types.resource_target_definition.serialize_aws_json_1_1(
                value["target"]
            )
        )
    if "evaluation" in value:
        import capo_service_catalog.types.evaluation_type

        out["Evaluation"] = (
            capo_service_catalog.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation"]
            )
        )
    if "causing_entity" in value:
        out["CausingEntity"] = value["causing_entity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceChangeDetail:
    out: ResourceChangeDetail = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_service_catalog.types.resource_target_definition

        out["target"] = (
            capo_service_catalog.types.resource_target_definition.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if data.get("Evaluation") is not None:
        import capo_service_catalog.types.evaluation_type

        out["evaluation"] = (
            capo_service_catalog.types.evaluation_type.deserialize_aws_json_1_1(
                data["Evaluation"]
            )
        )
    if data.get("CausingEntity") is not None:
        out["causing_entity"] = data["CausingEntity"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceChangeDetail) -> dict:
    out: dict = {}
    if "target" in value:
        import capo_service_catalog.types.resource_target_definition

        out["Target"] = (
            capo_service_catalog.types.resource_target_definition.serialize_cbor(
                value["target"]
            )
        )
    if "evaluation" in value:
        import capo_service_catalog.types.evaluation_type

        out["Evaluation"] = capo_service_catalog.types.evaluation_type.serialize_cbor(
            value["evaluation"]
        )
    if "causing_entity" in value:
        out["CausingEntity"] = value["causing_entity"]
    return out


def deserialize_cbor(data: dict) -> ResourceChangeDetail:
    out: ResourceChangeDetail = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        import capo_service_catalog.types.resource_target_definition

        out["target"] = (
            capo_service_catalog.types.resource_target_definition.deserialize_cbor(
                data["Target"]
            )
        )
    if data.get("Evaluation") is not None:
        import capo_service_catalog.types.evaluation_type

        out["evaluation"] = capo_service_catalog.types.evaluation_type.deserialize_cbor(
            data["Evaluation"]
        )
    if data.get("CausingEntity") is not None:
        out["causing_entity"] = data["CausingEntity"]
    return out
