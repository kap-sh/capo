"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.input_source
    import capo_resiliencehubv2.types.resource


class ServiceResource(TypedDict, closed=True):
    resource_identifier: "str"
    """<p>The identifier of the resource.</p>"""
    input_source: NotRequired["capo_resiliencehubv2.types.input_source.InputSource"]
    """<p>The input source that discovered the resource.</p>"""
    resource: "capo_resiliencehubv2.types.resource.Resource"
    """<p>The resource details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResource) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    if "input_source" in value:
        import capo_resiliencehubv2.types.input_source

        out["inputSource"] = capo_resiliencehubv2.types.input_source.serialize_json(
            value["input_source"]
        )
    import capo_resiliencehubv2.types.resource

    out["resource"] = capo_resiliencehubv2.types.resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> ServiceResource:
    out: ServiceResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("inputSource") is not None:
        import capo_resiliencehubv2.types.input_source

        out["input_source"] = capo_resiliencehubv2.types.input_source.deserialize_json(
            data["inputSource"]
        )
    if data.get("resource") is not None:
        import capo_resiliencehubv2.types.resource

        out["resource"] = capo_resiliencehubv2.types.resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("ServiceResource.resource required")
    return out
