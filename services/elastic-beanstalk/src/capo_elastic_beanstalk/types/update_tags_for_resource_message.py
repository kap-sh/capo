"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateTagsForResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_arn
    import capo_elastic_beanstalk.types.tag_key_list
    import capo_elastic_beanstalk.types.tag_list


class UpdateTagsForResourceMessage(TypedDict, closed=True):
    resource_arn: "capo_elastic_beanstalk.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resouce to be updated.</p> <p>Must be the ARN of an Elastic Beanstalk resource.</p>"""
    tags_to_add: NotRequired["capo_elastic_beanstalk.types.tag_list.TagList"]
    """<p>A list of tags to add or update. If a key of an existing tag is added, the tag's value is updated.</p> <p>Specify at least one of these parameters: <code>TagsToAdd</code>, <code>TagsToRemove</code>.</p>"""
    tags_to_remove: NotRequired["capo_elastic_beanstalk.types.tag_key_list.TagKeyList"]
    """<p>A list of tag keys to remove. If a tag key doesn't exist, it is silently ignored.</p> <p>Specify at least one of these parameters: <code>TagsToAdd</code>, <code>TagsToRemove</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTagsForResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "tags_to_add" in value:
        import capo_elastic_beanstalk.types.tag_list

        capo_elastic_beanstalk.types.tag_list.serialize_query(
            value["tags_to_add"], pairs, f"{key_prefix}TagsToAdd"
        )
    if "tags_to_remove" in value:
        import capo_elastic_beanstalk.types.tag_key_list

        capo_elastic_beanstalk.types.tag_key_list.serialize_query(
            value["tags_to_remove"], pairs, f"{key_prefix}TagsToRemove"
        )


def deserialize_query(el: Element) -> UpdateTagsForResourceMessage:
    out: UpdateTagsForResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        out["resource_arn"] = ""
    child_tags_to_add = el.find("TagsToAdd")
    if child_tags_to_add is not None:
        import capo_elastic_beanstalk.types.tag_list

        out["tags_to_add"] = capo_elastic_beanstalk.types.tag_list.deserialize_query(
            child_tags_to_add
        )
    child_tags_to_remove = el.find("TagsToRemove")
    if child_tags_to_remove is not None:
        import capo_elastic_beanstalk.types.tag_key_list

        out["tags_to_remove"] = (
            capo_elastic_beanstalk.types.tag_key_list.deserialize_query(
                child_tags_to_remove
            )
        )
    return out
