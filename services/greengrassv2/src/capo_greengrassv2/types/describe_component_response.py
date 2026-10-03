"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DescribeComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.cloud_component_status
    import capo_greengrassv2.types.component_name_string
    import capo_greengrassv2.types.component_platform_list
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.component_version_string
    import capo_greengrassv2.types.description_string
    import capo_greengrassv2.types.publisher_string
    import capo_greengrassv2.types.tag_map
    import capo_greengrassv2.types.timestamp


class DescribeComponentResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""
    component_name: NotRequired[
        "capo_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    creation_timestamp: NotRequired["capo_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the component was created, expressed in ISO 8601 format.</p>"""
    publisher: NotRequired["capo_greengrassv2.types.publisher_string.PublisherString"]
    """<p>The publisher of the component version.</p>"""
    description: NotRequired[
        "capo_greengrassv2.types.description_string.DescriptionString"
    ]
    """<p>The description of the component version.</p>"""
    status: NotRequired[
        "capo_greengrassv2.types.cloud_component_status.CloudComponentStatus"
    ]
    """<p>The status of the component version in IoT Greengrass V2. This status is different from the status of the component on a core device.</p>"""
    platforms: NotRequired[
        "capo_greengrassv2.types.component_platform_list.ComponentPlatformList"
    ]
    """<p>The platforms that the component version supports.</p>"""
    tags: NotRequired["capo_greengrassv2.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html">Tag your resources</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComponentResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "creation_timestamp" in value:
        import capo_greengrassv2.types.timestamp

        out["creationTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_greengrassv2.types.cloud_component_status

        out["status"] = capo_greengrassv2.types.cloud_component_status.serialize_json(
            value["status"]
        )
    if "platforms" in value:
        import capo_greengrassv2.types.component_platform_list

        out["platforms"] = (
            capo_greengrassv2.types.component_platform_list.serialize_json(
                value["platforms"]
            )
        )
    if "tags" in value:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeComponentResponse:
    out: DescribeComponentResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("creationTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["creation_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if data.get("publisher") is not None:
        out["publisher"] = data["publisher"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_greengrassv2.types.cloud_component_status

        out["status"] = capo_greengrassv2.types.cloud_component_status.deserialize_json(
            data["status"]
        )
    if data.get("platforms") is not None:
        import capo_greengrassv2.types.component_platform_list

        out["platforms"] = (
            capo_greengrassv2.types.component_platform_list.deserialize_json(
                data["platforms"]
            )
        )
    if data.get("tags") is not None:
        import capo_greengrassv2.types.tag_map

        out["tags"] = capo_greengrassv2.types.tag_map.deserialize_json(data["tags"])
    return out
