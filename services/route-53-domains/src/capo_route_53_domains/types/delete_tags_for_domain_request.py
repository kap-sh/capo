"""Generated from Smithy shape ``com.amazonaws.route53domains#DeleteTagsForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.tag_key_list


class DeleteTagsForDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The domain for which you want to delete one or more tags.</p>"""
    tags_to_delete: "capo_route_53_domains.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsForDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import capo_route_53_domains.types.tag_key_list

    out["TagsToDelete"] = (
        capo_route_53_domains.types.tag_key_list.serialize_aws_json_1_1(
            value["tags_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsForDomainRequest:
    out: DeleteTagsForDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("TagsToDelete") is not None:
        import capo_route_53_domains.types.tag_key_list

        out["tags_to_delete"] = (
            capo_route_53_domains.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagsToDelete"]
            )
        )
    else:
        out["tags_to_delete"] = []
    return out
