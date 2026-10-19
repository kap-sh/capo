"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceFunctionResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.resource_list


class DeleteServiceFunctionResourcesRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to remove resources from.</p>"""
    resources: "capo_resiliencehubv2.types.resource_list.ResourceList"
    """<p>The list of resources to remove from the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceFunctionResourcesRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    import capo_resiliencehubv2.types.resource_list

    out["resources"] = capo_resiliencehubv2.types.resource_list.serialize_json(
        value["resources"]
    )
    return out


def deserialize_json(data: dict) -> DeleteServiceFunctionResourcesRequest:
    out: DeleteServiceFunctionResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("serviceFunctionId") is not None:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        out["service_function_id"] = ""
    if data.get("resources") is not None:
        import capo_resiliencehubv2.types.resource_list

        out["resources"] = capo_resiliencehubv2.types.resource_list.deserialize_json(
            data["resources"]
        )
    else:
        out["resources"] = []
    return out
