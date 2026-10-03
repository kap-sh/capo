"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateAutoScalingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.as_config_max_concurrency
    import capo_apprunner.types.as_config_max_size
    import capo_apprunner.types.as_config_min_size
    import capo_apprunner.types.auto_scaling_configuration_name
    import capo_apprunner.types.tag_list


class CreateAutoScalingConfigurationRequest(TypedDict, closed=True):
    auto_scaling_configuration_name: "capo_apprunner.types.auto_scaling_configuration_name.AutoScalingConfigurationName"
    """<p>A name for the auto scaling configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number <code>1</code> of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</p> <note> <p>Prior to the release of <a href="https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2023-09-22-auto-scale-config.html">Auto scale configuration enhancements</a>, the name <code>DefaultConfiguration</code> was reserved. </p> <p>This restriction is no longer in place. You can now manage <code>DefaultConfiguration</code> the same way you manage your custom auto scaling configurations. This means you can do the following with the <code>DefaultConfiguration</code> that App Runner provides:</p> <ul> <li> <p>Create new revisions of the <code>DefaultConfiguration</code>.</p> </li> <li> <p>Delete the revisions of the <code>DefaultConfiguration</code>.</p> </li> <li> <p>Delete the auto scaling configuration for which the App Runner <code>DefaultConfiguration</code> was created.</p> </li> <li> <p>If you delete the auto scaling configuration you can create another custom auto scaling configuration with the same <code>DefaultConfiguration</code> name. The original <code>DefaultConfiguration</code> resource provided by App Runner remains in your account unless you make changes to it.</p> </li> </ul> </note>"""
    max_concurrency: NotRequired[
        "capo_apprunner.types.as_config_max_concurrency.ASConfigMaxConcurrency"
    ]
    """<p>The maximum number of concurrent requests that you want an instance to process. If the number of concurrent requests exceeds this limit, App Runner scales up your service.</p> <p>Default: <code>100</code> </p>"""
    min_size: NotRequired["capo_apprunner.types.as_config_min_size.ASConfigMinSize"]
    """<p>The minimum number of instances that App Runner provisions for your service. The service always has at least <code>MinSize</code> provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.</p> <p>App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.</p> <p>Default: <code>1</code> </p>"""
    max_size: NotRequired["capo_apprunner.types.as_config_max_size.ASConfigMaxSize"]
    """<p>The maximum number of instances that your service scales up to. At most <code>MaxSize</code> instances actively serve traffic for your service.</p> <p>Default: <code>25</code> </p>"""
    tags: NotRequired["capo_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutoScalingConfigurationRequest) -> dict:
    out: dict = {}
    out["AutoScalingConfigurationName"] = value["auto_scaling_configuration_name"]
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "min_size" in value:
        out["MinSize"] = value["min_size"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "tags" in value:
        import capo_apprunner.types.tag_list

        out["Tags"] = capo_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutoScalingConfigurationRequest:
    out: CreateAutoScalingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoScalingConfigurationName") is not None:
        out["auto_scaling_configuration_name"] = data["AutoScalingConfigurationName"]
    else:
        raise DeserializationError(
            "CreateAutoScalingConfigurationRequest.auto_scaling_configuration_name required"
        )
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MinSize") is not None:
        out["min_size"] = data["MinSize"]
    if data.get("MaxSize") is not None:
        out["max_size"] = data["MaxSize"]
    if data.get("Tags") is not None:
        import capo_apprunner.types.tag_list

        out["tags"] = capo_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
