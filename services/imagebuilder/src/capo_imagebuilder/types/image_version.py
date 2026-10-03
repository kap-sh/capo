"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.build_type
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_source
    import capo_imagebuilder.types.image_type
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.version_number


class ImageVersion(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of a specific version of an Image Builder image.</p> <note> <p>Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:</p> <ol> <li> <p>Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.</p> </li> <li> <p>Version ARNs have only the first three nodes: <major>.<minor>.<patch></p> </li> <li> <p>Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.</p> </li> </ol> </note>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of this specific version of an Image Builder image.</p>"""
    type: NotRequired["capo_imagebuilder.types.image_type.ImageType"]
    """<p>Specifies whether this image produces an AMI or a container image.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The semantic version of the image. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> <p> <b>Filtering:</b> You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The operating system platform of the image version, for example "Windows" or "Linux".</p>"""
    os_version: NotRequired["capo_imagebuilder.types.os_version.OsVersion"]
    """<p>The operating system version of the image. For example, Amazon Linux 2023 or Microsoft Windows Server 2022.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the image version.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this specific version of the Image Builder image was created.</p>"""
    build_type: NotRequired["capo_imagebuilder.types.build_type.BuildType"]
    """<p>Indicates the type of build that created this image. The build can be initiated in the following ways:</p> <ul> <li> <p> <b>USER_INITIATED</b> – A manual pipeline build request.</p> </li> <li> <p> <b>SCHEDULED</b> – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.</p> </li> <li> <p> <b>IMPORT</b> – A VM import created the image to use as the base image for the recipe.</p> </li> <li> <p> <b>IMPORT_ISO</b> – An ISO disk import created the image.</p> </li> </ul>"""
    image_source: NotRequired["capo_imagebuilder.types.image_source.ImageSource"]
    """<p>The origin of the base image that Image Builder used to build this image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.serialize_json(value["type"])
    if "version" in value:
        out["version"] = value["version"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "build_type" in value:
        import capo_imagebuilder.types.build_type

        out["buildType"] = capo_imagebuilder.types.build_type.serialize_json(
            value["build_type"]
        )
    if "image_source" in value:
        import capo_imagebuilder.types.image_source

        out["imageSource"] = capo_imagebuilder.types.image_source.serialize_json(
            value["image_source"]
        )
    return out


def deserialize_json(data: dict) -> ImageVersion:
    out: ImageVersion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.deserialize_json(data["type"])
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if data.get("osVersion") is not None:
        out["os_version"] = data["osVersion"]
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
    if data.get("buildType") is not None:
        import capo_imagebuilder.types.build_type

        out["build_type"] = capo_imagebuilder.types.build_type.deserialize_json(
            data["buildType"]
        )
    if data.get("imageSource") is not None:
        import capo_imagebuilder.types.image_source

        out["image_source"] = capo_imagebuilder.types.image_source.deserialize_json(
            data["imageSource"]
        )
    return out
