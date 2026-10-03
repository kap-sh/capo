"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.component_format
    import capo_imagebuilder.types.component_type
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.uri
    import capo_imagebuilder.types.version_number


class ImportComponentRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the component. Image Builder generates the component ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a component with the same name and semantic version already exists in your account in the same Amazon Web Services Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the component already exists.</p>"""
    semantic_version: "capo_imagebuilder.types.version_number.VersionNumber"
    """<p>The semantic version of the component. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the component. Describes the contents of the component.</p>"""
    change_description: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The change description of the component. This description indicates the change that has been made in this version, or what makes this version different from other versions of the component.</p>"""
    type: "capo_imagebuilder.types.component_type.ComponentType"
    """<p>The type of the component denotes whether the component is used to build the image, or only to test it.</p>"""
    format: "capo_imagebuilder.types.component_format.ComponentFormat"
    """<p>The format of the resource that you want to import as a component.</p>"""
    platform: "capo_imagebuilder.types.platform.Platform"
    """<p>The platform of the component.</p>"""
    data: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The data of the component. For the <code>SHELL</code> format, this is the plain script content. You must specify exactly one of the <code>data</code> or <code>uri</code> properties. For scripts that exceed the inline length constraint, use the <code>uri</code> property.</p>"""
    uri: NotRequired["capo_imagebuilder.types.uri.Uri"]
    """<p>The uri of the component. Must be an Amazon S3 URL and you must have permission to access the Amazon S3 bucket. If you use Amazon S3, you can specify component content up to your service quota. Either <code>data</code> or <code>uri</code> can be used to specify the data within the component.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the component data with a KMS key that Image Builder owns.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the component.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportComponentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["semanticVersion"] = value["semantic_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    import capo_imagebuilder.types.component_type

    out["type"] = capo_imagebuilder.types.component_type.serialize_json(value["type"])
    import capo_imagebuilder.types.component_format

    out["format"] = capo_imagebuilder.types.component_format.serialize_json(
        value["format"]
    )
    import capo_imagebuilder.types.platform

    out["platform"] = capo_imagebuilder.types.platform.serialize_json(value["platform"])
    if "data" in value:
        out["data"] = value["data"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportComponentRequest:
    out: ImportComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportComponentRequest.name required")
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("ImportComponentRequest.semantic_version required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("changeDescription") is not None:
        out["change_description"] = data["changeDescription"]
    if data.get("type") is not None:
        import capo_imagebuilder.types.component_type

        out["type"] = capo_imagebuilder.types.component_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.type required")
    if data.get("format") is not None:
        import capo_imagebuilder.types.component_format

        out["format"] = capo_imagebuilder.types.component_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.format required")
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    else:
        raise DeserializationError("ImportComponentRequest.platform required")
    if data.get("data") is not None:
        out["data"] = data["data"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("ImportComponentRequest.client_token required")
    return out
