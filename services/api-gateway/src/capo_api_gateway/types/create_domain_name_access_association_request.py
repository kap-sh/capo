"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDomainNameAccessAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.access_association_source_type
    import capo_api_gateway.types.map_of_string_to_string
    import capo_api_gateway.types.string


class CreateDomainNameAccessAssociationRequest(TypedDict, closed=True):
    domain_name_arn: "capo_api_gateway.types.string.String"
    """<p> The ARN of the domain name. </p>"""
    access_association_source_type: "capo_api_gateway.types.access_association_source_type.AccessAssociationSourceType"
    """<p> The type of the domain name access association source. </p>"""
    access_association_source: "capo_api_gateway.types.string.String"
    """<p> The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID. </p>"""
    tags: NotRequired[
        "capo_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameAccessAssociationRequest) -> dict:
    out: dict = {}
    out["domainNameArn"] = value["domain_name_arn"]
    import capo_api_gateway.types.access_association_source_type

    out["accessAssociationSourceType"] = (
        capo_api_gateway.types.access_association_source_type.serialize_json(
            value["access_association_source_type"]
        )
    )
    out["accessAssociationSource"] = value["access_association_source"]
    if "tags" in value:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainNameAccessAssociationRequest:
    out: CreateDomainNameAccessAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainNameArn") is not None:
        out["domain_name_arn"] = data["domainNameArn"]
    else:
        out["domain_name_arn"] = ""
    if data.get("accessAssociationSourceType") is not None:
        import capo_api_gateway.types.access_association_source_type

        out["access_association_source_type"] = (
            capo_api_gateway.types.access_association_source_type.deserialize_json(
                data["accessAssociationSourceType"]
            )
        )
    else:
        import typing

        out["access_association_source_type"] = typing.cast(
            "capo_api_gateway.types.access_association_source_type.AccessAssociationSourceType",
            "",
        )
    if data.get("accessAssociationSource") is not None:
        out["access_association_source"] = data["accessAssociationSource"]
    else:
        out["access_association_source"] = ""
    if data.get("tags") is not None:
        import capo_api_gateway.types.map_of_string_to_string

        out["tags"] = capo_api_gateway.types.map_of_string_to_string.deserialize_json(
            data["tags"]
        )
    return out
