"""Generated from Smithy shape ``com.amazonaws.sfn#CreateActivityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.name
    import capo_sfn.types.tag_list


class CreateActivityInput(TypedDict, closed=True):
    name: "capo_sfn.types.name.Name"
    r"""<p>The name of the activity to create. This name must be unique for your Amazon Web Services account and region.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    tags: NotRequired["capo_sfn.types.tag_list.TagList"]
    """<p>The list of tags to add to a resource.</p> <p>An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateActivityInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "tags" in value:
        import capo_sfn.types.tag_list

        out["tags"] = capo_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
    if "encryption_configuration" in value:
        import capo_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateActivityInput:
    out: CreateActivityInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateActivityInput.name required")
    if data.get("tags") is not None:
        import capo_sfn.types.tag_list

        out["tags"] = capo_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    if data.get("encryptionConfiguration") is not None:
        import capo_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
