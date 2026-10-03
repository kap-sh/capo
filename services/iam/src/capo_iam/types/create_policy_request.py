"""Generated from Smithy shape ``com.amazonaws.iam#CreatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.policy_description_type
    import capo_iam.types.policy_document_type
    import capo_iam.types.policy_name_type
    import capo_iam.types.policy_path_type
    import capo_iam.types.tag_list_type


class CreatePolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iam.types.policy_name_type.policyNameType"
    """<p>The friendly name of the policy.</p> <p>IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both "MyResource" and "myresource".</p>"""
    path: NotRequired["capo_iam.types.policy_path_type.policyPathType"]
    r"""<p>The path for the policy.</p> <p>For more information about paths, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html">IAM identifiers</a> in the <i>IAM User Guide</i>.</p> <p>This parameter is optional. If it is not included, it defaults to a slash (/).</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</p> <note> <p>You cannot use an asterisk (*) in the path name.</p> </note>"""
    policy_document: "capo_iam.types.policy_document_type.policyDocumentType"
    r"""<p>The JSON policy document that you want to use as the content for the new policy.</p> <p>You must provide policies in JSON format in IAM. However, for CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.</p> <p>The maximum length of the policy document that you can pass in this operation, including whitespace, is listed below. To view the maximum character counts of a managed policy with no whitespaces, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entity-length">IAM and STS character quotas</a>.</p> <p>To learn more about JSON policy grammar, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html">Grammar of the IAM JSON policy language</a> in the <i>IAM User Guide</i>. </p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> used to validate this parameter is a string of characters consisting of the following:</p> <ul> <li> <p>Any printable ASCII character ranging from the space character (<code>\u0020</code>) through the end of the ASCII character range</p> </li> <li> <p>The printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>)</p> </li> <li> <p>The special characters tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>)</p> </li> </ul>"""
    description: NotRequired[
        "capo_iam.types.policy_description_type.policyDescriptionType"
    ]
    """<p>A friendly description of the policy.</p> <p>Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables."</p> <p>The policy description is immutable. After a value is assigned, it cannot be changed.</p>"""
    tags: NotRequired["capo_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that you want to attach to the new IAM customer managed policy. Each tag consists of a key name and an associated value. For more information about tagging, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p> <note> <p>If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    pairs.append((f"{key_prefix}PolicyDocument", str(value["policy_document"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_iam.types.tag_list_type

        capo_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreatePolicyRequest:
    out: CreatePolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("CreatePolicyRequest.policy_name required")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    else:
        raise DeserializationError("CreatePolicyRequest.policy_document required")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
