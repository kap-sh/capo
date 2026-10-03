"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateBuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.operating_system
    import capo_gamelift.types.s3_location
    import capo_gamelift.types.server_sdk_version
    import capo_gamelift.types.tag_list


class CreateBuildInput(TypedDict, closed=True):
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a build. Build names do not need to be unique. You can change this value later. </p>"""
    version: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique. You can change this value later. </p>"""
    storage_location: NotRequired["capo_gamelift.types.s3_location.S3Location"]
    """<p>Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.</p> <p>If a <code>StorageLocation</code> is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a <code>SizeOnDisk</code> of 0. </p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note> <note> <p>Windows Server 2016 will reach end of support on 1/12/2027. For game servers that are hosted on Windows Server 2016 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to Windows Server 2022 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new build resource. Tags are developer defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. Once the resource is created, you can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to add, remove, and view tags. The maximum tag limit may be lower than stated. See the Amazon Web Services General Reference for actual tagging limits.</p>"""
    server_sdk_version: NotRequired[
        "capo_gamelift.types.server_sdk_version.ServerSdkVersion"
    ]
    """<p>A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html">Integrate games with custom game servers</a>. By default Amazon GameLift Servers sets this value to <code>4.0.2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBuildInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "storage_location" in value:
        import capo_gamelift.types.s3_location

        out["StorageLocation"] = capo_gamelift.types.s3_location.serialize_aws_json_1_1(
            value["storage_location"]
        )
    if "operating_system" in value:
        import capo_gamelift.types.operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "server_sdk_version" in value:
        out["ServerSdkVersion"] = value["server_sdk_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBuildInput:
    out: CreateBuildInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("StorageLocation") is not None:
        import capo_gamelift.types.s3_location

        out["storage_location"] = (
            capo_gamelift.types.s3_location.deserialize_aws_json_1_1(
                data["StorageLocation"]
            )
        )
    if data.get("OperatingSystem") is not None:
        import capo_gamelift.types.operating_system

        out["operating_system"] = (
            capo_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ServerSdkVersion") is not None:
        out["server_sdk_version"] = data["ServerSdkVersion"]
    return out
