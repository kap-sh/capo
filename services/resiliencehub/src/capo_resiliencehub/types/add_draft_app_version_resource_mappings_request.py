"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AddDraftAppVersionResourceMappingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.resource_mapping_list


class AddDraftAppVersionResourceMappingsRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    resource_mappings: (
        "capo_resiliencehub.types.resource_mapping_list.ResourceMappingList"
    )
    """<p>Mappings used to map logical resources from the template to physical resources. You can use the mapping type <code>CFN_STACK</code> if the application template uses a logical stack name. Or you can map individual resources by using the mapping type <code>RESOURCE</code>. We recommend using the mapping type <code>CFN_STACK</code> if the application is backed by a CloudFormation stack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDraftAppVersionResourceMappingsRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    import capo_resiliencehub.types.resource_mapping_list

    out["resourceMappings"] = (
        capo_resiliencehub.types.resource_mapping_list.serialize_json(
            value["resource_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddDraftAppVersionResourceMappingsRequest:
    out: AddDraftAppVersionResourceMappingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "AddDraftAppVersionResourceMappingsRequest.app_arn required"
        )
    if data.get("resourceMappings") is not None:
        import capo_resiliencehub.types.resource_mapping_list

        out["resource_mappings"] = (
            capo_resiliencehub.types.resource_mapping_list.deserialize_json(
                data["resourceMappings"]
            )
        )
    else:
        raise DeserializationError(
            "AddDraftAppVersionResourceMappingsRequest.resource_mappings required"
        )
    return out
