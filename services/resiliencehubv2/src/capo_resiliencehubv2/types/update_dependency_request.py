"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateDependencyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.uuid


class UpdateDependencyRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    dependency_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the dependency to update.</p>"""
    criticality: NotRequired[
        "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
    ]
    """<p>The updated criticality level of the dependency.</p>"""
    comment: NotRequired["str"]
    """<p>A comment about the dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDependencyRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["dependencyId"] = value["dependency_id"]
    if "criticality" in value:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.serialize_json(
                value["criticality"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> UpdateDependencyRequest:
    out: UpdateDependencyRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("dependencyId") is not None:
        out["dependency_id"] = data["dependencyId"]
    else:
        out["dependency_id"] = ""
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.dependency_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.dependency_criticality.deserialize_json(
                data["criticality"]
            )
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
