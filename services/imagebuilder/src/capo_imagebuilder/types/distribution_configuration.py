"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.distribution_list
    import capo_imagebuilder.types.distribution_timeout_minutes
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map


class DistributionConfiguration(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the distribution configuration.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the distribution configuration.</p>"""
    distributions: NotRequired[
        "capo_imagebuilder.types.distribution_list.DistributionList"
    ]
    """<p>The distribution objects that apply Region-specific settings for the deployment of the image to targeted Regions.</p>"""
    timeout_minutes: "capo_imagebuilder.types.distribution_timeout_minutes.DistributionTimeoutMinutes"
    """<p>A property that Image Builder doesn't use. You can't set this property when you create or update a distribution configuration, and it has no effect on distribution behavior.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this distribution configuration was created.</p>"""
    date_updated: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this distribution configuration was last updated.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the distribution configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributionConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "distributions" in value:
        import capo_imagebuilder.types.distribution_list

        out["distributions"] = capo_imagebuilder.types.distribution_list.serialize_json(
            value["distributions"]
        )
    out["timeoutMinutes"] = value["timeout_minutes"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["dateUpdated"] = value["date_updated"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DistributionConfiguration:
    out: DistributionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("distributions") is not None:
        import capo_imagebuilder.types.distribution_list

        out["distributions"] = (
            capo_imagebuilder.types.distribution_list.deserialize_json(
                data["distributions"]
            )
        )
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 0
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
    if data.get("dateUpdated") is not None:
        out["date_updated"] = data["dateUpdated"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    return out
