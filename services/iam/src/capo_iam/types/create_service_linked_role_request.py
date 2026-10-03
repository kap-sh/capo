"""Generated from Smithy shape ``com.amazonaws.iam#CreateServiceLinkedRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.custom_suffix_type
    import capo_iam.types.group_name_type
    import capo_iam.types.role_description_type


class CreateServiceLinkedRoleRequest(TypedDict, closed=True):
    aws_service_name: "capo_iam.types.group_name_type.groupNameType"
    """<p>The service principal for the Amazon Web Services service to which this role is attached. You use a string similar to a URL but without the http:// in front. For example: <code>elasticbeanstalk.amazonaws.com</code>. </p> <p>Service principals are unique and case-sensitive. To find the exact service principal for your service-linked role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html">Amazon Web Services services that work with IAM</a> in the <i>IAM User Guide</i>. Look for the services that have <b>Yes </b>in the <b>Service-Linked Role</b> column. Choose the <b>Yes</b> link to view the service-linked role documentation for that service.</p>"""
    description: NotRequired["capo_iam.types.role_description_type.roleDescriptionType"]
    """<p>The description of the role.</p>"""
    custom_suffix: NotRequired["capo_iam.types.custom_suffix_type.customSuffixType"]
    """<p></p> <p>A string that you provide, which is combined with the service-provided prefix to form the complete role name. If you make multiple requests for the same service, then you must supply a different <code>CustomSuffix</code> for each request. Otherwise the request fails with a duplicate role name error. For example, you could add <code>-1</code> or <code>-debug</code> to the suffix.</p> <p>Some services do not support the <code>CustomSuffix</code> parameter. If you provide an optional suffix and the operation fails, try the operation again without the suffix.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateServiceLinkedRoleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}AWSServiceName", str(value["aws_service_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "custom_suffix" in value:
        pairs.append((f"{key_prefix}CustomSuffix", str(value["custom_suffix"])))


def deserialize_query(el: Element) -> CreateServiceLinkedRoleRequest:
    out: CreateServiceLinkedRoleRequest = {}  # type: ignore[typeddict-item]
    child_aws_service_name = el.find("AWSServiceName")
    if child_aws_service_name is not None:
        out["aws_service_name"] = str(child_aws_service_name.text or "")
    else:
        raise DeserializationError(
            "CreateServiceLinkedRoleRequest.aws_service_name required"
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_custom_suffix = el.find("CustomSuffix")
    if child_custom_suffix is not None:
        out["custom_suffix"] = str(child_custom_suffix.text or "")
    return out
