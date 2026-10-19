"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.service_function_criticality
    import capo_resiliencehubv2.types.service_function_source


class ServiceFunction(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId"
    """<p>The unique identifier of the service function.</p>"""
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    criticality: "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
    """<p>The criticality level of the service function.</p>"""
    resource_count: NotRequired["int"]
    """<p>The number of resources associated with the service function.</p>"""
    source: NotRequired[
        "capo_resiliencehubv2.types.service_function_source.ServiceFunctionSource"
    ]
    """<p>The source of the service function.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service function was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the service function was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunction) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["serviceFunctionId"] = value["service_function_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_resiliencehubv2.types.service_function_criticality

    out["criticality"] = (
        capo_resiliencehubv2.types.service_function_criticality.serialize_json(
            value["criticality"]
        )
    )
    if "resource_count" in value:
        out["resourceCount"] = value["resource_count"]
    if "source" in value:
        import capo_resiliencehubv2.types.service_function_source

        out["source"] = (
            capo_resiliencehubv2.types.service_function_source.serialize_json(
                value["source"]
            )
        )
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updatedAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ServiceFunction:
    out: ServiceFunction = {}  # type: ignore[typeddict-item]
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
    else:
        out["name"] = ""
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
    if data.get("resourceCount") is not None:
        out["resource_count"] = data["resourceCount"]
    if data.get("source") is not None:
        import capo_resiliencehubv2.types.service_function_source

        out["source"] = (
            capo_resiliencehubv2.types.service_function_source.deserialize_json(
                data["source"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["updated_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
