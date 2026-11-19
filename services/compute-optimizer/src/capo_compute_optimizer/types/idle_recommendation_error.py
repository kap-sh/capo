"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.code
    import capo_compute_optimizer.types.identifier
    import capo_compute_optimizer.types.idle_recommendation_resource_type
    import capo_compute_optimizer.types.message


class IdleRecommendationError(TypedDict, closed=True):
    identifier: NotRequired["capo_compute_optimizer.types.identifier.Identifier"]
    """<p>The ID of the error.</p>"""
    code: NotRequired["capo_compute_optimizer.types.code.Code"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_compute_optimizer.types.message.Message"]
    """<p>The error message.</p>"""
    resource_type: NotRequired[
        "capo_compute_optimizer.types.idle_recommendation_resource_type.IdleRecommendationResourceType"
    ]
    """<p>The type of resource associated with the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationError) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleRecommendationError:
    out: IdleRecommendationError = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleRecommendationError) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resourceType"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.serialize_cbor(
                value["resource_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IdleRecommendationError:
    out: IdleRecommendationError = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.idle_recommendation_resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.idle_recommendation_resource_type.deserialize_cbor(
                data["resourceType"]
            )
        )
    return out
