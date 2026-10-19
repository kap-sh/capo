"""Generated from Smithy shape ``com.amazonaws.configservice#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. The following resources are supported:</p> <ul> <li> <p> <code>ConfigurationRecorder</code> </p> </li> <li> <p> <code>ConfigRule</code> </p> </li> <li> <p> <code>OrganizationConfigRule</code> </p> </li> <li> <p> <code>ConformancePack</code> </p> </li> <li> <p> <code>OrganizationConformancePack</code> </p> </li> <li> <p> <code>ConfigurationAggregator</code> </p> </li> <li> <p> <code>AggregationAuthorization</code> </p> </li> <li> <p> <code>StoredQuery</code> </p> </li> <li> <p> <code>Connector</code> </p> </li> </ul>"""
    tag_keys: "capo_config_service.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_config_service.types.tag_key_list

    out["TagKeys"] = capo_config_service.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_config_service.types.tag_key_list

        out["tag_keys"] = (
            capo_config_service.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
