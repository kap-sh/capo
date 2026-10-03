"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.facet_attribute_list
    import capo_clouddirectory.types.facet_name
    import capo_clouddirectory.types.facet_style
    import capo_clouddirectory.types.object_type


class CreateFacetRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The schema ARN in which the new <a>Facet</a> will be created. For more information, see <a>arns</a>.</p>"""
    name: "capo_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the <a>Facet</a>, which is unique for a given schema.</p>"""
    attributes: NotRequired[
        "capo_clouddirectory.types.facet_attribute_list.FacetAttributeList"
    ]
    """<p>The attributes that are associated with the <a>Facet</a>.</p>"""
    object_type: NotRequired["capo_clouddirectory.types.object_type.ObjectType"]
    """<p>Specifies whether a given object created from this facet is of type node, leaf node, policy or index.</p> <ul> <li> <p>Node: Can have multiple children but one parent.</p> </li> </ul> <ul> <li> <p>Leaf node: Cannot have children but can have multiple parents.</p> </li> </ul> <ul> <li> <p>Policy: Allows you to store a policy document and policy type. For more information, see <a href="https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies">Policies</a>.</p> </li> </ul> <ul> <li> <p>Index: Can be created with the Index API.</p> </li> </ul>"""
    facet_style: NotRequired["capo_clouddirectory.types.facet_style.FacetStyle"]
    """<p>There are two different styles that you can define on any given facet, <code>Static</code> and <code>Dynamic</code>. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attributes" in value:
        import capo_clouddirectory.types.facet_attribute_list

        out["Attributes"] = (
            capo_clouddirectory.types.facet_attribute_list.serialize_json(
                value["attributes"]
            )
        )
    if "object_type" in value:
        import capo_clouddirectory.types.object_type

        out["ObjectType"] = capo_clouddirectory.types.object_type.serialize_json(
            value["object_type"]
        )
    if "facet_style" in value:
        import capo_clouddirectory.types.facet_style

        out["FacetStyle"] = capo_clouddirectory.types.facet_style.serialize_json(
            value["facet_style"]
        )
    return out


def deserialize_json(data: dict) -> CreateFacetRequest:
    out: CreateFacetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateFacetRequest.name required")
    if data.get("Attributes") is not None:
        import capo_clouddirectory.types.facet_attribute_list

        out["attributes"] = (
            capo_clouddirectory.types.facet_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("ObjectType") is not None:
        import capo_clouddirectory.types.object_type

        out["object_type"] = capo_clouddirectory.types.object_type.deserialize_json(
            data["ObjectType"]
        )
    if data.get("FacetStyle") is not None:
        import capo_clouddirectory.types.facet_style

        out["facet_style"] = capo_clouddirectory.types.facet_style.deserialize_json(
            data["FacetStyle"]
        )
    return out
