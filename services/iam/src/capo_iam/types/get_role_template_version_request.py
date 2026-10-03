"""Generated from Smithy shape ``com.amazonaws.iam#GetRoleTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.minor_version_type


class GetRoleTemplateVersionRequest(TypedDict, closed=True):
    template_arn: "capo_iam.types.arn_type.arnType"
    """<p>The Amazon Resource Name (ARN) of the role template whose version you want to retrieve.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    minor_version: NotRequired["capo_iam.types.minor_version_type.minorVersionType"]
    """<p>The minor version of the role template to retrieve. If you do not specify a minor version, the service returns the template's default minor version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetRoleTemplateVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TemplateArn", str(value["template_arn"])))
    if "minor_version" in value:
        pairs.append((f"{key_prefix}MinorVersion", str(value["minor_version"])))


def deserialize_query(el: Element) -> GetRoleTemplateVersionRequest:
    out: GetRoleTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    child_template_arn = el.find("TemplateArn")
    if child_template_arn is not None:
        out["template_arn"] = str(child_template_arn.text or "")
    else:
        raise DeserializationError(
            "GetRoleTemplateVersionRequest.template_arn required"
        )
    child_minor_version = el.find("MinorVersion")
    if child_minor_version is not None:
        out["minor_version"] = int(child_minor_version.text or "")
    return out
