"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateServiceFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.service_function_criticality


class UpdateServiceFunctionRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId"
    """<p>The identifier of the service function to update.</p>"""
    name: NotRequired["capo_resiliencehubv2.types.entity_label.EntityLabel"]
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: NotRequired[
        "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    ]
    """<p>The updated criticality level of the service function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceFunctionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "criticality" in value:
        import capo_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.service_function_criticality.serialize_json(
                value["criticality"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceFunctionRequest:
    out: UpdateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("serviceFunctionId") is not None:
        out["service_function_id"] = data["serviceFunctionId"]
    else:
        out["service_function_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.service_function_criticality.deserialize_json(
                data["criticality"]
            )
        )
    return out
