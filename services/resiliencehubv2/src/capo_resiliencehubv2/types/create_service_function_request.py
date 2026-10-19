"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateServiceFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.service_function_criticality


class CreateServiceFunctionRequest(TypedDict, closed=True):
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    """<p>The criticality level of the service function.</p>"""
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceFunctionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["serviceArn"] = value["service_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehubv2.types.service_function_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.service_function_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateServiceFunctionRequest:
    out: CreateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("criticality") is not None:
        import capo_resiliencehubv2.types.service_function_criticality

        out["criticality"] = (
            capo_resiliencehubv2.types.service_function_criticality.deserialize_json(
                data["criticality"]
            )
        )
    else:
        import typing

        out["criticality"] = typing.cast(
            "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality",
            "",
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
