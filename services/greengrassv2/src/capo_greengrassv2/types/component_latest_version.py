"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentLatestVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_platform_list
    import capo_greengrassv2.types.component_version_arn
    import capo_greengrassv2.types.component_version_string
    import capo_greengrassv2.types.non_empty_string
    import capo_greengrassv2.types.timestamp


class ComponentLatestVersion(TypedDict, closed=True):
    arn: NotRequired[
        "capo_greengrassv2.types.component_version_arn.ComponentVersionARN"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the component version.</p>"""
    component_version: NotRequired[
        "capo_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    creation_timestamp: NotRequired["capo_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the component was created, expressed in ISO 8601 format.</p>"""
    description: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The description of the component version.</p>"""
    publisher: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The publisher of the component version.</p>"""
    platforms: NotRequired[
        "capo_greengrassv2.types.component_platform_list.ComponentPlatformList"
    ]
    """<p>The platforms that the component version supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentLatestVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "creation_timestamp" in value:
        import capo_greengrassv2.types.timestamp

        out["creationTimestamp"] = capo_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    if "platforms" in value:
        import capo_greengrassv2.types.component_platform_list

        out["platforms"] = (
            capo_greengrassv2.types.component_platform_list.serialize_json(
                value["platforms"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentLatestVersion:
    out: ComponentLatestVersion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("componentVersion") is not None:
        out["component_version"] = data["componentVersion"]
    if data.get("creationTimestamp") is not None:
        import capo_greengrassv2.types.timestamp

        out["creation_timestamp"] = capo_greengrassv2.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("publisher") is not None:
        out["publisher"] = data["publisher"]
    if data.get("platforms") is not None:
        import capo_greengrassv2.types.component_platform_list

        out["platforms"] = (
            capo_greengrassv2.types.component_platform_list.deserialize_json(
                data["platforms"]
            )
        )
    return out
