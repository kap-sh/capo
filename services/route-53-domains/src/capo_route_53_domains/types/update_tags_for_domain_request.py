"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateTagsForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.tag_list


class UpdateTagsForDomainRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The domain for which you want to add or update tags.</p>"""
    tags_to_update: NotRequired["capo_route_53_domains.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to add or update. If you specify a key that already exists, the corresponding value will be replaced.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTagsForDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "tags_to_update" in value:
        import capo_route_53_domains.types.tag_list

        out["TagsToUpdate"] = (
            capo_route_53_domains.types.tag_list.serialize_aws_json_1_1(
                value["tags_to_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTagsForDomainRequest:
    out: UpdateTagsForDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("TagsToUpdate") is not None:
        import capo_route_53_domains.types.tag_list

        out["tags_to_update"] = (
            capo_route_53_domains.types.tag_list.deserialize_aws_json_1_1(
                data["TagsToUpdate"]
            )
        )
    return out
