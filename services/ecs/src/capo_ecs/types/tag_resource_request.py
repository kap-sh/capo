"""Generated from Smithy shape ``com.amazonaws.ecs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p> <p>In order to tag a service that has the following ARN format, you need to migrate the service to the long ARN. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-arn-migration.html">Migrate an Amazon ECS short service ARN to a long ARN</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/service-name</code> </p> <p>After the migration is complete, the service has the long ARN format, as shown below. Use this ARN to tag the service.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p> <p>If you try to tag a service with a short ARN, you receive an <code>InvalidParameterException</code> error.</p>"""
    tags: "capo_ecs.types.tags.Tags"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_ecs.types.tags

    out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
