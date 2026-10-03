"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AddDraftAppVersionResourceMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.resource_mapping_list


class AddDraftAppVersionResourceMappingsResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    resource_mappings: (
        "capo_resiliencehub.types.resource_mapping_list.ResourceMappingList"
    )
    """<p>List of sources that are used to map a logical resource from the template to a physical resource. You can use sources such as CloudFormation, Terraform state files, AppRegistry applications, or Amazon EKS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDraftAppVersionResourceMappingsResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    import capo_resiliencehub.types.resource_mapping_list

    out["resourceMappings"] = (
        capo_resiliencehub.types.resource_mapping_list.serialize_json(
            value["resource_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddDraftAppVersionResourceMappingsResponse:
    out: AddDraftAppVersionResourceMappingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "AddDraftAppVersionResourceMappingsResponse.app_arn required"
        )
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "AddDraftAppVersionResourceMappingsResponse.app_version required"
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
            "AddDraftAppVersionResourceMappingsResponse.resource_mappings required"
        )
    return out
